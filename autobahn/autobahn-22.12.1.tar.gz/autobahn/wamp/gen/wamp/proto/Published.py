# automatically generated by the FlatBuffers compiler, do not modify

# namespace: proto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Published(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Published()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsPublished(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Published
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Published
    def Session(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Published
    def Request(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Published
    def Publication(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

def PublishedStart(builder): builder.StartObject(3)
def Start(builder):
    return PublishedStart(builder)
def PublishedAddSession(builder, session): builder.PrependUint64Slot(0, session, 0)
def AddSession(builder, session):
    return PublishedAddSession(builder, session)
def PublishedAddRequest(builder, request): builder.PrependUint64Slot(1, request, 0)
def AddRequest(builder, request):
    return PublishedAddRequest(builder, request)
def PublishedAddPublication(builder, publication): builder.PrependUint64Slot(2, publication, 0)
def AddPublication(builder, publication):
    return PublishedAddPublication(builder, publication)
def PublishedEnd(builder): return builder.EndObject()
def End(builder):
    return PublishedEnd(builder)