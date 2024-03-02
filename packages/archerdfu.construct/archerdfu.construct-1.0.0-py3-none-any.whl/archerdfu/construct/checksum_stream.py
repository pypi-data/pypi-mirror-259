import binascii

from construct import ChecksumError, Checksum, bytestringtype


class ChecksumStream(Checksum):
    """
    Custom Checksum Subconstruct to chercksuming data in current stream instead of context
    """
    def _parse(self, stream, context, path):
        hash1 = self.checksumfield._parsereport(stream, context, path)
        hash2 = self.hashfunc(self.bytesfunc(stream, context))
        if hash1 != hash2:
            raise ChecksumError(
                "wrong checksum, read %r, computed %r" % (
                    hash1 if not isinstance(hash1, bytestringtype) else binascii.hexlify(hash1),
                    hash2 if not isinstance(hash2, bytestringtype) else binascii.hexlify(hash2),),
                path=path
            )
        return hash1

    def _build(self, obj, stream, context, path):
        hash2 = self.hashfunc(self.bytesfunc(stream, context))
        self.checksumfield._build(hash2, stream, context, path)
        return hash2
