# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ContentsFeverExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ContentsFeverExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsContentsFeverExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ContentsFeverExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ContentsFeverExcel
    def ConditionContent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ContentsFeverExcel
    def SkillFeverCheckCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ContentsFeverExcel
    def SkillCostFever(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ContentsFeverExcel
    def FeverStartTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ContentsFeverExcel
    def FeverDurationTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(5)
def ContentsFeverExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddConditionContent(builder, ConditionContent): builder.PrependInt32Slot(0, ConditionContent, 0)
def ContentsFeverExcelAddConditionContent(builder, ConditionContent):
    """This method is deprecated. Please switch to AddConditionContent."""
    return AddConditionContent(builder, ConditionContent)
def AddSkillFeverCheckCondition(builder, SkillFeverCheckCondition): builder.PrependInt32Slot(1, SkillFeverCheckCondition, 0)
def ContentsFeverExcelAddSkillFeverCheckCondition(builder, SkillFeverCheckCondition):
    """This method is deprecated. Please switch to AddSkillFeverCheckCondition."""
    return AddSkillFeverCheckCondition(builder, SkillFeverCheckCondition)
def AddSkillCostFever(builder, SkillCostFever): builder.PrependInt64Slot(2, SkillCostFever, 0)
def ContentsFeverExcelAddSkillCostFever(builder, SkillCostFever):
    """This method is deprecated. Please switch to AddSkillCostFever."""
    return AddSkillCostFever(builder, SkillCostFever)
def AddFeverStartTime(builder, FeverStartTime): builder.PrependInt64Slot(3, FeverStartTime, 0)
def ContentsFeverExcelAddFeverStartTime(builder, FeverStartTime):
    """This method is deprecated. Please switch to AddFeverStartTime."""
    return AddFeverStartTime(builder, FeverStartTime)
def AddFeverDurationTime(builder, FeverDurationTime): builder.PrependInt64Slot(4, FeverDurationTime, 0)
def ContentsFeverExcelAddFeverDurationTime(builder, FeverDurationTime):
    """This method is deprecated. Please switch to AddFeverDurationTime."""
    return AddFeverDurationTime(builder, FeverDurationTime)
def End(builder): return builder.EndObject()
def ContentsFeverExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)