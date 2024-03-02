
from construct import Container, ListContainer, Subconstruct


class Anchor(Subconstruct):
    """
    Custom Subconstruct for adding to other constructs properties like offsets and others
    depends on Subcon placing in stream
    """

    class AbstractDetailedField:
        """Abstract class for extending with offsets in _detail_field function"""

    def __init__(self, subcon):
        super(Anchor, self).__init__(subcon)
        self.flagbuildnone = True

    def _parse(self, stream, context, path):
        tell1 = stream.tell()
        obj = self.subcon._parsereport(stream, context, path)
        tell2 = stream.tell()
        obj = self._detail(obj, tell1, tell2)
        return obj

    def _build(self, obj, stream, context, path):
        tell1 = stream.tell()
        buildret = self.subcon._build(obj, stream, context, path)
        tell2 = stream.tell()
        buildret = self._detail(buildret, tell1, tell2)
        return buildret

    def _sizeof(self, context, path):
        return self.subcon._sizeof(context, path)

    @classmethod
    def _detail_field(cls, instance, tell1, tell2):
        class DetailedField(instance.__class__, cls.AbstractDetailedField):
            # extending builtin with required data
            def __new__(cls, value, offset1, offset2):
                obj = super().__new__(cls, value)
                obj.offset1 = offset1
                obj.offset2 = offset2
                obj.length = offset2 - offset1
                return obj

            def __getitem__(self, item):
                return self.__getattribute__(item)

            def get(self, key, default=None):
                if hasattr(self, key):
                    return self.__getattribute__(key)
                else:
                    return default

        return DetailedField(instance, tell1, tell2)

    @classmethod
    def _detail_container(cls, instance, tell1, tell2):

        if isinstance(instance, dict):
            container = Container(instance)
        else:
            container = ListContainer(instance)

        # container.__setattr__('offset1', tell1)
        container.offset1 = tell1
        container.__setattr__('offset2', tell2)
        container.__setattr__('length', tell2 - tell1)
        return container

    @classmethod
    def _detail(cls, instance, tell1, tell2):
        if isinstance(instance, cls.AbstractDetailedField):
            return cls._detail_field(instance.__repr__(), tell1, tell2)
        elif isinstance(instance, (dict, list)):
            return cls._detail_container(instance, tell1, tell2)
        else:
            return cls._detail_field(instance, tell1, tell2)
