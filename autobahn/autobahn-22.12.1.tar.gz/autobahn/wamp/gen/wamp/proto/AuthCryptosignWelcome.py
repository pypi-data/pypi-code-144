# automatically generated by the FlatBuffers compiler, do not modify

# namespace: proto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AuthCryptosignWelcome(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AuthCryptosignWelcome()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAuthCryptosignWelcome(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # AuthCryptosignWelcome
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def AuthCryptosignWelcomeStart(builder): builder.StartObject(0)
def Start(builder):
    return AuthCryptosignWelcomeStart(builder)
def AuthCryptosignWelcomeEnd(builder): return builder.EndObject()
def End(builder):
    return AuthCryptosignWelcomeEnd(builder)