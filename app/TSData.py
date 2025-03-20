# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TSData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TSData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTSData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # TSData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TSData
    def IsEmergency(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TSData
    def IsEmergencyButtonPressed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TSData
    def IsEmergencySwitchToggled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TSData
    def IsHydrogenLeaking(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TSData
    def IsScRelayClosed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TSData
    def IsTimeResetButtonPressed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TSData
    def IsHalfSpeedButtonPressed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TSData
    def IsGasButtonPressed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TSData
    def FuelCellMode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # TSData
    def FcCurrent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def FcScCurrent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def ScMotorCurrent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def FcVoltage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def ScVoltage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def HydrogenSensorVoltage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def FuelCellTemperature(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def FanRpm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TSData
    def VehicleSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def MotorPwm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TSData
    def HydrogenPressure(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def GpsLatitude(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def GpsLongitude(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def GpsAltitude(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def GpsSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def MotorSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def MotorCurrent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def FcCurrentRaw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def FcVoltageRaw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def McCurrent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TSData
    def LapNumber(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

def TSDataStart(builder):
    builder.StartObject(30)

def Start(builder):
    TSDataStart(builder)

def TSDataAddIsEmergency(builder, isEmergency):
    builder.PrependBoolSlot(0, isEmergency, 0)

def AddIsEmergency(builder, isEmergency):
    TSDataAddIsEmergency(builder, isEmergency)

def TSDataAddIsEmergencyButtonPressed(builder, isEmergencyButtonPressed):
    builder.PrependBoolSlot(1, isEmergencyButtonPressed, 0)

def AddIsEmergencyButtonPressed(builder, isEmergencyButtonPressed):
    TSDataAddIsEmergencyButtonPressed(builder, isEmergencyButtonPressed)

def TSDataAddIsEmergencySwitchToggled(builder, isEmergencySwitchToggled):
    builder.PrependBoolSlot(2, isEmergencySwitchToggled, 0)

def AddIsEmergencySwitchToggled(builder, isEmergencySwitchToggled):
    TSDataAddIsEmergencySwitchToggled(builder, isEmergencySwitchToggled)

def TSDataAddIsHydrogenLeaking(builder, isHydrogenLeaking):
    builder.PrependBoolSlot(3, isHydrogenLeaking, 0)

def AddIsHydrogenLeaking(builder, isHydrogenLeaking):
    TSDataAddIsHydrogenLeaking(builder, isHydrogenLeaking)

def TSDataAddIsScRelayClosed(builder, isScRelayClosed):
    builder.PrependBoolSlot(4, isScRelayClosed, 0)

def AddIsScRelayClosed(builder, isScRelayClosed):
    TSDataAddIsScRelayClosed(builder, isScRelayClosed)

def TSDataAddIsTimeResetButtonPressed(builder, isTimeResetButtonPressed):
    builder.PrependBoolSlot(5, isTimeResetButtonPressed, 0)

def AddIsTimeResetButtonPressed(builder, isTimeResetButtonPressed):
    TSDataAddIsTimeResetButtonPressed(builder, isTimeResetButtonPressed)

def TSDataAddIsHalfSpeedButtonPressed(builder, isHalfSpeedButtonPressed):
    builder.PrependBoolSlot(6, isHalfSpeedButtonPressed, 0)

def AddIsHalfSpeedButtonPressed(builder, isHalfSpeedButtonPressed):
    TSDataAddIsHalfSpeedButtonPressed(builder, isHalfSpeedButtonPressed)

def TSDataAddIsGasButtonPressed(builder, isGasButtonPressed):
    builder.PrependBoolSlot(7, isGasButtonPressed, 0)

def AddIsGasButtonPressed(builder, isGasButtonPressed):
    TSDataAddIsGasButtonPressed(builder, isGasButtonPressed)

def TSDataAddFuelCellMode(builder, fuelCellMode):
    builder.PrependInt8Slot(8, fuelCellMode, 0)

def AddFuelCellMode(builder, fuelCellMode):
    TSDataAddFuelCellMode(builder, fuelCellMode)

def TSDataAddFcCurrent(builder, fcCurrent):
    builder.PrependFloat32Slot(9, fcCurrent, 0.0)

def AddFcCurrent(builder, fcCurrent):
    TSDataAddFcCurrent(builder, fcCurrent)

def TSDataAddFcScCurrent(builder, fcScCurrent):
    builder.PrependFloat32Slot(10, fcScCurrent, 0.0)

def AddFcScCurrent(builder, fcScCurrent):
    TSDataAddFcScCurrent(builder, fcScCurrent)

def TSDataAddScMotorCurrent(builder, scMotorCurrent):
    builder.PrependFloat32Slot(11, scMotorCurrent, 0.0)

def AddScMotorCurrent(builder, scMotorCurrent):
    TSDataAddScMotorCurrent(builder, scMotorCurrent)

def TSDataAddFcVoltage(builder, fcVoltage):
    builder.PrependFloat32Slot(12, fcVoltage, 0.0)

def AddFcVoltage(builder, fcVoltage):
    TSDataAddFcVoltage(builder, fcVoltage)

def TSDataAddScVoltage(builder, scVoltage):
    builder.PrependFloat32Slot(13, scVoltage, 0.0)

def AddScVoltage(builder, scVoltage):
    TSDataAddScVoltage(builder, scVoltage)

def TSDataAddHydrogenSensorVoltage(builder, hydrogenSensorVoltage):
    builder.PrependFloat32Slot(14, hydrogenSensorVoltage, 0.0)

def AddHydrogenSensorVoltage(builder, hydrogenSensorVoltage):
    TSDataAddHydrogenSensorVoltage(builder, hydrogenSensorVoltage)

def TSDataAddFuelCellTemperature(builder, fuelCellTemperature):
    builder.PrependFloat32Slot(15, fuelCellTemperature, 0.0)

def AddFuelCellTemperature(builder, fuelCellTemperature):
    TSDataAddFuelCellTemperature(builder, fuelCellTemperature)

def TSDataAddFanRpm(builder, fanRpm):
    builder.PrependInt32Slot(16, fanRpm, 0)

def AddFanRpm(builder, fanRpm):
    TSDataAddFanRpm(builder, fanRpm)

def TSDataAddVehicleSpeed(builder, vehicleSpeed):
    builder.PrependFloat32Slot(17, vehicleSpeed, 0.0)

def AddVehicleSpeed(builder, vehicleSpeed):
    TSDataAddVehicleSpeed(builder, vehicleSpeed)

def TSDataAddMotorPwm(builder, motorPwm):
    builder.PrependInt32Slot(18, motorPwm, 0)

def AddMotorPwm(builder, motorPwm):
    TSDataAddMotorPwm(builder, motorPwm)

def TSDataAddHydrogenPressure(builder, hydrogenPressure):
    builder.PrependFloat32Slot(19, hydrogenPressure, 0.0)

def AddHydrogenPressure(builder, hydrogenPressure):
    TSDataAddHydrogenPressure(builder, hydrogenPressure)

def TSDataAddGpsLatitude(builder, gpsLatitude):
    builder.PrependFloat32Slot(20, gpsLatitude, 0.0)

def AddGpsLatitude(builder, gpsLatitude):
    TSDataAddGpsLatitude(builder, gpsLatitude)

def TSDataAddGpsLongitude(builder, gpsLongitude):
    builder.PrependFloat32Slot(21, gpsLongitude, 0.0)

def AddGpsLongitude(builder, gpsLongitude):
    TSDataAddGpsLongitude(builder, gpsLongitude)

def TSDataAddGpsAltitude(builder, gpsAltitude):
    builder.PrependFloat32Slot(22, gpsAltitude, 0.0)

def AddGpsAltitude(builder, gpsAltitude):
    TSDataAddGpsAltitude(builder, gpsAltitude)

def TSDataAddGpsSpeed(builder, gpsSpeed):
    builder.PrependFloat32Slot(23, gpsSpeed, 0.0)

def AddGpsSpeed(builder, gpsSpeed):
    TSDataAddGpsSpeed(builder, gpsSpeed)

def TSDataAddMotorSpeed(builder, motorSpeed):
    builder.PrependFloat32Slot(24, motorSpeed, 0.0)

def AddMotorSpeed(builder, motorSpeed):
    TSDataAddMotorSpeed(builder, motorSpeed)

def TSDataAddMotorCurrent(builder, motorCurrent):
    builder.PrependFloat32Slot(25, motorCurrent, 0.0)

def AddMotorCurrent(builder, motorCurrent):
    TSDataAddMotorCurrent(builder, motorCurrent)

def TSDataAddFcCurrentRaw(builder, fcCurrentRaw):
    builder.PrependFloat32Slot(26, fcCurrentRaw, 0.0)

def AddFcCurrentRaw(builder, fcCurrentRaw):
    TSDataAddFcCurrentRaw(builder, fcCurrentRaw)

def TSDataAddFcVoltageRaw(builder, fcVoltageRaw):
    builder.PrependFloat32Slot(27, fcVoltageRaw, 0.0)

def AddFcVoltageRaw(builder, fcVoltageRaw):
    TSDataAddFcVoltageRaw(builder, fcVoltageRaw)

def TSDataAddMcCurrent(builder, mcCurrent):
    builder.PrependFloat32Slot(28, mcCurrent, 0.0)

def AddMcCurrent(builder, mcCurrent):
    TSDataAddMcCurrent(builder, mcCurrent)

def TSDataAddLapNumber(builder, lapNumber):
    builder.PrependUint8Slot(29, lapNumber, 0)

def AddLapNumber(builder, lapNumber):
    TSDataAddLapNumber(builder, lapNumber)

def TSDataEnd(builder):
    return builder.EndObject()

def End(builder):
    return TSDataEnd(builder)
