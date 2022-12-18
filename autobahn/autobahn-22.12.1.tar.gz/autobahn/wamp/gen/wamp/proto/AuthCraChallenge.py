# automatically generated by the FlatBuffers compiler, do not modify

# namespace: proto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AuthCraChallenge(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AuthCraChallenge()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAuthCraChallenge(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # AuthCraChallenge
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AuthCraChallenge
    def Challenge(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AuthCraChallenge
    def Salt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AuthCraChallenge
    def Iterations(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 1000

    # AuthCraChallenge
    def Keylen(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 32

def AuthCraChallengeStart(builder): builder.StartObject(4)
def Start(builder):
    return AuthCraChallengeStart(builder)
def AuthCraChallengeAddChallenge(builder, challenge): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(challenge), 0)
def AddChallenge(builder, challenge):
    return AuthCraChallengeAddChallenge(builder, challenge)
def AuthCraChallengeAddSalt(builder, salt): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(salt), 0)
def AddSalt(builder, salt):
    return AuthCraChallengeAddSalt(builder, salt)
def AuthCraChallengeAddIterations(builder, iterations): builder.PrependUint32Slot(2, iterations, 1000)
def AddIterations(builder, iterations):
    return AuthCraChallengeAddIterations(builder, iterations)
def AuthCraChallengeAddKeylen(builder, keylen): builder.PrependUint8Slot(3, keylen, 32)
def AddKeylen(builder, keylen):
    return AuthCraChallengeAddKeylen(builder, keylen)
def AuthCraChallengeEnd(builder): return builder.EndObject()
def End(builder):
    return AuthCraChallengeEnd(builder)