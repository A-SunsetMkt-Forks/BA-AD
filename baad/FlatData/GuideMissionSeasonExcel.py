# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GuideMissionSeasonExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GuideMissionSeasonExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsGuideMissionSeasonExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # GuideMissionSeasonExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GuideMissionSeasonExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GuideMissionSeasonExcel
    def TitleLocalizeCode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # GuideMissionSeasonExcel
    def PermanentInfomationLocalizeCode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # GuideMissionSeasonExcel
    def InfomationLocalizeCode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # GuideMissionSeasonExcel
    def AccountType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GuideMissionSeasonExcel
    def Enabled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # GuideMissionSeasonExcel
    def BannerOpenDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # GuideMissionSeasonExcel
    def StartDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # GuideMissionSeasonExcel
    def StartableEndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # GuideMissionSeasonExcel
    def EndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # GuideMissionSeasonExcel
    def CloseBannerAfterCompletion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # GuideMissionSeasonExcel
    def MaximumLoginCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GuideMissionSeasonExcel
    def ExpiryDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GuideMissionSeasonExcel
    def SpineCharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GuideMissionSeasonExcel
    def RequirementParcelImage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # GuideMissionSeasonExcel
    def RewardImage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # GuideMissionSeasonExcel
    def LobbyBannerImage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # GuideMissionSeasonExcel
    def BackgroundImage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # GuideMissionSeasonExcel
    def TitleImage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # GuideMissionSeasonExcel
    def RequirementParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GuideMissionSeasonExcel
    def RequirementParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GuideMissionSeasonExcel
    def RequirementParcelAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GuideMissionSeasonExcel
    def TabType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GuideMissionSeasonExcel
    def IsPermanent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # GuideMissionSeasonExcel
    def PreSeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(25)
def GuideMissionSeasonExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def GuideMissionSeasonExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddTitleLocalizeCode(builder, TitleLocalizeCode): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(TitleLocalizeCode), 0)
def GuideMissionSeasonExcelAddTitleLocalizeCode(builder, TitleLocalizeCode):
    """This method is deprecated. Please switch to AddTitleLocalizeCode."""
    return AddTitleLocalizeCode(builder, TitleLocalizeCode)
def AddPermanentInfomationLocalizeCode(builder, PermanentInfomationLocalizeCode): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(PermanentInfomationLocalizeCode), 0)
def GuideMissionSeasonExcelAddPermanentInfomationLocalizeCode(builder, PermanentInfomationLocalizeCode):
    """This method is deprecated. Please switch to AddPermanentInfomationLocalizeCode."""
    return AddPermanentInfomationLocalizeCode(builder, PermanentInfomationLocalizeCode)
def AddInfomationLocalizeCode(builder, InfomationLocalizeCode): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(InfomationLocalizeCode), 0)
def GuideMissionSeasonExcelAddInfomationLocalizeCode(builder, InfomationLocalizeCode):
    """This method is deprecated. Please switch to AddInfomationLocalizeCode."""
    return AddInfomationLocalizeCode(builder, InfomationLocalizeCode)
def AddAccountType(builder, AccountType): builder.PrependInt32Slot(4, AccountType, 0)
def GuideMissionSeasonExcelAddAccountType(builder, AccountType):
    """This method is deprecated. Please switch to AddAccountType."""
    return AddAccountType(builder, AccountType)
def AddEnabled(builder, Enabled): builder.PrependBoolSlot(5, Enabled, 0)
def GuideMissionSeasonExcelAddEnabled(builder, Enabled):
    """This method is deprecated. Please switch to AddEnabled."""
    return AddEnabled(builder, Enabled)
def AddBannerOpenDate(builder, BannerOpenDate): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(BannerOpenDate), 0)
def GuideMissionSeasonExcelAddBannerOpenDate(builder, BannerOpenDate):
    """This method is deprecated. Please switch to AddBannerOpenDate."""
    return AddBannerOpenDate(builder, BannerOpenDate)
def AddStartDate(builder, StartDate): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(StartDate), 0)
def GuideMissionSeasonExcelAddStartDate(builder, StartDate):
    """This method is deprecated. Please switch to AddStartDate."""
    return AddStartDate(builder, StartDate)
def AddStartableEndDate(builder, StartableEndDate): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(StartableEndDate), 0)
def GuideMissionSeasonExcelAddStartableEndDate(builder, StartableEndDate):
    """This method is deprecated. Please switch to AddStartableEndDate."""
    return AddStartableEndDate(builder, StartableEndDate)
def AddEndDate(builder, EndDate): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(EndDate), 0)
def GuideMissionSeasonExcelAddEndDate(builder, EndDate):
    """This method is deprecated. Please switch to AddEndDate."""
    return AddEndDate(builder, EndDate)
def AddCloseBannerAfterCompletion(builder, CloseBannerAfterCompletion): builder.PrependBoolSlot(10, CloseBannerAfterCompletion, 0)
def GuideMissionSeasonExcelAddCloseBannerAfterCompletion(builder, CloseBannerAfterCompletion):
    """This method is deprecated. Please switch to AddCloseBannerAfterCompletion."""
    return AddCloseBannerAfterCompletion(builder, CloseBannerAfterCompletion)
def AddMaximumLoginCount(builder, MaximumLoginCount): builder.PrependInt64Slot(11, MaximumLoginCount, 0)
def GuideMissionSeasonExcelAddMaximumLoginCount(builder, MaximumLoginCount):
    """This method is deprecated. Please switch to AddMaximumLoginCount."""
    return AddMaximumLoginCount(builder, MaximumLoginCount)
def AddExpiryDate(builder, ExpiryDate): builder.PrependInt64Slot(12, ExpiryDate, 0)
def GuideMissionSeasonExcelAddExpiryDate(builder, ExpiryDate):
    """This method is deprecated. Please switch to AddExpiryDate."""
    return AddExpiryDate(builder, ExpiryDate)
def AddSpineCharacterId(builder, SpineCharacterId): builder.PrependInt64Slot(13, SpineCharacterId, 0)
def GuideMissionSeasonExcelAddSpineCharacterId(builder, SpineCharacterId):
    """This method is deprecated. Please switch to AddSpineCharacterId."""
    return AddSpineCharacterId(builder, SpineCharacterId)
def AddRequirementParcelImage(builder, RequirementParcelImage): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(RequirementParcelImage), 0)
def GuideMissionSeasonExcelAddRequirementParcelImage(builder, RequirementParcelImage):
    """This method is deprecated. Please switch to AddRequirementParcelImage."""
    return AddRequirementParcelImage(builder, RequirementParcelImage)
def AddRewardImage(builder, RewardImage): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(RewardImage), 0)
def GuideMissionSeasonExcelAddRewardImage(builder, RewardImage):
    """This method is deprecated. Please switch to AddRewardImage."""
    return AddRewardImage(builder, RewardImage)
def AddLobbyBannerImage(builder, LobbyBannerImage): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(LobbyBannerImage), 0)
def GuideMissionSeasonExcelAddLobbyBannerImage(builder, LobbyBannerImage):
    """This method is deprecated. Please switch to AddLobbyBannerImage."""
    return AddLobbyBannerImage(builder, LobbyBannerImage)
def AddBackgroundImage(builder, BackgroundImage): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(BackgroundImage), 0)
def GuideMissionSeasonExcelAddBackgroundImage(builder, BackgroundImage):
    """This method is deprecated. Please switch to AddBackgroundImage."""
    return AddBackgroundImage(builder, BackgroundImage)
def AddTitleImage(builder, TitleImage): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(TitleImage), 0)
def GuideMissionSeasonExcelAddTitleImage(builder, TitleImage):
    """This method is deprecated. Please switch to AddTitleImage."""
    return AddTitleImage(builder, TitleImage)
def AddRequirementParcelType(builder, RequirementParcelType): builder.PrependInt32Slot(19, RequirementParcelType, 0)
def GuideMissionSeasonExcelAddRequirementParcelType(builder, RequirementParcelType):
    """This method is deprecated. Please switch to AddRequirementParcelType."""
    return AddRequirementParcelType(builder, RequirementParcelType)
def AddRequirementParcelId(builder, RequirementParcelId): builder.PrependInt64Slot(20, RequirementParcelId, 0)
def GuideMissionSeasonExcelAddRequirementParcelId(builder, RequirementParcelId):
    """This method is deprecated. Please switch to AddRequirementParcelId."""
    return AddRequirementParcelId(builder, RequirementParcelId)
def AddRequirementParcelAmount(builder, RequirementParcelAmount): builder.PrependInt32Slot(21, RequirementParcelAmount, 0)
def GuideMissionSeasonExcelAddRequirementParcelAmount(builder, RequirementParcelAmount):
    """This method is deprecated. Please switch to AddRequirementParcelAmount."""
    return AddRequirementParcelAmount(builder, RequirementParcelAmount)
def AddTabType(builder, TabType): builder.PrependInt32Slot(22, TabType, 0)
def GuideMissionSeasonExcelAddTabType(builder, TabType):
    """This method is deprecated. Please switch to AddTabType."""
    return AddTabType(builder, TabType)
def AddIsPermanent(builder, IsPermanent): builder.PrependBoolSlot(23, IsPermanent, 0)
def GuideMissionSeasonExcelAddIsPermanent(builder, IsPermanent):
    """This method is deprecated. Please switch to AddIsPermanent."""
    return AddIsPermanent(builder, IsPermanent)
def AddPreSeasonId(builder, PreSeasonId): builder.PrependInt64Slot(24, PreSeasonId, 0)
def GuideMissionSeasonExcelAddPreSeasonId(builder, PreSeasonId):
    """This method is deprecated. Please switch to AddPreSeasonId."""
    return AddPreSeasonId(builder, PreSeasonId)
def End(builder): return builder.EndObject()
def GuideMissionSeasonExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)