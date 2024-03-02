from construct.core import *

DEFAULT_ENCODING = 'ascii'
__all__ = ['CStringPadded']


CP1251 = 'cp1251'


class TruncatedString:
    """Used internally"""

    def __init__(self, data: str, encoding='ascii', *args, **kwargs):
        self.__data = data
        self.__encoding = encoding

    def __len__(self):
        return len(self.__data)

    def __str__(self):
        if self.__data.find(b'\x00'):
            string = self.__data.split(b'\x00')[0]
        return string.decode(self.__encoding, errors='replace')

    def __repr__(self):
        return self.__str__()

    @property
    def data(self):
        return self.__data.decode(self.__encoding, errors='replace')

    def decode(self, obj):
        return self


class StringEncodedUnstrict(StringEncoded):
    """
    Used internally.
    Ignores encoding error if needed
    """

    def __init__(self, subcon, encoding, strict=False):
        self.strict = strict
        super().__init__(subcon, encoding)
        if not encoding:
            raise StringError("String* classes require explicit encoding")
        self.encoding = encoding

    def _decode(self, obj, context, path):

        if isinstance(obj, str):

            # drop data after terminator
            if obj.find(b'\x00'):
                obj = obj.split(b'\x00')[0]
            return str(TruncatedString(obj))

        if isinstance(obj, bytes):
            if not self.strict:
                return obj.decode(self.encoding, errors='replace')

            return obj.decode(self.encoding)
        return obj

    def _encode(self, obj, context, path):
        if isinstance(obj, TruncatedString):
            obj = str(obj)

        # if not isinstance(obj, unicodestringtype):
        #     raise StringError("string encoding failed, expected unicode string", path=path)
        if obj == u"":
            return b""
        if isinstance(obj, str):
            if not self.strict:
                return obj.encode(self.encoding, errors='replace')
            return obj.encode(self.encoding)
        return obj


class FixedStrippedSized(FixedSized):
    """
    Used internally.
    Strip string len to required and removing it's last char
    """

    def _build(self, obj, stream, context: Container, path):
        length = evaluate(self.length, context)
        if length < 0:
            raise PaddingError("length cannot be negative", path=path)
        stream2 = io.BytesIO()
        buildret = self.subcon._build(obj, stream2, context, path)
        data = stream2.getvalue()

        # strip data to length
        data = data[:length - 1]
        pad = length - len(data)

        if pad < 0:
            raise PaddingError("subcon build %d bytes but was allowed only %d" % (len(data), length), path=path)
        stream_write(stream, data, len(data), path)
        stream_write(stream, bytes(pad), pad, path)
        return buildret


def CStringPadded(length=1, encoding='utf-8', strict=False, pad=None):
    """
    Strip string len to required and removing it's last char,
    after make it NullStripped, can ignore encoding errors
    """
    SKIP_DEFAULT_ENCODING = 'utf-8'

    macro = StringEncodedUnstrict(FixedStrippedSized(length, NullStripped(
        GreedyBytes,
        pad=encodingunit(SKIP_DEFAULT_ENCODING)
    )), encoding, strict)

    def _emitfulltype(ksy, bitwise):
        return dict(size=length, type="strz", encoding=encoding)

    macro._emitfulltype = _emitfulltype
    return macro


def Str1251(length: [int, callable]):
    return CStringPadded(length, CP1251)
