# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameShootingCharacterExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameShootingCharacterExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMiniGameShootingCharacterExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MiniGameShootingCharacterExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MiniGameShootingCharacterExcel
    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def SpineResourceName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MiniGameShootingCharacterExcel
    def BodyRadius(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MiniGameShootingCharacterExcel
    def ModelPrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MiniGameShootingCharacterExcel
    def NormalAttackSkillData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MiniGameShootingCharacterExcel
    def PublicSkillData(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # MiniGameShootingCharacterExcel
    def PublicSkillDataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MiniGameShootingCharacterExcel
    def PublicSkillDataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # MiniGameShootingCharacterExcel
    def DeathSkillData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MiniGameShootingCharacterExcel
    def MaxHP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def AttackPower(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def DefensePower(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def CriticalRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def CriticalDamageRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def AttackRange(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def MoveSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def ShotTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def IsBoss(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # MiniGameShootingCharacterExcel
    def Scale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MiniGameShootingCharacterExcel
    def IgnoreObstacleCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # MiniGameShootingCharacterExcel
    def CharacterVoiceGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(19)
def MiniGameShootingCharacterExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddUniqueId(builder, UniqueId): builder.PrependInt64Slot(0, UniqueId, 0)
def MiniGameShootingCharacterExcelAddUniqueId(builder, UniqueId):
    """This method is deprecated. Please switch to AddUniqueId."""
    return AddUniqueId(builder, UniqueId)
def AddSpineResourceName(builder, SpineResourceName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(SpineResourceName), 0)
def MiniGameShootingCharacterExcelAddSpineResourceName(builder, SpineResourceName):
    """This method is deprecated. Please switch to AddSpineResourceName."""
    return AddSpineResourceName(builder, SpineResourceName)
def AddBodyRadius(builder, BodyRadius): builder.PrependFloat32Slot(2, BodyRadius, 0.0)
def MiniGameShootingCharacterExcelAddBodyRadius(builder, BodyRadius):
    """This method is deprecated. Please switch to AddBodyRadius."""
    return AddBodyRadius(builder, BodyRadius)
def AddModelPrefabName(builder, ModelPrefabName): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(ModelPrefabName), 0)
def MiniGameShootingCharacterExcelAddModelPrefabName(builder, ModelPrefabName):
    """This method is deprecated. Please switch to AddModelPrefabName."""
    return AddModelPrefabName(builder, ModelPrefabName)
def AddNormalAttackSkillData(builder, NormalAttackSkillData): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(NormalAttackSkillData), 0)
def MiniGameShootingCharacterExcelAddNormalAttackSkillData(builder, NormalAttackSkillData):
    """This method is deprecated. Please switch to AddNormalAttackSkillData."""
    return AddNormalAttackSkillData(builder, NormalAttackSkillData)
def AddPublicSkillData(builder, PublicSkillData): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(PublicSkillData), 0)
def MiniGameShootingCharacterExcelAddPublicSkillData(builder, PublicSkillData):
    """This method is deprecated. Please switch to AddPublicSkillData."""
    return AddPublicSkillData(builder, PublicSkillData)
def StartPublicSkillDataVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MiniGameShootingCharacterExcelStartPublicSkillDataVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartPublicSkillDataVector(builder, numElems)
def AddDeathSkillData(builder, DeathSkillData): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(DeathSkillData), 0)
def MiniGameShootingCharacterExcelAddDeathSkillData(builder, DeathSkillData):
    """This method is deprecated. Please switch to AddDeathSkillData."""
    return AddDeathSkillData(builder, DeathSkillData)
def AddMaxHP(builder, MaxHP): builder.PrependInt64Slot(7, MaxHP, 0)
def MiniGameShootingCharacterExcelAddMaxHP(builder, MaxHP):
    """This method is deprecated. Please switch to AddMaxHP."""
    return AddMaxHP(builder, MaxHP)
def AddAttackPower(builder, AttackPower): builder.PrependInt64Slot(8, AttackPower, 0)
def MiniGameShootingCharacterExcelAddAttackPower(builder, AttackPower):
    """This method is deprecated. Please switch to AddAttackPower."""
    return AddAttackPower(builder, AttackPower)
def AddDefensePower(builder, DefensePower): builder.PrependInt64Slot(9, DefensePower, 0)
def MiniGameShootingCharacterExcelAddDefensePower(builder, DefensePower):
    """This method is deprecated. Please switch to AddDefensePower."""
    return AddDefensePower(builder, DefensePower)
def AddCriticalRate(builder, CriticalRate): builder.PrependInt64Slot(10, CriticalRate, 0)
def MiniGameShootingCharacterExcelAddCriticalRate(builder, CriticalRate):
    """This method is deprecated. Please switch to AddCriticalRate."""
    return AddCriticalRate(builder, CriticalRate)
def AddCriticalDamageRate(builder, CriticalDamageRate): builder.PrependInt64Slot(11, CriticalDamageRate, 0)
def MiniGameShootingCharacterExcelAddCriticalDamageRate(builder, CriticalDamageRate):
    """This method is deprecated. Please switch to AddCriticalDamageRate."""
    return AddCriticalDamageRate(builder, CriticalDamageRate)
def AddAttackRange(builder, AttackRange): builder.PrependInt64Slot(12, AttackRange, 0)
def MiniGameShootingCharacterExcelAddAttackRange(builder, AttackRange):
    """This method is deprecated. Please switch to AddAttackRange."""
    return AddAttackRange(builder, AttackRange)
def AddMoveSpeed(builder, MoveSpeed): builder.PrependInt64Slot(13, MoveSpeed, 0)
def MiniGameShootingCharacterExcelAddMoveSpeed(builder, MoveSpeed):
    """This method is deprecated. Please switch to AddMoveSpeed."""
    return AddMoveSpeed(builder, MoveSpeed)
def AddShotTime(builder, ShotTime): builder.PrependInt64Slot(14, ShotTime, 0)
def MiniGameShootingCharacterExcelAddShotTime(builder, ShotTime):
    """This method is deprecated. Please switch to AddShotTime."""
    return AddShotTime(builder, ShotTime)
def AddIsBoss(builder, IsBoss): builder.PrependBoolSlot(15, IsBoss, 0)
def MiniGameShootingCharacterExcelAddIsBoss(builder, IsBoss):
    """This method is deprecated. Please switch to AddIsBoss."""
    return AddIsBoss(builder, IsBoss)
def AddScale(builder, Scale): builder.PrependFloat32Slot(16, Scale, 0.0)
def MiniGameShootingCharacterExcelAddScale(builder, Scale):
    """This method is deprecated. Please switch to AddScale."""
    return AddScale(builder, Scale)
def AddIgnoreObstacleCheck(builder, IgnoreObstacleCheck): builder.PrependBoolSlot(17, IgnoreObstacleCheck, 0)
def MiniGameShootingCharacterExcelAddIgnoreObstacleCheck(builder, IgnoreObstacleCheck):
    """This method is deprecated. Please switch to AddIgnoreObstacleCheck."""
    return AddIgnoreObstacleCheck(builder, IgnoreObstacleCheck)
def AddCharacterVoiceGroupId(builder, CharacterVoiceGroupId): builder.PrependInt64Slot(18, CharacterVoiceGroupId, 0)
def MiniGameShootingCharacterExcelAddCharacterVoiceGroupId(builder, CharacterVoiceGroupId):
    """This method is deprecated. Please switch to AddCharacterVoiceGroupId."""
    return AddCharacterVoiceGroupId(builder, CharacterVoiceGroupId)
def End(builder): return builder.EndObject()
def MiniGameShootingCharacterExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)