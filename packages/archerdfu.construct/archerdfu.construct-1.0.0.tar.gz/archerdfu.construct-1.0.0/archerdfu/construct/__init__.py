"""Classes that extends standard construct library to make functionality more flexible"""

from construct import *

from .padded_cstring import CStringPadded, Str1251, CP1251
from .detailed import Anchor
from .checksum_stream import ChecksumStream
from .array_pointer import ArrayPointer
from . import jsonify


Arr = Array
Def = Default
Reb = Rebuild
Crc = Checksum
Idx = Index
Ptr = Pointer
Raw = RawCopy
Pad = Padding

PCStr = CStringPadded
StreamCrc = ChecksumStream
ArrPtr = ArrayPointer
