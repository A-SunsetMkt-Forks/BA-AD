# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class StageFileRefreshSettingExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = StageFileRefreshSettingExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsStageFileRefreshSettingExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # StageFileRefreshSettingExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # StageFileRefreshSettingExcel
    def GroundId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # StageFileRefreshSettingExcel
    def ForceSave(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def Start(builder): builder.StartObject(2)
def StageFileRefreshSettingExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddGroundId(builder, GroundId): builder.PrependInt64Slot(0, GroundId, 0)
def StageFileRefreshSettingExcelAddGroundId(builder, GroundId):
    """This method is deprecated. Please switch to AddGroundId."""
    return AddGroundId(builder, GroundId)
def AddForceSave(builder, ForceSave): builder.PrependBoolSlot(1, ForceSave, 0)
def StageFileRefreshSettingExcelAddForceSave(builder, ForceSave):
    """This method is deprecated. Please switch to AddForceSave."""
    return AddForceSave(builder, ForceSave)
def End(builder): return builder.EndObject()
def StageFileRefreshSettingExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)