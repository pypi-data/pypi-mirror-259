from __future__ import annotations

from collections.abc import Set, Mapping, Sequence
from dataclasses import dataclass
from typing import Generic, Optional, Iterable, TypedDict, Required, Callable, Any

import pandas as pd

from . import ObservationSeriesDef
from .base import SpecFac, ContFac, cont_fac_for_cls, spec_fac_for_cls, MDFac, md_fac_for_cls, CombContFac, \
    comb_cont_fac_for_cls
from .factories import Factory, match_def_and_df, _prep_series_container_df
from ..header import Meta
from ..protocols import ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC, MD
from ..raw import FeatureMetadata
from ..shared_defs import Extension, SpecLabel, only_feature_columns
from ..v2.header_v2 import SegmentSpec, SegmentDataSpec
from ..v2.machine_data_v2 import SegmentSeriesSpec, SegmentsContainer, SegmentDataSeriesSpec, \
    SegmentDataContainer, MachineDataV2
from ..v2.protocols_v2 import SSSpec, SDSSpec, SSContainer, SDSContainer, MachineDataV2Protocol, MDV2, SDSView
from ..v2.raw_v2 import SegmentMetadata
from ..v2.shared_defs import SegmentConcepts

s_columns_def = {SegmentConcepts.Object: str, SegmentConcepts.Segment: str,
                 SegmentConcepts.Start: str, SegmentConcepts.End: str,
                 SegmentConcepts.Object + '_col': str,
                 SegmentConcepts.Segment + '_col': str,
                 SegmentConcepts.Start + '_col': str, SegmentConcepts.End + '_col': str}

sd_columns_def = {SegmentConcepts.Object: str, SegmentConcepts.Segment: str,
                  SegmentConcepts.Label: str, SegmentConcepts.Object + '_col': str,
                  SegmentConcepts.Segment + '_col': str,
                  SegmentConcepts.Label + '_col': str}

SColumnsDef = TypedDict('SColumnsDef', s_columns_def)
SDColumnsDef = TypedDict('SDColumnsDef', sd_columns_def)

SegmentsDef = TypedDict('SegmentsDef', {'df': Required[pd.DataFrame],
                                        'segment_metadata': Mapping[str, SegmentMetadata],
                                        'preserve_full_df': bool} | s_columns_def)
SegmentDataDef = TypedDict('SegmentDataDef',
                           {'df': Required[pd.DataFrame], 'feature_metadata': Mapping[str, FeatureMetadata],
                            'feature_columns': Sequence[str]} | sd_columns_def)


def define_segment_data_series_defs_by_groupby(df: pd.DataFrame, key: str | list[str],
                                               func: Callable[[Any, pd.DataFrame], SegmentDataDef] = lambda
                                                       g, g_df: SegmentDataDef(df=g_df)) -> list[SegmentDataDef]:
    return [func(g, df.loc[idx]) for g, idx in df.groupby(by=key).groups.items()]


def prepare_segments_df(df: pd.DataFrame, copy=False, **kwargs: SColumnsDef) -> (
        pd.DataFrame, list[SpecLabel]):
    df = df.copy() if copy else df

    object_def = match_def_and_df(kwargs, df, SegmentConcepts.Object, 0)
    segment_def = match_def_and_df(kwargs, df, SegmentConcepts.Segment, 1)
    index_def = match_def_and_df(kwargs, df, SegmentConcepts.Index, 2)
    start_def = match_def_and_df(kwargs, df, SegmentConcepts.Start, 3, is_dt_type=True)
    end_def = match_def_and_df(kwargs, df, SegmentConcepts.End, 4, is_dt_type=True)
    assert object_def is not None
    assert segment_def is not None
    assert index_def is not None
    assert start_def is not None
    assert end_def is not None

    if not kwargs.get('preserve_full_df'):
        df = df[SegmentConcepts.segment_columns]

    return df, df[SegmentConcepts.Segment].unique().tolist()


def prepare_segment_data_df(df: pd.DataFrame, copy=False, **kwargs: SDColumnsDef) -> (
        pd.DataFrame, SpecLabel):
    df = df.copy() if copy else df

    object_def = match_def_and_df(kwargs, df, SegmentConcepts.Object, 0)
    segment_def = match_def_and_df(kwargs, df, SegmentConcepts.Segment, 1)
    index_def = match_def_and_df(kwargs, df, SegmentConcepts.Index, 2)
    label_def = match_def_and_df(kwargs, df, SegmentConcepts.Label, 3)
    assert object_def is not None
    assert segment_def is not None
    assert index_def is not None
    assert label_def is not None

    if (fc := kwargs.get('feature_columns')) is not None:
        df = df[SegmentConcepts.segmentdata_columns + list(fc)]

    return df, label_def


@dataclass
class ExtendedFactory(Factory[ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC, MD], Generic[
    ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC, MD, SSSpec, SSContainer, SDSSpec, SDSView, SDSContainer, MDV2]):
    _ss_spec_cls: type[SSSpec]
    _ss_cont_cls: type[SSContainer]
    _sds_spec_cls: type[SDSSpec]
    _sds_view_cls: type[SDSView]
    _sds_cont_cls: type[SDSContainer]
    _md_v2_cls: type[MachineDataV2Protocol[
        ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC, SSSpec, SSContainer, SDSSpec, SDSView, SDSContainer]]

    def __post_init__(self):
        super().__post_init__()
        self._ss_spec_factory = spec_fac_for_cls(SegmentSpecFactory, SegmentSpec, self._ss_spec_cls)
        self._sds_spec_factory = spec_fac_for_cls(SegmentDataSpecFactory, SegmentDataSpec, self._sds_spec_cls)
        self._ss_cont_factory = comb_cont_fac_for_cls(SegmentContainerFactory, self._ss_spec_cls, self._ss_cont_cls)
        self._sds_cont_factory = cont_fac_for_cls(SegmentDataContainerFactory, self._sds_spec_cls, self._sds_cont_cls)
        self._md_v2_factory = md_fac_for_cls(MachineDataV2Factory, self._md_v2_cls)

    @property
    def supported_extensions(self) -> Set[Extension]:
        return self._md_v2_cls.supported_extensions

    def make_segment_spec(self, label: SpecLabel, base_spec: SegmentSpec) -> SSSpec:
        return self._ss_spec_factory.make(label, base_spec)

    def make_segment_data_spec(self, label: SpecLabel, base_spec: SegmentDataSpec) -> SDSSpec:
        return self._sds_spec_factory.make(label, base_spec)

    def make_segment_spec_from_data(self, label: SpecLabel, df: pd.DataFrame,
                                    extra_metadata: SegmentMetadata) -> SSSpec:
        df = df.loc[df[SegmentConcepts.Segment] == label]
        from mdata.core.extensions.segments.properties import derive_segments_properties

        defined_props = extra_metadata.get('properties', []) if extra_metadata else []
        props = derive_segments_properties(df, claimed=set(defined_props))

        ss = SegmentSpec(label, long_name=(extra_metadata.get('long_name', label) if extra_metadata else label),
                         properties=props)

        return self.make_segment_spec(label, ss)

    def make_segment_data_spec_from_data(self, label: SpecLabel, df: pd.DataFrame,
                                         extra_metadata: Mapping[str, FeatureMetadata]) -> SDSSpec:
        features = only_feature_columns(df.columns, SegmentConcepts.segmentdata_columns)
        base_spec = SegmentDataSpec.from_raw(
            [({f: extra_metadata[f]} if (extra_metadata and f in extra_metadata) else f) for f in features])
        return self.make_segment_data_spec(label, base_spec)

    def make_segments_container(self, specs: list[SegmentSeriesSpec], df: pd.DataFrame, copy=False) -> SSContainer:
        return self._ss_cont_factory.make(specs, df.copy() if copy else df)

    def make_segments_container_from_data(self, segments_def: SegmentsDef, copy=False) -> SSContainer:
        df, segments_list = prepare_segments_df(copy=copy, **segments_def)
        segment_specs = [
            self.make_segment_spec_from_data(label, df, extra_metadata=segments_def.get('segment_metadata')) for label
            in segments_list]
        return self.make_segments_container(segment_specs, df, copy=False)

    def make_segment_data_container(self, spec: SegmentDataSeriesSpec, df: pd.DataFrame, copy=True,
                                    convert_dtypes=False) -> SDSContainer:
        df = _prep_series_container_df(spec, df, copy=copy, convert_dtypes=convert_dtypes)
        return self._sds_cont_factory.make(spec, df)

    def make_segment_data_container_from_data(self, segment_data_def: SegmentDataDef, copy=True,
                                              convert_dtypes=False) -> SDSContainer:
        df, label = prepare_segment_data_df(copy=copy, **segment_data_def)
        spec = self.make_segment_data_spec_from_data(label, df, extra_metadata=segment_data_def.get('feature_metadata'))
        return self.make_segment_data_container(spec, df, copy=False, convert_dtypes=convert_dtypes)

    def make_from_data(self, *series_defs: ObservationSeriesDef, meta: Meta = Meta.of(extensions=[Extension.Metadata, Extension.Segments]), sort_by_time=True, copy_dfs=True,
                       convert_dtypes=False, lazy=False, segment_defs: SegmentsDef = None,
                       segment_data_defs: Iterable[SegmentDataDef] = ()) -> MachineDataV2Protocol[
        ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC, SSSpec, SSContainer, SDSSpec, SDSView, SDSContainer]:

        md_v1 = super().make_from_data(*series_defs, sort_by_time=sort_by_time, copy_dfs=copy_dfs,
                                       convert_dtypes=convert_dtypes, lazy=True, meta=meta)

        segments = None
        segment_data = None
        if segment_defs is not None:
            segments = self.make_segments_container_from_data(segment_defs, copy=copy_dfs)

        if segment_data_defs is not None:
            segment_data = [
                self.make_segment_data_container_from_data(seg_data_def, copy=copy_dfs, convert_dtypes=convert_dtypes) for
                seg_data_def in segment_data_defs] if segment_data_defs else []

        return self.make(meta=meta, events=md_v1.event_series.values(), measurements=md_v1.measurement_series.values(),
                         segments=segments, segment_data=segment_data,
                         sort_by_time=sort_by_time, lazy=lazy)

    def make(self, meta: Meta = Meta(), events: Iterable[ETSC] = (), measurements: Iterable[MTSC] = (),
             index_frame: pd.DataFrame = None,
             lazy=True,
             segments: Optional[SSContainer] = None, segment_data: Iterable[SDSContainer] = (),
             **kwargs) -> \
            MachineDataV2Protocol[
                ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC, SSSpec, SSContainer, SDSSpec, SDSView, SDSContainer]:
        return self._md_v2_factory.make(meta=meta, events=events, measurements=measurements, index_frame=index_frame,
                                        lazy=lazy, segments=segments, segment_data=segment_data, **kwargs)


class SegmentSpecFactory(SpecFac[SegmentSpec, SSSpec]):
    constructors = {SegmentSeriesSpec: SegmentSeriesSpec.of}


class SegmentDataSpecFactory(SpecFac[SegmentDataSpec, SDSSpec]):
    constructors = {SegmentDataSpec: SegmentDataSeriesSpec.of}


class SegmentContainerFactory(CombContFac[SSSpec, SSContainer]):
    constructors = {SegmentsContainer: SegmentsContainer.of}


class SegmentDataContainerFactory(ContFac[SDSSpec, SDSContainer]):
    constructors = {SegmentDataContainer: SegmentDataContainer.of}


class MachineDataV2Factory(MDFac[MDV2]):
    constructors = {MachineDataV2: MachineDataV2.of}

    def make(self, meta: Meta, events: Iterable[ETSC], measurements: Iterable[MTSC], index_frame: pd.DataFrame = None,
             lazy=True,
             segments: Optional[SSContainer] = None, segment_data: Iterable[SDSContainer] = (),
             **kwargs) -> MDV2:
        return super().make(meta=meta, events=events, measurements=measurements, index_frame=index_frame,
                            lazy_map_creation=lazy, lazy_index_creation=lazy, segments=segments,
                            segment_data=segment_data, **kwargs)
