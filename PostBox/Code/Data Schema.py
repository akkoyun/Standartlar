from pydantic import BaseModel, Field, conlist
from typing import Optional, List

# Define IoT RAW Data Base Model 02.00.00

class Info(BaseModel):
    ID: str
    Hardware: Optional[str] = None
    Firmware: Optional[str] = None
    Temperature: Optional[float] = None
    Humidity: Optional[float] = None

class Battery(BaseModel):
    IV: float
    AC: float
    SOC: float
    FB: Optional[int] = None
    IB: Optional[int] = None
    T: Optional[float] = None
    Charge: int

class Power(BaseModel):
    Battery: Battery

class Module(BaseModel):
    Firmware: str
    IMEI: str
    Manufacturer: int
    Model: int
    Serial: str

class Operator(BaseModel):
    Iccid: Optional[str] = None
    IP: Optional[str] = None
    Code: int
    RSSI: int
    ConnTime: Optional[int] = None
    LAC: Optional[str] = None
    Cell_ID: Optional[str] = None

class GSM(BaseModel):
    Module: Optional[Module] = None
    Operator: Operator

class IoT(BaseModel):
    GSM: GSM

class Device(BaseModel):
    Info: Info
    Power: Power
    IoT: IoT

class StatusLimit(BaseModel):
    Control: bool
    Min: Optional[int]
    Max: Optional[int]

class StatusRegression(BaseModel):
    Control: bool
    Max: Optional[float]

class StatusImbalance(BaseModel):
    Control: bool
    Max: Optional[float]

class StatusPressure(BaseModel):
    Limit: Optional[StatusLimit]
    Regression: Optional[StatusRegression]

class StatusVoltage(BaseModel):
    Limit: Optional[StatusLimit]
    Imbalance: Optional[StatusImbalance]

class StatusCurrent(BaseModel):
    Limit: Optional[StatusLimit]
    Imbalance: Optional[StatusImbalance]
    Multiplexer: Optional[int]

class StatusFrequency(BaseModel):
    Limit: Optional[StatusLimit]

class StatusControl(BaseModel):
    PhaseLose: Optional[bool]
    Thermic: Optional[bool]
    MotorProtection: Optional[bool]
    ContactorAnomaly: Optional[bool]
    Pressure: Optional[StatusPressure]
    Voltage: Optional[StatusVoltage]
    Current: Optional[StatusCurrent]
    Frequency: Optional[StatusFrequency]

class Status(BaseModel):
	Device: int
	Fault: Optional[int] = None
	Control: Optional[StatusControl]

class Pressure(BaseModel):
    Pout: conlist(float, min_items=1, max_items=8)

class Voltage(BaseModel):
    PhaseR: conlist(float, min_items=1, max_items=8)
    PhaseS: conlist(float, min_items=1, max_items=8)
    PhaseT: conlist(float, min_items=1, max_items=8)

class Current(BaseModel):
    PhaseR: conlist(float, min_items=1, max_items=8)
    PhaseS: conlist(float, min_items=1, max_items=8)
    PhaseT: conlist(float, min_items=1, max_items=8)

class PowerFactor(BaseModel):
    PhaseR: Optional[conlist(float, min_items=1, max_items=8)]
    PhaseS: Optional[conlist(float, min_items=1, max_items=8)]
    PhaseT: Optional[conlist(float, min_items=1, max_items=8)]
    PhaseA: Optional[conlist(float, min_items=1, max_items=8)]

class Frequency(BaseModel):
    FQ: conlist(float, min_items=1, max_items=8)

class Consumption(BaseModel):
    Active: int
    ReActive: int

class Energy(BaseModel):
    Voltage: Optional[Voltage]
    Current: Optional[Current]
    PowerFactor: Optional[PowerFactor]
    Frequency: Optional[Frequency]
    Consumption: Optional[Consumption]

class Input(BaseModel):
	IN1: bool
	IN2: bool
	IN3: bool
	IN4: bool
	IN5: bool
	IN6: bool
	IN7: bool
	IN8: bool

class Location(BaseModel):
    Lat: float
    Long: float

class Environment(BaseModel):
	AT: Optional[float]
	AH: Optional[float]
	AP: Optional[float]
	UV: Optional[int]
	ST: Optional[conlist(float, min_items=1, max_items=8)]
	R: Optional[int]
	WD: Optional[int]
	WS: Optional[float]

class Payload(BaseModel):
    TimeStamp: str
    Status: Optional[Status]
    Pressure: Optional[Pressure]
    Energy: Optional[Energy]
    Input: Optional[Input]
    Location: Optional[Location]
    Environment: Optional[Environment]

class DataPack(BaseModel):
    Command: str
    Device: Device
    Payload: Payload
