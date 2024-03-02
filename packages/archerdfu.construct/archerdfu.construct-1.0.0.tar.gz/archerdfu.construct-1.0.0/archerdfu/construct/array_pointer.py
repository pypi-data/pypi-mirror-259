from construct import evaluate, stream_tell, stream_seek, ListContainer, RangeError, Subconstruct


class ArrayPointer(Subconstruct):
    """
    Custom Subconstruct that can make pointers from previous defined Array to target Array to link them
    """
    def __init__(self, count, target_arr: str, target_offset: str, subcon, src_arr: str, src_field: str,
                 stream=None, discard=False):
        super(ArrayPointer, self).__init__(subcon)
        self.flagbuildnone = True

        self.count = count
        self.tar_arr = target_arr
        self.tar_oft = target_offset
        self.src_arr = src_arr
        self.src_field = src_field
        self.stream = stream
        self.discard = discard

    @staticmethod
    def ctx_by_path(context, path: str):
        cur_path = []
        for inner_field in path.split('.'):
            cur_path.append(f'({inner_field})')
            context = context.get(inner_field, None)
            if context is None:
                raise KeyError(' -> '.join(cur_path))
        return context

    def _parse(self, stream, context, path):
        obj = ListContainer()
        return obj

    def _build(self, obj, stream, context, path):
        src_arr = ArrayPointer.ctx_by_path(context, self.src_arr)
        tar_arr = ArrayPointer.ctx_by_path(context, self.tar_arr)
        count = ArrayPointer.ctx_by_path(context, self.count)

        if not 0 <= count:
            raise RangeError("invalid count %s" % (count,), path=path)
        if not (len(src_arr) == len(tar_arr) == count):
            raise RangeError(f"expected {count} elements, found {len(src_arr)}: %d, target: {len(tar_arr)}", path=path)

        discard = self.discard
        retlist = ListContainer()

        for i in range(count):
            target_offset = ArrayPointer.ctx_by_path(tar_arr[i], self.tar_oft)
            obj = ArrayPointer.ctx_by_path(src_arr[i], self.src_field)

            offset = evaluate(target_offset, context)
            stream = evaluate(self.stream, context) or stream
            fallback = stream_tell(stream, path)
            stream_seek(stream, offset, 2 if offset < 0 else 0, path)
            buildret = self.subcon._build(obj, stream, context, path)
            # self.subcon._build(obj, stream, context, path)
            stream_seek(stream, fallback, 0, path)
            if not discard:
                retlist.append(buildret)

        return retlist
        # return self.subcon._build(obj, stream, context, path)

    def _sizeof(self, context, path):
        return 0
