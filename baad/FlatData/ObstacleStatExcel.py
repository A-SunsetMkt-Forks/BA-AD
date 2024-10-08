# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ObstacleStatExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ObstacleStatExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsObstacleStatExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ObstacleStatExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ObstacleStatExcel
    def StringID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # ObstacleStatExcel
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ObstacleStatExcel
    def MaxHP1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ObstacleStatExcel
    def MaxHP100(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ObstacleStatExcel
    def BlockRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ObstacleStatExcel
    def Dodge(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ObstacleStatExcel
    def CanNotStandRange(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ObstacleStatExcel
    def HighlightFloaterHeight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ObstacleStatExcel
    def EnhanceLightArmorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ObstacleStatExcel
    def EnhanceHeavyArmorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ObstacleStatExcel
    def EnhanceUnarmedRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ObstacleStatExcel
    def EnhanceElasticArmorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ObstacleStatExcel
    def EnhanceStructureRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ObstacleStatExcel
    def EnhanceNormalArmorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ObstacleStatExcel
    def ReduceExDamagedRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(15)
def ObstacleStatExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddStringID(builder, StringID): builder.PrependUint32Slot(0, StringID, 0)
def ObstacleStatExcelAddStringID(builder, StringID):
    """This method is deprecated. Please switch to AddStringID."""
    return AddStringID(builder, StringID)
def AddName(builder, Name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Name), 0)
def ObstacleStatExcelAddName(builder, Name):
    """This method is deprecated. Please switch to AddName."""
    return AddName(builder, Name)
def AddMaxHP1(builder, MaxHP1): builder.PrependInt64Slot(2, MaxHP1, 0)
def ObstacleStatExcelAddMaxHP1(builder, MaxHP1):
    """This method is deprecated. Please switch to AddMaxHP1."""
    return AddMaxHP1(builder, MaxHP1)
def AddMaxHP100(builder, MaxHP100): builder.PrependInt64Slot(3, MaxHP100, 0)
def ObstacleStatExcelAddMaxHP100(builder, MaxHP100):
    """This method is deprecated. Please switch to AddMaxHP100."""
    return AddMaxHP100(builder, MaxHP100)
def AddBlockRate(builder, BlockRate): builder.PrependInt64Slot(4, BlockRate, 0)
def ObstacleStatExcelAddBlockRate(builder, BlockRate):
    """This method is deprecated. Please switch to AddBlockRate."""
    return AddBlockRate(builder, BlockRate)
def AddDodge(builder, Dodge): builder.PrependInt64Slot(5, Dodge, 0)
def ObstacleStatExcelAddDodge(builder, Dodge):
    """This method is deprecated. Please switch to AddDodge."""
    return AddDodge(builder, Dodge)
def AddCanNotStandRange(builder, CanNotStandRange): builder.PrependInt64Slot(6, CanNotStandRange, 0)
def ObstacleStatExcelAddCanNotStandRange(builder, CanNotStandRange):
    """This method is deprecated. Please switch to AddCanNotStandRange."""
    return AddCanNotStandRange(builder, CanNotStandRange)
def AddHighlightFloaterHeight(builder, HighlightFloaterHeight): builder.PrependFloat32Slot(7, HighlightFloaterHeight, 0.0)
def ObstacleStatExcelAddHighlightFloaterHeight(builder, HighlightFloaterHeight):
    """This method is deprecated. Please switch to AddHighlightFloaterHeight."""
    return AddHighlightFloaterHeight(builder, HighlightFloaterHeight)
def AddEnhanceLightArmorRate(builder, EnhanceLightArmorRate): builder.PrependInt64Slot(8, EnhanceLightArmorRate, 0)
def ObstacleStatExcelAddEnhanceLightArmorRate(builder, EnhanceLightArmorRate):
    """This method is deprecated. Please switch to AddEnhanceLightArmorRate."""
    return AddEnhanceLightArmorRate(builder, EnhanceLightArmorRate)
def AddEnhanceHeavyArmorRate(builder, EnhanceHeavyArmorRate): builder.PrependInt64Slot(9, EnhanceHeavyArmorRate, 0)
def ObstacleStatExcelAddEnhanceHeavyArmorRate(builder, EnhanceHeavyArmorRate):
    """This method is deprecated. Please switch to AddEnhanceHeavyArmorRate."""
    return AddEnhanceHeavyArmorRate(builder, EnhanceHeavyArmorRate)
def AddEnhanceUnarmedRate(builder, EnhanceUnarmedRate): builder.PrependInt64Slot(10, EnhanceUnarmedRate, 0)
def ObstacleStatExcelAddEnhanceUnarmedRate(builder, EnhanceUnarmedRate):
    """This method is deprecated. Please switch to AddEnhanceUnarmedRate."""
    return AddEnhanceUnarmedRate(builder, EnhanceUnarmedRate)
def AddEnhanceElasticArmorRate(builder, EnhanceElasticArmorRate): builder.PrependInt64Slot(11, EnhanceElasticArmorRate, 0)
def ObstacleStatExcelAddEnhanceElasticArmorRate(builder, EnhanceElasticArmorRate):
    """This method is deprecated. Please switch to AddEnhanceElasticArmorRate."""
    return AddEnhanceElasticArmorRate(builder, EnhanceElasticArmorRate)
def AddEnhanceStructureRate(builder, EnhanceStructureRate): builder.PrependInt64Slot(12, EnhanceStructureRate, 0)
def ObstacleStatExcelAddEnhanceStructureRate(builder, EnhanceStructureRate):
    """This method is deprecated. Please switch to AddEnhanceStructureRate."""
    return AddEnhanceStructureRate(builder, EnhanceStructureRate)
def AddEnhanceNormalArmorRate(builder, EnhanceNormalArmorRate): builder.PrependInt64Slot(13, EnhanceNormalArmorRate, 0)
def ObstacleStatExcelAddEnhanceNormalArmorRate(builder, EnhanceNormalArmorRate):
    """This method is deprecated. Please switch to AddEnhanceNormalArmorRate."""
    return AddEnhanceNormalArmorRate(builder, EnhanceNormalArmorRate)
def AddReduceExDamagedRate(builder, ReduceExDamagedRate): builder.PrependInt64Slot(14, ReduceExDamagedRate, 0)
def ObstacleStatExcelAddReduceExDamagedRate(builder, ReduceExDamagedRate):
    """This method is deprecated. Please switch to AddReduceExDamagedRate."""
    return AddReduceExDamagedRate(builder, ReduceExDamagedRate)
def End(builder): return builder.EndObject()
def ObstacleStatExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)