# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EventContentMissionExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventContentMissionExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEventContentMissionExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # EventContentMissionExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EventContentMissionExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentMissionExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentMissionExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentMissionExcel
    def GroupName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EventContentMissionExcel
    def Category(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EventContentMissionExcel
    def Description(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # EventContentMissionExcel
    def ResetType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EventContentMissionExcel
    def ToastDisplayType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EventContentMissionExcel
    def ToastImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EventContentMissionExcel
    def ViewFlag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # EventContentMissionExcel
    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentMissionExcel
    def PreMissionId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # EventContentMissionExcel
    def PreMissionIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # EventContentMissionExcel
    def PreMissionIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentMissionExcel
    def PreMissionIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0

    # EventContentMissionExcel
    def AccountType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EventContentMissionExcel
    def AccountLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentMissionExcel
    def ShortcutUI(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # EventContentMissionExcel
    def ShortcutUILength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentMissionExcel
    def ShortcutUIIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        return o == 0

    # EventContentMissionExcel
    def ChallengeStageShortcut(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentMissionExcel
    def CompleteConditionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EventContentMissionExcel
    def IsCompleteExtensionTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # EventContentMissionExcel
    def CompleteConditionCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentMissionExcel
    def CompleteConditionParameter(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # EventContentMissionExcel
    def CompleteConditionParameterAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # EventContentMissionExcel
    def CompleteConditionParameterLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentMissionExcel
    def CompleteConditionParameterIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        return o == 0

    # EventContentMissionExcel
    def CompleteConditionParameterTag(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # EventContentMissionExcel
    def CompleteConditionParameterTagAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # EventContentMissionExcel
    def CompleteConditionParameterTagLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentMissionExcel
    def CompleteConditionParameterTagIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        return o == 0

    # EventContentMissionExcel
    def RewardIcon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EventContentMissionExcel
    def CompleteConditionMissionId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # EventContentMissionExcel
    def CompleteConditionMissionIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # EventContentMissionExcel
    def CompleteConditionMissionIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentMissionExcel
    def CompleteConditionMissionIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        return o == 0

    # EventContentMissionExcel
    def CompleteConditionMissionCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentMissionExcel
    def MissionRewardParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # EventContentMissionExcel
    def MissionRewardParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # EventContentMissionExcel
    def MissionRewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentMissionExcel
    def MissionRewardParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        return o == 0

    # EventContentMissionExcel
    def MissionRewardParcelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # EventContentMissionExcel
    def MissionRewardParcelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # EventContentMissionExcel
    def MissionRewardParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentMissionExcel
    def MissionRewardParcelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        return o == 0

    # EventContentMissionExcel
    def MissionRewardAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # EventContentMissionExcel
    def MissionRewardAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # EventContentMissionExcel
    def MissionRewardAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentMissionExcel
    def MissionRewardAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        return o == 0

    # EventContentMissionExcel
    def ConditionRewardParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # EventContentMissionExcel
    def ConditionRewardParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # EventContentMissionExcel
    def ConditionRewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentMissionExcel
    def ConditionRewardParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        return o == 0

    # EventContentMissionExcel
    def ConditionRewardParcelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # EventContentMissionExcel
    def ConditionRewardParcelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # EventContentMissionExcel
    def ConditionRewardParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentMissionExcel
    def ConditionRewardParcelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        return o == 0

    # EventContentMissionExcel
    def ConditionRewardAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # EventContentMissionExcel
    def ConditionRewardAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # EventContentMissionExcel
    def ConditionRewardAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentMissionExcel
    def ConditionRewardAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        return o == 0

def Start(builder): builder.StartObject(30)
def EventContentMissionExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def EventContentMissionExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(1, EventContentId, 0)
def EventContentMissionExcelAddEventContentId(builder, EventContentId):
    """This method is deprecated. Please switch to AddEventContentId."""
    return AddEventContentId(builder, EventContentId)
def AddGroupId(builder, GroupId): builder.PrependInt64Slot(2, GroupId, 0)
def EventContentMissionExcelAddGroupId(builder, GroupId):
    """This method is deprecated. Please switch to AddGroupId."""
    return AddGroupId(builder, GroupId)
def AddGroupName(builder, GroupName): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(GroupName), 0)
def EventContentMissionExcelAddGroupName(builder, GroupName):
    """This method is deprecated. Please switch to AddGroupName."""
    return AddGroupName(builder, GroupName)
def AddCategory(builder, Category): builder.PrependInt32Slot(4, Category, 0)
def EventContentMissionExcelAddCategory(builder, Category):
    """This method is deprecated. Please switch to AddCategory."""
    return AddCategory(builder, Category)
def AddDescription(builder, Description): builder.PrependUint32Slot(5, Description, 0)
def EventContentMissionExcelAddDescription(builder, Description):
    """This method is deprecated. Please switch to AddDescription."""
    return AddDescription(builder, Description)
def AddResetType(builder, ResetType): builder.PrependInt32Slot(6, ResetType, 0)
def EventContentMissionExcelAddResetType(builder, ResetType):
    """This method is deprecated. Please switch to AddResetType."""
    return AddResetType(builder, ResetType)
def AddToastDisplayType(builder, ToastDisplayType): builder.PrependInt32Slot(7, ToastDisplayType, 0)
def EventContentMissionExcelAddToastDisplayType(builder, ToastDisplayType):
    """This method is deprecated. Please switch to AddToastDisplayType."""
    return AddToastDisplayType(builder, ToastDisplayType)
def AddToastImagePath(builder, ToastImagePath): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(ToastImagePath), 0)
def EventContentMissionExcelAddToastImagePath(builder, ToastImagePath):
    """This method is deprecated. Please switch to AddToastImagePath."""
    return AddToastImagePath(builder, ToastImagePath)
def AddViewFlag(builder, ViewFlag): builder.PrependBoolSlot(9, ViewFlag, 0)
def EventContentMissionExcelAddViewFlag(builder, ViewFlag):
    """This method is deprecated. Please switch to AddViewFlag."""
    return AddViewFlag(builder, ViewFlag)
def AddDisplayOrder(builder, DisplayOrder): builder.PrependInt64Slot(10, DisplayOrder, 0)
def EventContentMissionExcelAddDisplayOrder(builder, DisplayOrder):
    """This method is deprecated. Please switch to AddDisplayOrder."""
    return AddDisplayOrder(builder, DisplayOrder)
def AddPreMissionId(builder, PreMissionId): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(PreMissionId), 0)
def EventContentMissionExcelAddPreMissionId(builder, PreMissionId):
    """This method is deprecated. Please switch to AddPreMissionId."""
    return AddPreMissionId(builder, PreMissionId)
def StartPreMissionIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def EventContentMissionExcelStartPreMissionIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartPreMissionIdVector(builder, numElems)
def AddAccountType(builder, AccountType): builder.PrependInt32Slot(12, AccountType, 0)
def EventContentMissionExcelAddAccountType(builder, AccountType):
    """This method is deprecated. Please switch to AddAccountType."""
    return AddAccountType(builder, AccountType)
def AddAccountLevel(builder, AccountLevel): builder.PrependInt64Slot(13, AccountLevel, 0)
def EventContentMissionExcelAddAccountLevel(builder, AccountLevel):
    """This method is deprecated. Please switch to AddAccountLevel."""
    return AddAccountLevel(builder, AccountLevel)
def AddShortcutUI(builder, ShortcutUI): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(ShortcutUI), 0)
def EventContentMissionExcelAddShortcutUI(builder, ShortcutUI):
    """This method is deprecated. Please switch to AddShortcutUI."""
    return AddShortcutUI(builder, ShortcutUI)
def StartShortcutUIVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EventContentMissionExcelStartShortcutUIVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartShortcutUIVector(builder, numElems)
def AddChallengeStageShortcut(builder, ChallengeStageShortcut): builder.PrependInt64Slot(15, ChallengeStageShortcut, 0)
def EventContentMissionExcelAddChallengeStageShortcut(builder, ChallengeStageShortcut):
    """This method is deprecated. Please switch to AddChallengeStageShortcut."""
    return AddChallengeStageShortcut(builder, ChallengeStageShortcut)
def AddCompleteConditionType(builder, CompleteConditionType): builder.PrependInt32Slot(16, CompleteConditionType, 0)
def EventContentMissionExcelAddCompleteConditionType(builder, CompleteConditionType):
    """This method is deprecated. Please switch to AddCompleteConditionType."""
    return AddCompleteConditionType(builder, CompleteConditionType)
def AddIsCompleteExtensionTime(builder, IsCompleteExtensionTime): builder.PrependBoolSlot(17, IsCompleteExtensionTime, 0)
def EventContentMissionExcelAddIsCompleteExtensionTime(builder, IsCompleteExtensionTime):
    """This method is deprecated. Please switch to AddIsCompleteExtensionTime."""
    return AddIsCompleteExtensionTime(builder, IsCompleteExtensionTime)
def AddCompleteConditionCount(builder, CompleteConditionCount): builder.PrependInt64Slot(18, CompleteConditionCount, 0)
def EventContentMissionExcelAddCompleteConditionCount(builder, CompleteConditionCount):
    """This method is deprecated. Please switch to AddCompleteConditionCount."""
    return AddCompleteConditionCount(builder, CompleteConditionCount)
def AddCompleteConditionParameter(builder, CompleteConditionParameter): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(CompleteConditionParameter), 0)
def EventContentMissionExcelAddCompleteConditionParameter(builder, CompleteConditionParameter):
    """This method is deprecated. Please switch to AddCompleteConditionParameter."""
    return AddCompleteConditionParameter(builder, CompleteConditionParameter)
def StartCompleteConditionParameterVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def EventContentMissionExcelStartCompleteConditionParameterVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartCompleteConditionParameterVector(builder, numElems)
def AddCompleteConditionParameterTag(builder, CompleteConditionParameterTag): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(CompleteConditionParameterTag), 0)
def EventContentMissionExcelAddCompleteConditionParameterTag(builder, CompleteConditionParameterTag):
    """This method is deprecated. Please switch to AddCompleteConditionParameterTag."""
    return AddCompleteConditionParameterTag(builder, CompleteConditionParameterTag)
def StartCompleteConditionParameterTagVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EventContentMissionExcelStartCompleteConditionParameterTagVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartCompleteConditionParameterTagVector(builder, numElems)
def AddRewardIcon(builder, RewardIcon): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(RewardIcon), 0)
def EventContentMissionExcelAddRewardIcon(builder, RewardIcon):
    """This method is deprecated. Please switch to AddRewardIcon."""
    return AddRewardIcon(builder, RewardIcon)
def AddCompleteConditionMissionId(builder, CompleteConditionMissionId): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(CompleteConditionMissionId), 0)
def EventContentMissionExcelAddCompleteConditionMissionId(builder, CompleteConditionMissionId):
    """This method is deprecated. Please switch to AddCompleteConditionMissionId."""
    return AddCompleteConditionMissionId(builder, CompleteConditionMissionId)
def StartCompleteConditionMissionIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def EventContentMissionExcelStartCompleteConditionMissionIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartCompleteConditionMissionIdVector(builder, numElems)
def AddCompleteConditionMissionCount(builder, CompleteConditionMissionCount): builder.PrependInt64Slot(23, CompleteConditionMissionCount, 0)
def EventContentMissionExcelAddCompleteConditionMissionCount(builder, CompleteConditionMissionCount):
    """This method is deprecated. Please switch to AddCompleteConditionMissionCount."""
    return AddCompleteConditionMissionCount(builder, CompleteConditionMissionCount)
def AddMissionRewardParcelType(builder, MissionRewardParcelType): builder.PrependUOffsetTRelativeSlot(24, flatbuffers.number_types.UOffsetTFlags.py_type(MissionRewardParcelType), 0)
def EventContentMissionExcelAddMissionRewardParcelType(builder, MissionRewardParcelType):
    """This method is deprecated. Please switch to AddMissionRewardParcelType."""
    return AddMissionRewardParcelType(builder, MissionRewardParcelType)
def StartMissionRewardParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EventContentMissionExcelStartMissionRewardParcelTypeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartMissionRewardParcelTypeVector(builder, numElems)
def AddMissionRewardParcelId(builder, MissionRewardParcelId): builder.PrependUOffsetTRelativeSlot(25, flatbuffers.number_types.UOffsetTFlags.py_type(MissionRewardParcelId), 0)
def EventContentMissionExcelAddMissionRewardParcelId(builder, MissionRewardParcelId):
    """This method is deprecated. Please switch to AddMissionRewardParcelId."""
    return AddMissionRewardParcelId(builder, MissionRewardParcelId)
def StartMissionRewardParcelIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def EventContentMissionExcelStartMissionRewardParcelIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartMissionRewardParcelIdVector(builder, numElems)
def AddMissionRewardAmount(builder, MissionRewardAmount): builder.PrependUOffsetTRelativeSlot(26, flatbuffers.number_types.UOffsetTFlags.py_type(MissionRewardAmount), 0)
def EventContentMissionExcelAddMissionRewardAmount(builder, MissionRewardAmount):
    """This method is deprecated. Please switch to AddMissionRewardAmount."""
    return AddMissionRewardAmount(builder, MissionRewardAmount)
def StartMissionRewardAmountVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EventContentMissionExcelStartMissionRewardAmountVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartMissionRewardAmountVector(builder, numElems)
def AddConditionRewardParcelType(builder, ConditionRewardParcelType): builder.PrependUOffsetTRelativeSlot(27, flatbuffers.number_types.UOffsetTFlags.py_type(ConditionRewardParcelType), 0)
def EventContentMissionExcelAddConditionRewardParcelType(builder, ConditionRewardParcelType):
    """This method is deprecated. Please switch to AddConditionRewardParcelType."""
    return AddConditionRewardParcelType(builder, ConditionRewardParcelType)
def StartConditionRewardParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EventContentMissionExcelStartConditionRewardParcelTypeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartConditionRewardParcelTypeVector(builder, numElems)
def AddConditionRewardParcelId(builder, ConditionRewardParcelId): builder.PrependUOffsetTRelativeSlot(28, flatbuffers.number_types.UOffsetTFlags.py_type(ConditionRewardParcelId), 0)
def EventContentMissionExcelAddConditionRewardParcelId(builder, ConditionRewardParcelId):
    """This method is deprecated. Please switch to AddConditionRewardParcelId."""
    return AddConditionRewardParcelId(builder, ConditionRewardParcelId)
def StartConditionRewardParcelIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def EventContentMissionExcelStartConditionRewardParcelIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartConditionRewardParcelIdVector(builder, numElems)
def AddConditionRewardAmount(builder, ConditionRewardAmount): builder.PrependUOffsetTRelativeSlot(29, flatbuffers.number_types.UOffsetTFlags.py_type(ConditionRewardAmount), 0)
def EventContentMissionExcelAddConditionRewardAmount(builder, ConditionRewardAmount):
    """This method is deprecated. Please switch to AddConditionRewardAmount."""
    return AddConditionRewardAmount(builder, ConditionRewardAmount)
def StartConditionRewardAmountVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EventContentMissionExcelStartConditionRewardAmountVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartConditionRewardAmountVector(builder, numElems)
def End(builder): return builder.EndObject()
def EventContentMissionExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)