# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EventContentArchiveBannerOffsetExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventContentArchiveBannerOffsetExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEventContentArchiveBannerOffsetExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # EventContentArchiveBannerOffsetExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EventContentArchiveBannerOffsetExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentArchiveBannerOffsetExcel
    def OffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # EventContentArchiveBannerOffsetExcel
    def OffsetY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # EventContentArchiveBannerOffsetExcel
    def ScaleX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # EventContentArchiveBannerOffsetExcel
    def ScaleY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def Start(builder): builder.StartObject(5)
def EventContentArchiveBannerOffsetExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)
def EventContentArchiveBannerOffsetExcelAddEventContentId(builder, EventContentId):
    """This method is deprecated. Please switch to AddEventContentId."""
    return AddEventContentId(builder, EventContentId)
def AddOffsetX(builder, OffsetX): builder.PrependFloat32Slot(1, OffsetX, 0.0)
def EventContentArchiveBannerOffsetExcelAddOffsetX(builder, OffsetX):
    """This method is deprecated. Please switch to AddOffsetX."""
    return AddOffsetX(builder, OffsetX)
def AddOffsetY(builder, OffsetY): builder.PrependFloat32Slot(2, OffsetY, 0.0)
def EventContentArchiveBannerOffsetExcelAddOffsetY(builder, OffsetY):
    """This method is deprecated. Please switch to AddOffsetY."""
    return AddOffsetY(builder, OffsetY)
def AddScaleX(builder, ScaleX): builder.PrependFloat32Slot(3, ScaleX, 0.0)
def EventContentArchiveBannerOffsetExcelAddScaleX(builder, ScaleX):
    """This method is deprecated. Please switch to AddScaleX."""
    return AddScaleX(builder, ScaleX)
def AddScaleY(builder, ScaleY): builder.PrependFloat32Slot(4, ScaleY, 0.0)
def EventContentArchiveBannerOffsetExcelAddScaleY(builder, ScaleY):
    """This method is deprecated. Please switch to AddScaleY."""
    return AddScaleY(builder, ScaleY)
def End(builder): return builder.EndObject()
def EventContentArchiveBannerOffsetExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)