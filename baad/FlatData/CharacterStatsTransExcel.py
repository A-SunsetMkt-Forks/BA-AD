# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterStatsTransExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterStatsTransExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCharacterStatsTransExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CharacterStatsTransExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CharacterStatsTransExcel
    def TransSupportStats(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterStatsTransExcel
    def EchelonExtensionType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterStatsTransExcel
    def TransSupportStatsFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterStatsTransExcel
    def StatTransType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(4)
def CharacterStatsTransExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddTransSupportStats(builder, TransSupportStats): builder.PrependInt32Slot(0, TransSupportStats, 0)
def CharacterStatsTransExcelAddTransSupportStats(builder, TransSupportStats):
    """This method is deprecated. Please switch to AddTransSupportStats."""
    return AddTransSupportStats(builder, TransSupportStats)
def AddEchelonExtensionType_(builder, EchelonExtensionType_): builder.PrependInt32Slot(1, EchelonExtensionType_, 0)
def CharacterStatsTransExcelAddEchelonExtensionType_(builder, EchelonExtensionType_):
    """This method is deprecated. Please switch to AddEchelonExtensionType_."""
    return AddEchelonExtensionType_(builder, EchelonExtensionType_)
def AddTransSupportStatsFactor(builder, TransSupportStatsFactor): builder.PrependInt32Slot(2, TransSupportStatsFactor, 0)
def CharacterStatsTransExcelAddTransSupportStatsFactor(builder, TransSupportStatsFactor):
    """This method is deprecated. Please switch to AddTransSupportStatsFactor."""
    return AddTransSupportStatsFactor(builder, TransSupportStatsFactor)
def AddStatTransType_(builder, StatTransType_): builder.PrependInt32Slot(3, StatTransType_, 0)
def CharacterStatsTransExcelAddStatTransType_(builder, StatTransType_):
    """This method is deprecated. Please switch to AddStatTransType_."""
    return AddStatTransType_(builder, StatTransType_)
def End(builder): return builder.EndObject()
def CharacterStatsTransExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)