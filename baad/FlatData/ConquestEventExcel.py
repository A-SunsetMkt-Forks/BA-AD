# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestEventExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestEventExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsConquestEventExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ConquestEventExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConquestEventExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConquestEventExcel
    def MainStoryEventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConquestEventExcel
    def ConquestEventType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestEventExcel
    def UseErosion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ConquestEventExcel
    def UseUnexpectedEvent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ConquestEventExcel
    def UseCalculate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ConquestEventExcel
    def UseConquestObject(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ConquestEventExcel
    def EvnetMapGoalLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConquestEventExcel
    def EvnetMapNameLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConquestEventExcel
    def MapEnterScenarioGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConquestEventExcel
    def EvnetScenarioBG(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConquestEventExcel
    def ManageUnitChange(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestEventExcel
    def AssistCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestEventExcel
    def PlayTimeLimitInSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestEventExcel
    def AnimationUnitAmountMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestEventExcel
    def AnimationUnitAmountMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestEventExcel
    def AnimationUnitDelay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConquestEventExcel
    def LocalizeUnexpected(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConquestEventExcel
    def LocalizeErosions(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConquestEventExcel
    def LocalizeStep(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConquestEventExcel
    def LocalizeTile(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConquestEventExcel
    def LocalizeMapInfo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConquestEventExcel
    def LocalizeManage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConquestEventExcel
    def LocalizeUpgrade(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConquestEventExcel
    def LocalizeTreasureBox(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConquestEventExcel
    def IndividualErosionDailyCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(26)
def ConquestEventExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)
def ConquestEventExcelAddEventContentId(builder, EventContentId):
    """This method is deprecated. Please switch to AddEventContentId."""
    return AddEventContentId(builder, EventContentId)
def AddMainStoryEventContentId(builder, MainStoryEventContentId): builder.PrependInt64Slot(1, MainStoryEventContentId, 0)
def ConquestEventExcelAddMainStoryEventContentId(builder, MainStoryEventContentId):
    """This method is deprecated. Please switch to AddMainStoryEventContentId."""
    return AddMainStoryEventContentId(builder, MainStoryEventContentId)
def AddConquestEventType_(builder, ConquestEventType_): builder.PrependInt32Slot(2, ConquestEventType_, 0)
def ConquestEventExcelAddConquestEventType_(builder, ConquestEventType_):
    """This method is deprecated. Please switch to AddConquestEventType_."""
    return AddConquestEventType_(builder, ConquestEventType_)
def AddUseErosion(builder, UseErosion): builder.PrependBoolSlot(3, UseErosion, 0)
def ConquestEventExcelAddUseErosion(builder, UseErosion):
    """This method is deprecated. Please switch to AddUseErosion."""
    return AddUseErosion(builder, UseErosion)
def AddUseUnexpectedEvent(builder, UseUnexpectedEvent): builder.PrependBoolSlot(4, UseUnexpectedEvent, 0)
def ConquestEventExcelAddUseUnexpectedEvent(builder, UseUnexpectedEvent):
    """This method is deprecated. Please switch to AddUseUnexpectedEvent."""
    return AddUseUnexpectedEvent(builder, UseUnexpectedEvent)
def AddUseCalculate(builder, UseCalculate): builder.PrependBoolSlot(5, UseCalculate, 0)
def ConquestEventExcelAddUseCalculate(builder, UseCalculate):
    """This method is deprecated. Please switch to AddUseCalculate."""
    return AddUseCalculate(builder, UseCalculate)
def AddUseConquestObject(builder, UseConquestObject): builder.PrependBoolSlot(6, UseConquestObject, 0)
def ConquestEventExcelAddUseConquestObject(builder, UseConquestObject):
    """This method is deprecated. Please switch to AddUseConquestObject."""
    return AddUseConquestObject(builder, UseConquestObject)
def AddEvnetMapGoalLocalize(builder, EvnetMapGoalLocalize): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(EvnetMapGoalLocalize), 0)
def ConquestEventExcelAddEvnetMapGoalLocalize(builder, EvnetMapGoalLocalize):
    """This method is deprecated. Please switch to AddEvnetMapGoalLocalize."""
    return AddEvnetMapGoalLocalize(builder, EvnetMapGoalLocalize)
def AddEvnetMapNameLocalize(builder, EvnetMapNameLocalize): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(EvnetMapNameLocalize), 0)
def ConquestEventExcelAddEvnetMapNameLocalize(builder, EvnetMapNameLocalize):
    """This method is deprecated. Please switch to AddEvnetMapNameLocalize."""
    return AddEvnetMapNameLocalize(builder, EvnetMapNameLocalize)
def AddMapEnterScenarioGroupId(builder, MapEnterScenarioGroupId): builder.PrependInt64Slot(9, MapEnterScenarioGroupId, 0)
def ConquestEventExcelAddMapEnterScenarioGroupId(builder, MapEnterScenarioGroupId):
    """This method is deprecated. Please switch to AddMapEnterScenarioGroupId."""
    return AddMapEnterScenarioGroupId(builder, MapEnterScenarioGroupId)
def AddEvnetScenarioBG(builder, EvnetScenarioBG): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(EvnetScenarioBG), 0)
def ConquestEventExcelAddEvnetScenarioBG(builder, EvnetScenarioBG):
    """This method is deprecated. Please switch to AddEvnetScenarioBG."""
    return AddEvnetScenarioBG(builder, EvnetScenarioBG)
def AddManageUnitChange(builder, ManageUnitChange): builder.PrependInt32Slot(11, ManageUnitChange, 0)
def ConquestEventExcelAddManageUnitChange(builder, ManageUnitChange):
    """This method is deprecated. Please switch to AddManageUnitChange."""
    return AddManageUnitChange(builder, ManageUnitChange)
def AddAssistCount(builder, AssistCount): builder.PrependInt32Slot(12, AssistCount, 0)
def ConquestEventExcelAddAssistCount(builder, AssistCount):
    """This method is deprecated. Please switch to AddAssistCount."""
    return AddAssistCount(builder, AssistCount)
def AddPlayTimeLimitInSeconds(builder, PlayTimeLimitInSeconds): builder.PrependInt32Slot(13, PlayTimeLimitInSeconds, 0)
def ConquestEventExcelAddPlayTimeLimitInSeconds(builder, PlayTimeLimitInSeconds):
    """This method is deprecated. Please switch to AddPlayTimeLimitInSeconds."""
    return AddPlayTimeLimitInSeconds(builder, PlayTimeLimitInSeconds)
def AddAnimationUnitAmountMin(builder, AnimationUnitAmountMin): builder.PrependInt32Slot(14, AnimationUnitAmountMin, 0)
def ConquestEventExcelAddAnimationUnitAmountMin(builder, AnimationUnitAmountMin):
    """This method is deprecated. Please switch to AddAnimationUnitAmountMin."""
    return AddAnimationUnitAmountMin(builder, AnimationUnitAmountMin)
def AddAnimationUnitAmountMax(builder, AnimationUnitAmountMax): builder.PrependInt32Slot(15, AnimationUnitAmountMax, 0)
def ConquestEventExcelAddAnimationUnitAmountMax(builder, AnimationUnitAmountMax):
    """This method is deprecated. Please switch to AddAnimationUnitAmountMax."""
    return AddAnimationUnitAmountMax(builder, AnimationUnitAmountMax)
def AddAnimationUnitDelay(builder, AnimationUnitDelay): builder.PrependFloat32Slot(16, AnimationUnitDelay, 0.0)
def ConquestEventExcelAddAnimationUnitDelay(builder, AnimationUnitDelay):
    """This method is deprecated. Please switch to AddAnimationUnitDelay."""
    return AddAnimationUnitDelay(builder, AnimationUnitDelay)
def AddLocalizeUnexpected(builder, LocalizeUnexpected): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeUnexpected), 0)
def ConquestEventExcelAddLocalizeUnexpected(builder, LocalizeUnexpected):
    """This method is deprecated. Please switch to AddLocalizeUnexpected."""
    return AddLocalizeUnexpected(builder, LocalizeUnexpected)
def AddLocalizeErosions(builder, LocalizeErosions): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeErosions), 0)
def ConquestEventExcelAddLocalizeErosions(builder, LocalizeErosions):
    """This method is deprecated. Please switch to AddLocalizeErosions."""
    return AddLocalizeErosions(builder, LocalizeErosions)
def AddLocalizeStep(builder, LocalizeStep): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeStep), 0)
def ConquestEventExcelAddLocalizeStep(builder, LocalizeStep):
    """This method is deprecated. Please switch to AddLocalizeStep."""
    return AddLocalizeStep(builder, LocalizeStep)
def AddLocalizeTile(builder, LocalizeTile): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeTile), 0)
def ConquestEventExcelAddLocalizeTile(builder, LocalizeTile):
    """This method is deprecated. Please switch to AddLocalizeTile."""
    return AddLocalizeTile(builder, LocalizeTile)
def AddLocalizeMapInfo(builder, LocalizeMapInfo): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeMapInfo), 0)
def ConquestEventExcelAddLocalizeMapInfo(builder, LocalizeMapInfo):
    """This method is deprecated. Please switch to AddLocalizeMapInfo."""
    return AddLocalizeMapInfo(builder, LocalizeMapInfo)
def AddLocalizeManage(builder, LocalizeManage): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeManage), 0)
def ConquestEventExcelAddLocalizeManage(builder, LocalizeManage):
    """This method is deprecated. Please switch to AddLocalizeManage."""
    return AddLocalizeManage(builder, LocalizeManage)
def AddLocalizeUpgrade(builder, LocalizeUpgrade): builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeUpgrade), 0)
def ConquestEventExcelAddLocalizeUpgrade(builder, LocalizeUpgrade):
    """This method is deprecated. Please switch to AddLocalizeUpgrade."""
    return AddLocalizeUpgrade(builder, LocalizeUpgrade)
def AddLocalizeTreasureBox(builder, LocalizeTreasureBox): builder.PrependUOffsetTRelativeSlot(24, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeTreasureBox), 0)
def ConquestEventExcelAddLocalizeTreasureBox(builder, LocalizeTreasureBox):
    """This method is deprecated. Please switch to AddLocalizeTreasureBox."""
    return AddLocalizeTreasureBox(builder, LocalizeTreasureBox)
def AddIndividualErosionDailyCount(builder, IndividualErosionDailyCount): builder.PrependInt64Slot(25, IndividualErosionDailyCount, 0)
def ConquestEventExcelAddIndividualErosionDailyCount(builder, IndividualErosionDailyCount):
    """This method is deprecated. Please switch to AddIndividualErosionDailyCount."""
    return AddIndividualErosionDailyCount(builder, IndividualErosionDailyCount)
def End(builder): return builder.EndObject()
def ConquestEventExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)