# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GachaCraftNodeExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GachaCraftNodeExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsGachaCraftNodeExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # GachaCraftNodeExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GachaCraftNodeExcel
    def ID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GachaCraftNodeExcel
    def Tier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GachaCraftNodeExcel
    def QuickCraftNodeDisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GachaCraftNodeExcel
    def NodeQuality(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GachaCraftNodeExcel
    def Icon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # GachaCraftNodeExcel
    def LocalizeKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # GachaCraftNodeExcel
    def Property(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(7)
def GachaCraftNodeExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddID(builder, ID): builder.PrependInt64Slot(0, ID, 0)
def GachaCraftNodeExcelAddID(builder, ID):
    """This method is deprecated. Please switch to AddID."""
    return AddID(builder, ID)
def AddTier(builder, Tier): builder.PrependInt64Slot(1, Tier, 0)
def GachaCraftNodeExcelAddTier(builder, Tier):
    """This method is deprecated. Please switch to AddTier."""
    return AddTier(builder, Tier)
def AddQuickCraftNodeDisplayOrder(builder, QuickCraftNodeDisplayOrder): builder.PrependInt32Slot(2, QuickCraftNodeDisplayOrder, 0)
def GachaCraftNodeExcelAddQuickCraftNodeDisplayOrder(builder, QuickCraftNodeDisplayOrder):
    """This method is deprecated. Please switch to AddQuickCraftNodeDisplayOrder."""
    return AddQuickCraftNodeDisplayOrder(builder, QuickCraftNodeDisplayOrder)
def AddNodeQuality(builder, NodeQuality): builder.PrependInt64Slot(3, NodeQuality, 0)
def GachaCraftNodeExcelAddNodeQuality(builder, NodeQuality):
    """This method is deprecated. Please switch to AddNodeQuality."""
    return AddNodeQuality(builder, NodeQuality)
def AddIcon(builder, Icon): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(Icon), 0)
def GachaCraftNodeExcelAddIcon(builder, Icon):
    """This method is deprecated. Please switch to AddIcon."""
    return AddIcon(builder, Icon)
def AddLocalizeKey(builder, LocalizeKey): builder.PrependUint32Slot(5, LocalizeKey, 0)
def GachaCraftNodeExcelAddLocalizeKey(builder, LocalizeKey):
    """This method is deprecated. Please switch to AddLocalizeKey."""
    return AddLocalizeKey(builder, LocalizeKey)
def AddProperty(builder, Property): builder.PrependInt64Slot(6, Property, 0)
def GachaCraftNodeExcelAddProperty(builder, Property):
    """This method is deprecated. Please switch to AddProperty."""
    return AddProperty(builder, Property)
def End(builder): return builder.EndObject()
def GachaCraftNodeExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)