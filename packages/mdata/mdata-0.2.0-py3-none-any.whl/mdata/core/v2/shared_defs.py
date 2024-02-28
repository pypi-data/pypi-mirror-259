from enum import Enum
from typing import TypeAlias, Literal, Union

from mdata.core.shared_defs import SpecLabel, ObservationTypeValue
from mdata.core.util import StringEnumeration

SegmentDefinitionTypeValue = Literal['S', 'SD']
SegmentPropertyValue = str
DataTypeLabelValue = Union[ObservationTypeValue, SegmentDefinitionTypeValue]
SpecIdentifier = tuple[DataTypeLabelValue, SpecLabel]


class SegmentDefinitionTypes(StringEnumeration):
    Segments: SegmentDefinitionTypeValue = 'S'
    SegmentData: SegmentDefinitionTypeValue = 'SD'


class SegmentDefinitionType(Enum):
    Segments = 'S'
    SegmentData = 'SD'


class SegmentConcepts(StringEnumeration):
    Object = 'object'
    Segment = 'segment'
    Index = 'segment_index'
    Label = 'label'
    Start = 'start'
    End = 'end'

    segment_columns = [Object, Segment, Index, Start, End]
    segmentdata_columns = [Object, Segment, Index, Label]


class ExtendedSegmentConcepts(SegmentConcepts):
    SegmentInterval = 'segment_interval'


class SegmentProperties(StringEnumeration):
    Monotonic: SegmentPropertyValue = 'monotonic'
    Disjoint: SegmentPropertyValue = 'disjoint'
    Seamless: SegmentPropertyValue = 'seamless'
    Complete: SegmentPropertyValue = 'complete'


class SegmentProperty(Enum):
    Monotonic = 'monotonic'
    Disjoint = 'disjoint'
    Seamless = 'seamless'
    Complete = 'complete'


SegmentSpecLabel: TypeAlias = SpecLabel
SegmentDataSpecLabel: TypeAlias = SpecLabel
