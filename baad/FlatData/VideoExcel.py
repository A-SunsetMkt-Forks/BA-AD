# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class VideoExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = VideoExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsVideoExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # VideoExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # VideoExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # VideoExcel
    def Nation_(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # VideoExcel
    def Nation_AsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # VideoExcel
    def Nation_Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # VideoExcel
    def Nation_IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # VideoExcel
    def VideoPath(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # VideoExcel
    def VideoPathLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # VideoExcel
    def VideoPathIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # VideoExcel
    def SoundPath(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # VideoExcel
    def SoundPathLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # VideoExcel
    def SoundPathIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # VideoExcel
    def SoundVolume(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # VideoExcel
    def SoundVolumeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # VideoExcel
    def SoundVolumeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # VideoExcel
    def SoundVolumeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

def Start(builder): builder.StartObject(5)
def VideoExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def VideoExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddNation_(builder, Nation_): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Nation_), 0)
def VideoExcelAddNation_(builder, Nation_):
    """This method is deprecated. Please switch to AddNation_."""
    return AddNation_(builder, Nation_)
def StartNation_Vector(builder, numElems): return builder.StartVector(4, numElems, 4)
def VideoExcelStartNation_Vector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartNation_Vector(builder, numElems)
def AddVideoPath(builder, VideoPath): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(VideoPath), 0)
def VideoExcelAddVideoPath(builder, VideoPath):
    """This method is deprecated. Please switch to AddVideoPath."""
    return AddVideoPath(builder, VideoPath)
def StartVideoPathVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def VideoExcelStartVideoPathVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartVideoPathVector(builder, numElems)
def AddSoundPath(builder, SoundPath): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(SoundPath), 0)
def VideoExcelAddSoundPath(builder, SoundPath):
    """This method is deprecated. Please switch to AddSoundPath."""
    return AddSoundPath(builder, SoundPath)
def StartSoundPathVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def VideoExcelStartSoundPathVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartSoundPathVector(builder, numElems)
def AddSoundVolume(builder, SoundVolume): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(SoundVolume), 0)
def VideoExcelAddSoundVolume(builder, SoundVolume):
    """This method is deprecated. Please switch to AddSoundVolume."""
    return AddSoundVolume(builder, SoundVolume)
def StartSoundVolumeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def VideoExcelStartSoundVolumeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartSoundVolumeVector(builder, numElems)
def End(builder): return builder.EndObject()
def VideoExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)