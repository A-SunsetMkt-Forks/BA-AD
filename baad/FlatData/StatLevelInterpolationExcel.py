# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class StatLevelInterpolationExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = StatLevelInterpolationExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsStatLevelInterpolationExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # StatLevelInterpolationExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # StatLevelInterpolationExcel
    def Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # StatLevelInterpolationExcel
    def StatTypeIndex(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # StatLevelInterpolationExcel
    def StatTypeIndexAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # StatLevelInterpolationExcel
    def StatTypeIndexLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # StatLevelInterpolationExcel
    def StatTypeIndexIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def Start(builder): builder.StartObject(2)
def StatLevelInterpolationExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddLevel(builder, Level): builder.PrependInt64Slot(0, Level, 0)
def StatLevelInterpolationExcelAddLevel(builder, Level):
    """This method is deprecated. Please switch to AddLevel."""
    return AddLevel(builder, Level)
def AddStatTypeIndex(builder, StatTypeIndex): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(StatTypeIndex), 0)
def StatLevelInterpolationExcelAddStatTypeIndex(builder, StatTypeIndex):
    """This method is deprecated. Please switch to AddStatTypeIndex."""
    return AddStatTypeIndex(builder, StatTypeIndex)
def StartStatTypeIndexVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def StatLevelInterpolationExcelStartStatTypeIndexVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartStatTypeIndexVector(builder, numElems)
def End(builder): return builder.EndObject()
def StatLevelInterpolationExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)