# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FormationLocationExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FormationLocationExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFormationLocationExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # FormationLocationExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FormationLocationExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FormationLocationExcel
    def GroupID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FormationLocationExcel
    def SlotZ(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # FormationLocationExcel
    def SlotZAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # FormationLocationExcel
    def SlotZLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FormationLocationExcel
    def SlotZIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # FormationLocationExcel
    def SlotX(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # FormationLocationExcel
    def SlotXAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # FormationLocationExcel
    def SlotXLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FormationLocationExcel
    def SlotXIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

def Start(builder): builder.StartObject(4)
def FormationLocationExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def FormationLocationExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddGroupID(builder, GroupID): builder.PrependInt64Slot(1, GroupID, 0)
def FormationLocationExcelAddGroupID(builder, GroupID):
    """This method is deprecated. Please switch to AddGroupID."""
    return AddGroupID(builder, GroupID)
def AddSlotZ(builder, SlotZ): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(SlotZ), 0)
def FormationLocationExcelAddSlotZ(builder, SlotZ):
    """This method is deprecated. Please switch to AddSlotZ."""
    return AddSlotZ(builder, SlotZ)
def StartSlotZVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def FormationLocationExcelStartSlotZVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartSlotZVector(builder, numElems)
def AddSlotX(builder, SlotX): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(SlotX), 0)
def FormationLocationExcelAddSlotX(builder, SlotX):
    """This method is deprecated. Please switch to AddSlotX."""
    return AddSlotX(builder, SlotX)
def StartSlotXVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def FormationLocationExcelStartSlotXVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartSlotXVector(builder, numElems)
def End(builder): return builder.EndObject()
def FormationLocationExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)