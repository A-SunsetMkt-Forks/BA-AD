# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestRewardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestRewardExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsConquestRewardExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ConquestRewardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConquestRewardExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConquestRewardExcel
    def RewardTag_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestRewardExcel
    def RewardProb(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestRewardExcel
    def RewardParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestRewardExcel
    def RewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConquestRewardExcel
    def RewardAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestRewardExcel
    def IsDisplayed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def Start(builder): builder.StartObject(7)
def ConquestRewardExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddGroupId(builder, GroupId): builder.PrependInt64Slot(0, GroupId, 0)
def ConquestRewardExcelAddGroupId(builder, GroupId):
    """This method is deprecated. Please switch to AddGroupId."""
    return AddGroupId(builder, GroupId)
def AddRewardTag_(builder, RewardTag_): builder.PrependInt32Slot(1, RewardTag_, 0)
def ConquestRewardExcelAddRewardTag_(builder, RewardTag_):
    """This method is deprecated. Please switch to AddRewardTag_."""
    return AddRewardTag_(builder, RewardTag_)
def AddRewardProb(builder, RewardProb): builder.PrependInt32Slot(2, RewardProb, 0)
def ConquestRewardExcelAddRewardProb(builder, RewardProb):
    """This method is deprecated. Please switch to AddRewardProb."""
    return AddRewardProb(builder, RewardProb)
def AddRewardParcelType(builder, RewardParcelType): builder.PrependInt32Slot(3, RewardParcelType, 0)
def ConquestRewardExcelAddRewardParcelType(builder, RewardParcelType):
    """This method is deprecated. Please switch to AddRewardParcelType."""
    return AddRewardParcelType(builder, RewardParcelType)
def AddRewardId(builder, RewardId): builder.PrependInt64Slot(4, RewardId, 0)
def ConquestRewardExcelAddRewardId(builder, RewardId):
    """This method is deprecated. Please switch to AddRewardId."""
    return AddRewardId(builder, RewardId)
def AddRewardAmount(builder, RewardAmount): builder.PrependInt32Slot(5, RewardAmount, 0)
def ConquestRewardExcelAddRewardAmount(builder, RewardAmount):
    """This method is deprecated. Please switch to AddRewardAmount."""
    return AddRewardAmount(builder, RewardAmount)
def AddIsDisplayed(builder, IsDisplayed): builder.PrependBoolSlot(6, IsDisplayed, 0)
def ConquestRewardExcelAddIsDisplayed(builder, IsDisplayed):
    """This method is deprecated. Please switch to AddIsDisplayed."""
    return AddIsDisplayed(builder, IsDisplayed)
def End(builder): return builder.EndObject()
def ConquestRewardExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)