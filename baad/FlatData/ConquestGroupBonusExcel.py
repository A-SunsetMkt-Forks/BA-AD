# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestGroupBonusExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestGroupBonusExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsConquestGroupBonusExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ConquestGroupBonusExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConquestGroupBonusExcel
    def ConquestBonusId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConquestGroupBonusExcel
    def School_(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ConquestGroupBonusExcel
    def School_AsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # ConquestGroupBonusExcel
    def School_Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConquestGroupBonusExcel
    def School_IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # ConquestGroupBonusExcel
    def RecommandLocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # ConquestGroupBonusExcel
    def BonusParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ConquestGroupBonusExcel
    def BonusParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # ConquestGroupBonusExcel
    def BonusParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConquestGroupBonusExcel
    def BonusParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # ConquestGroupBonusExcel
    def BonusId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ConquestGroupBonusExcel
    def BonusIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ConquestGroupBonusExcel
    def BonusIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConquestGroupBonusExcel
    def BonusIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # ConquestGroupBonusExcel
    def BonusCharacterCount1(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ConquestGroupBonusExcel
    def BonusCharacterCount1AsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # ConquestGroupBonusExcel
    def BonusCharacterCount1Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConquestGroupBonusExcel
    def BonusCharacterCount1IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # ConquestGroupBonusExcel
    def BonusPercentage1(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ConquestGroupBonusExcel
    def BonusPercentage1AsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ConquestGroupBonusExcel
    def BonusPercentage1Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConquestGroupBonusExcel
    def BonusPercentage1IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

    # ConquestGroupBonusExcel
    def BonusCharacterCount2(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ConquestGroupBonusExcel
    def BonusCharacterCount2AsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # ConquestGroupBonusExcel
    def BonusCharacterCount2Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConquestGroupBonusExcel
    def BonusCharacterCount2IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0

    # ConquestGroupBonusExcel
    def BonusPercentage2(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ConquestGroupBonusExcel
    def BonusPercentage2AsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ConquestGroupBonusExcel
    def BonusPercentage2Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConquestGroupBonusExcel
    def BonusPercentage2IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0

    # ConquestGroupBonusExcel
    def BonusCharacterCount3(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ConquestGroupBonusExcel
    def BonusCharacterCount3AsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # ConquestGroupBonusExcel
    def BonusCharacterCount3Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConquestGroupBonusExcel
    def BonusCharacterCount3IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0

    # ConquestGroupBonusExcel
    def BonusPercentage3(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ConquestGroupBonusExcel
    def BonusPercentage3AsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ConquestGroupBonusExcel
    def BonusPercentage3Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConquestGroupBonusExcel
    def BonusPercentage3IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0

def Start(builder): builder.StartObject(11)
def ConquestGroupBonusExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddConquestBonusId(builder, ConquestBonusId): builder.PrependInt64Slot(0, ConquestBonusId, 0)
def ConquestGroupBonusExcelAddConquestBonusId(builder, ConquestBonusId):
    """This method is deprecated. Please switch to AddConquestBonusId."""
    return AddConquestBonusId(builder, ConquestBonusId)
def AddSchool_(builder, School_): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(School_), 0)
def ConquestGroupBonusExcelAddSchool_(builder, School_):
    """This method is deprecated. Please switch to AddSchool_."""
    return AddSchool_(builder, School_)
def StartSchool_Vector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ConquestGroupBonusExcelStartSchool_Vector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartSchool_Vector(builder, numElems)
def AddRecommandLocalizeEtcId(builder, RecommandLocalizeEtcId): builder.PrependUint32Slot(2, RecommandLocalizeEtcId, 0)
def ConquestGroupBonusExcelAddRecommandLocalizeEtcId(builder, RecommandLocalizeEtcId):
    """This method is deprecated. Please switch to AddRecommandLocalizeEtcId."""
    return AddRecommandLocalizeEtcId(builder, RecommandLocalizeEtcId)
def AddBonusParcelType(builder, BonusParcelType): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(BonusParcelType), 0)
def ConquestGroupBonusExcelAddBonusParcelType(builder, BonusParcelType):
    """This method is deprecated. Please switch to AddBonusParcelType."""
    return AddBonusParcelType(builder, BonusParcelType)
def StartBonusParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ConquestGroupBonusExcelStartBonusParcelTypeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartBonusParcelTypeVector(builder, numElems)
def AddBonusId(builder, BonusId): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(BonusId), 0)
def ConquestGroupBonusExcelAddBonusId(builder, BonusId):
    """This method is deprecated. Please switch to AddBonusId."""
    return AddBonusId(builder, BonusId)
def StartBonusIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ConquestGroupBonusExcelStartBonusIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartBonusIdVector(builder, numElems)
def AddBonusCharacterCount1(builder, BonusCharacterCount1): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(BonusCharacterCount1), 0)
def ConquestGroupBonusExcelAddBonusCharacterCount1(builder, BonusCharacterCount1):
    """This method is deprecated. Please switch to AddBonusCharacterCount1."""
    return AddBonusCharacterCount1(builder, BonusCharacterCount1)
def StartBonusCharacterCount1Vector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ConquestGroupBonusExcelStartBonusCharacterCount1Vector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartBonusCharacterCount1Vector(builder, numElems)
def AddBonusPercentage1(builder, BonusPercentage1): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(BonusPercentage1), 0)
def ConquestGroupBonusExcelAddBonusPercentage1(builder, BonusPercentage1):
    """This method is deprecated. Please switch to AddBonusPercentage1."""
    return AddBonusPercentage1(builder, BonusPercentage1)
def StartBonusPercentage1Vector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ConquestGroupBonusExcelStartBonusPercentage1Vector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartBonusPercentage1Vector(builder, numElems)
def AddBonusCharacterCount2(builder, BonusCharacterCount2): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(BonusCharacterCount2), 0)
def ConquestGroupBonusExcelAddBonusCharacterCount2(builder, BonusCharacterCount2):
    """This method is deprecated. Please switch to AddBonusCharacterCount2."""
    return AddBonusCharacterCount2(builder, BonusCharacterCount2)
def StartBonusCharacterCount2Vector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ConquestGroupBonusExcelStartBonusCharacterCount2Vector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartBonusCharacterCount2Vector(builder, numElems)
def AddBonusPercentage2(builder, BonusPercentage2): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(BonusPercentage2), 0)
def ConquestGroupBonusExcelAddBonusPercentage2(builder, BonusPercentage2):
    """This method is deprecated. Please switch to AddBonusPercentage2."""
    return AddBonusPercentage2(builder, BonusPercentage2)
def StartBonusPercentage2Vector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ConquestGroupBonusExcelStartBonusPercentage2Vector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartBonusPercentage2Vector(builder, numElems)
def AddBonusCharacterCount3(builder, BonusCharacterCount3): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(BonusCharacterCount3), 0)
def ConquestGroupBonusExcelAddBonusCharacterCount3(builder, BonusCharacterCount3):
    """This method is deprecated. Please switch to AddBonusCharacterCount3."""
    return AddBonusCharacterCount3(builder, BonusCharacterCount3)
def StartBonusCharacterCount3Vector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ConquestGroupBonusExcelStartBonusCharacterCount3Vector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartBonusCharacterCount3Vector(builder, numElems)
def AddBonusPercentage3(builder, BonusPercentage3): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(BonusPercentage3), 0)
def ConquestGroupBonusExcelAddBonusPercentage3(builder, BonusPercentage3):
    """This method is deprecated. Please switch to AddBonusPercentage3."""
    return AddBonusPercentage3(builder, BonusPercentage3)
def StartBonusPercentage3Vector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ConquestGroupBonusExcelStartBonusPercentage3Vector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartBonusPercentage3Vector(builder, numElems)
def End(builder): return builder.EndObject()
def ConquestGroupBonusExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)