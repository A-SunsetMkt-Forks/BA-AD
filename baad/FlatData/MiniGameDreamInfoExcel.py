# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameDreamInfoExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameDreamInfoExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMiniGameDreamInfoExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MiniGameDreamInfoExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MiniGameDreamInfoExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamInfoExcel
    def DreamMakerMultiplierCondition_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamInfoExcel
    def DreamMakerMultiplierConditionValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamInfoExcel
    def DreamMakerMultiplierMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamInfoExcel
    def DreamMakerDays(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamInfoExcel
    def DreamMakerActionPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamInfoExcel
    def DreamMakerParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamInfoExcel
    def DreamMakerParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamInfoExcel
    def DreamMakerDailyPointParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamInfoExcel
    def DreamMakerDailyPointId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamInfoExcel
    def DreamMakerParameterTransfer(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamInfoExcel
    def ScheduleCostGoodsId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamInfoExcel
    def LobbyBGMChangeScenarioId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(13)
def MiniGameDreamInfoExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)
def MiniGameDreamInfoExcelAddEventContentId(builder, EventContentId):
    """This method is deprecated. Please switch to AddEventContentId."""
    return AddEventContentId(builder, EventContentId)
def AddDreamMakerMultiplierCondition_(builder, DreamMakerMultiplierCondition_): builder.PrependInt32Slot(1, DreamMakerMultiplierCondition_, 0)
def MiniGameDreamInfoExcelAddDreamMakerMultiplierCondition_(builder, DreamMakerMultiplierCondition_):
    """This method is deprecated. Please switch to AddDreamMakerMultiplierCondition_."""
    return AddDreamMakerMultiplierCondition_(builder, DreamMakerMultiplierCondition_)
def AddDreamMakerMultiplierConditionValue(builder, DreamMakerMultiplierConditionValue): builder.PrependInt64Slot(2, DreamMakerMultiplierConditionValue, 0)
def MiniGameDreamInfoExcelAddDreamMakerMultiplierConditionValue(builder, DreamMakerMultiplierConditionValue):
    """This method is deprecated. Please switch to AddDreamMakerMultiplierConditionValue."""
    return AddDreamMakerMultiplierConditionValue(builder, DreamMakerMultiplierConditionValue)
def AddDreamMakerMultiplierMax(builder, DreamMakerMultiplierMax): builder.PrependInt64Slot(3, DreamMakerMultiplierMax, 0)
def MiniGameDreamInfoExcelAddDreamMakerMultiplierMax(builder, DreamMakerMultiplierMax):
    """This method is deprecated. Please switch to AddDreamMakerMultiplierMax."""
    return AddDreamMakerMultiplierMax(builder, DreamMakerMultiplierMax)
def AddDreamMakerDays(builder, DreamMakerDays): builder.PrependInt64Slot(4, DreamMakerDays, 0)
def MiniGameDreamInfoExcelAddDreamMakerDays(builder, DreamMakerDays):
    """This method is deprecated. Please switch to AddDreamMakerDays."""
    return AddDreamMakerDays(builder, DreamMakerDays)
def AddDreamMakerActionPoint(builder, DreamMakerActionPoint): builder.PrependInt64Slot(5, DreamMakerActionPoint, 0)
def MiniGameDreamInfoExcelAddDreamMakerActionPoint(builder, DreamMakerActionPoint):
    """This method is deprecated. Please switch to AddDreamMakerActionPoint."""
    return AddDreamMakerActionPoint(builder, DreamMakerActionPoint)
def AddDreamMakerParcelType(builder, DreamMakerParcelType): builder.PrependInt32Slot(6, DreamMakerParcelType, 0)
def MiniGameDreamInfoExcelAddDreamMakerParcelType(builder, DreamMakerParcelType):
    """This method is deprecated. Please switch to AddDreamMakerParcelType."""
    return AddDreamMakerParcelType(builder, DreamMakerParcelType)
def AddDreamMakerParcelId(builder, DreamMakerParcelId): builder.PrependInt64Slot(7, DreamMakerParcelId, 0)
def MiniGameDreamInfoExcelAddDreamMakerParcelId(builder, DreamMakerParcelId):
    """This method is deprecated. Please switch to AddDreamMakerParcelId."""
    return AddDreamMakerParcelId(builder, DreamMakerParcelId)
def AddDreamMakerDailyPointParcelType(builder, DreamMakerDailyPointParcelType): builder.PrependInt32Slot(8, DreamMakerDailyPointParcelType, 0)
def MiniGameDreamInfoExcelAddDreamMakerDailyPointParcelType(builder, DreamMakerDailyPointParcelType):
    """This method is deprecated. Please switch to AddDreamMakerDailyPointParcelType."""
    return AddDreamMakerDailyPointParcelType(builder, DreamMakerDailyPointParcelType)
def AddDreamMakerDailyPointId(builder, DreamMakerDailyPointId): builder.PrependInt64Slot(9, DreamMakerDailyPointId, 0)
def MiniGameDreamInfoExcelAddDreamMakerDailyPointId(builder, DreamMakerDailyPointId):
    """This method is deprecated. Please switch to AddDreamMakerDailyPointId."""
    return AddDreamMakerDailyPointId(builder, DreamMakerDailyPointId)
def AddDreamMakerParameterTransfer(builder, DreamMakerParameterTransfer): builder.PrependInt64Slot(10, DreamMakerParameterTransfer, 0)
def MiniGameDreamInfoExcelAddDreamMakerParameterTransfer(builder, DreamMakerParameterTransfer):
    """This method is deprecated. Please switch to AddDreamMakerParameterTransfer."""
    return AddDreamMakerParameterTransfer(builder, DreamMakerParameterTransfer)
def AddScheduleCostGoodsId(builder, ScheduleCostGoodsId): builder.PrependInt64Slot(11, ScheduleCostGoodsId, 0)
def MiniGameDreamInfoExcelAddScheduleCostGoodsId(builder, ScheduleCostGoodsId):
    """This method is deprecated. Please switch to AddScheduleCostGoodsId."""
    return AddScheduleCostGoodsId(builder, ScheduleCostGoodsId)
def AddLobbyBGMChangeScenarioId(builder, LobbyBGMChangeScenarioId): builder.PrependInt64Slot(12, LobbyBGMChangeScenarioId, 0)
def MiniGameDreamInfoExcelAddLobbyBGMChangeScenarioId(builder, LobbyBGMChangeScenarioId):
    """This method is deprecated. Please switch to AddLobbyBGMChangeScenarioId."""
    return AddLobbyBGMChangeScenarioId(builder, LobbyBGMChangeScenarioId)
def End(builder): return builder.EndObject()
def MiniGameDreamInfoExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)