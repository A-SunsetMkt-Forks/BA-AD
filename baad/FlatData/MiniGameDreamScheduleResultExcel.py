# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameDreamScheduleResultExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameDreamScheduleResultExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMiniGameDreamScheduleResultExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MiniGameDreamScheduleResultExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MiniGameDreamScheduleResultExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamScheduleResultExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamScheduleResultExcel
    def DreamMakerResult_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamScheduleResultExcel
    def DreamMakerScheduleGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamScheduleResultExcel
    def Prob(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamScheduleResultExcel
    def RewardParameter(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # MiniGameDreamScheduleResultExcel
    def RewardParameterAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # MiniGameDreamScheduleResultExcel
    def RewardParameterLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MiniGameDreamScheduleResultExcel
    def RewardParameterIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # MiniGameDreamScheduleResultExcel
    def RewardParameterOperationType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # MiniGameDreamScheduleResultExcel
    def RewardParameterOperationTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # MiniGameDreamScheduleResultExcel
    def RewardParameterOperationTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MiniGameDreamScheduleResultExcel
    def RewardParameterOperationTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

    # MiniGameDreamScheduleResultExcel
    def RewardParameterAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # MiniGameDreamScheduleResultExcel
    def RewardParameterAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # MiniGameDreamScheduleResultExcel
    def RewardParameterAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MiniGameDreamScheduleResultExcel
    def RewardParameterAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0

    # MiniGameDreamScheduleResultExcel
    def RewardParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamScheduleResultExcel
    def RewardParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamScheduleResultExcel
    def RewardParcelAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(11)
def MiniGameDreamScheduleResultExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def MiniGameDreamScheduleResultExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(1, EventContentId, 0)
def MiniGameDreamScheduleResultExcelAddEventContentId(builder, EventContentId):
    """This method is deprecated. Please switch to AddEventContentId."""
    return AddEventContentId(builder, EventContentId)
def AddDreamMakerResult_(builder, DreamMakerResult_): builder.PrependInt32Slot(2, DreamMakerResult_, 0)
def MiniGameDreamScheduleResultExcelAddDreamMakerResult_(builder, DreamMakerResult_):
    """This method is deprecated. Please switch to AddDreamMakerResult_."""
    return AddDreamMakerResult_(builder, DreamMakerResult_)
def AddDreamMakerScheduleGroup(builder, DreamMakerScheduleGroup): builder.PrependInt64Slot(3, DreamMakerScheduleGroup, 0)
def MiniGameDreamScheduleResultExcelAddDreamMakerScheduleGroup(builder, DreamMakerScheduleGroup):
    """This method is deprecated. Please switch to AddDreamMakerScheduleGroup."""
    return AddDreamMakerScheduleGroup(builder, DreamMakerScheduleGroup)
def AddProb(builder, Prob): builder.PrependInt32Slot(4, Prob, 0)
def MiniGameDreamScheduleResultExcelAddProb(builder, Prob):
    """This method is deprecated. Please switch to AddProb."""
    return AddProb(builder, Prob)
def AddRewardParameter(builder, RewardParameter): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParameter), 0)
def MiniGameDreamScheduleResultExcelAddRewardParameter(builder, RewardParameter):
    """This method is deprecated. Please switch to AddRewardParameter."""
    return AddRewardParameter(builder, RewardParameter)
def StartRewardParameterVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MiniGameDreamScheduleResultExcelStartRewardParameterVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParameterVector(builder, numElems)
def AddRewardParameterOperationType(builder, RewardParameterOperationType): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParameterOperationType), 0)
def MiniGameDreamScheduleResultExcelAddRewardParameterOperationType(builder, RewardParameterOperationType):
    """This method is deprecated. Please switch to AddRewardParameterOperationType."""
    return AddRewardParameterOperationType(builder, RewardParameterOperationType)
def StartRewardParameterOperationTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MiniGameDreamScheduleResultExcelStartRewardParameterOperationTypeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParameterOperationTypeVector(builder, numElems)
def AddRewardParameterAmount(builder, RewardParameterAmount): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParameterAmount), 0)
def MiniGameDreamScheduleResultExcelAddRewardParameterAmount(builder, RewardParameterAmount):
    """This method is deprecated. Please switch to AddRewardParameterAmount."""
    return AddRewardParameterAmount(builder, RewardParameterAmount)
def StartRewardParameterAmountVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def MiniGameDreamScheduleResultExcelStartRewardParameterAmountVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParameterAmountVector(builder, numElems)
def AddRewardParcelType(builder, RewardParcelType): builder.PrependInt32Slot(8, RewardParcelType, 0)
def MiniGameDreamScheduleResultExcelAddRewardParcelType(builder, RewardParcelType):
    """This method is deprecated. Please switch to AddRewardParcelType."""
    return AddRewardParcelType(builder, RewardParcelType)
def AddRewardParcelId(builder, RewardParcelId): builder.PrependInt64Slot(9, RewardParcelId, 0)
def MiniGameDreamScheduleResultExcelAddRewardParcelId(builder, RewardParcelId):
    """This method is deprecated. Please switch to AddRewardParcelId."""
    return AddRewardParcelId(builder, RewardParcelId)
def AddRewardParcelAmount(builder, RewardParcelAmount): builder.PrependInt64Slot(10, RewardParcelAmount, 0)
def MiniGameDreamScheduleResultExcelAddRewardParcelAmount(builder, RewardParcelAmount):
    """This method is deprecated. Please switch to AddRewardParcelAmount."""
    return AddRewardParcelAmount(builder, RewardParcelAmount)
def End(builder): return builder.EndObject()
def MiniGameDreamScheduleResultExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)