# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FieldRewardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FieldRewardExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFieldRewardExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # FieldRewardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FieldRewardExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FieldRewardExcel
    def RewardProb(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # FieldRewardExcel
    def RewardParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # FieldRewardExcel
    def RewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FieldRewardExcel
    def RewardAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(5)
def FieldRewardExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddGroupId(builder, GroupId): builder.PrependInt64Slot(0, GroupId, 0)
def FieldRewardExcelAddGroupId(builder, GroupId):
    """This method is deprecated. Please switch to AddGroupId."""
    return AddGroupId(builder, GroupId)
def AddRewardProb(builder, RewardProb): builder.PrependInt32Slot(1, RewardProb, 0)
def FieldRewardExcelAddRewardProb(builder, RewardProb):
    """This method is deprecated. Please switch to AddRewardProb."""
    return AddRewardProb(builder, RewardProb)
def AddRewardParcelType(builder, RewardParcelType): builder.PrependInt32Slot(2, RewardParcelType, 0)
def FieldRewardExcelAddRewardParcelType(builder, RewardParcelType):
    """This method is deprecated. Please switch to AddRewardParcelType."""
    return AddRewardParcelType(builder, RewardParcelType)
def AddRewardId(builder, RewardId): builder.PrependInt64Slot(3, RewardId, 0)
def FieldRewardExcelAddRewardId(builder, RewardId):
    """This method is deprecated. Please switch to AddRewardId."""
    return AddRewardId(builder, RewardId)
def AddRewardAmount(builder, RewardAmount): builder.PrependInt32Slot(4, RewardAmount, 0)
def FieldRewardExcelAddRewardAmount(builder, RewardAmount):
    """This method is deprecated. Please switch to AddRewardAmount."""
    return AddRewardAmount(builder, RewardAmount)
def End(builder): return builder.EndObject()
def FieldRewardExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)