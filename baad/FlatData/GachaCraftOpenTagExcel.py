# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GachaCraftOpenTagExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GachaCraftOpenTagExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsGachaCraftOpenTagExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # GachaCraftOpenTagExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GachaCraftOpenTagExcel
    def NodeTier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GachaCraftOpenTagExcel
    def Tag_(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # GachaCraftOpenTagExcel
    def Tag_AsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # GachaCraftOpenTagExcel
    def Tag_Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # GachaCraftOpenTagExcel
    def Tag_IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def Start(builder): builder.StartObject(2)
def GachaCraftOpenTagExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddNodeTier(builder, NodeTier): builder.PrependInt32Slot(0, NodeTier, 0)
def GachaCraftOpenTagExcelAddNodeTier(builder, NodeTier):
    """This method is deprecated. Please switch to AddNodeTier."""
    return AddNodeTier(builder, NodeTier)
def AddTag_(builder, Tag_): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Tag_), 0)
def GachaCraftOpenTagExcelAddTag_(builder, Tag_):
    """This method is deprecated. Please switch to AddTag_."""
    return AddTag_(builder, Tag_)
def StartTag_Vector(builder, numElems): return builder.StartVector(4, numElems, 4)
def GachaCraftOpenTagExcelStartTag_Vector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartTag_Vector(builder, numElems)
def End(builder): return builder.EndObject()
def GachaCraftOpenTagExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)