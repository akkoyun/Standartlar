from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Define IoT RAW Data Base Model
# PowerStat Model Version 01.02.00
# WeatherStat Model Version 01.02.00
class IoT_Data_Pack_Model(BaseModel):

	# Define Command
	Command: str

	# Define Device
	class IoT_Data_Pack_Device(BaseModel):

		# Define Info
		class IoT_Data_Pack_Info(BaseModel):
			
			# Device ID
			ID: str
			
			# Device Hardware Version
			Hardware: Optional[str] = None
			
			# Device Firmware Version
			Firmware: Optional[str] = None
			
			# Device PCB Temperature
			Temperature: float
			
			# Device PCB Humidity
			Humidity: float
		
		# Device Info
		Info: IoT_Data_Pack_Info

		# Define Power
		class IoT_Data_Pack_Power(BaseModel):

			# Define Battery
			class IoT_Data_Pack_Battery(BaseModel):

				# Instant Battery Voltage
				IV: float

				# Average Battery Current
				AC: float

				# Battery State of Charge
				SOC: float

				# Battery Charge State
				Charge: int

				# Battery Temperature
				T: Optional[float]

				# Battery Full Battery Cap
				FB: Optional[int]

				# Battery Instant Battery Cap
				IB: Optional[int]
			
			# Device Battery
			Battery: IoT_Data_Pack_Battery
		
		# Device Power
		Power: IoT_Data_Pack_Power

		# Define IoT
		class IoT_Data_Pack_IoT(BaseModel):

			# Define GSM
			class IoT_Data_Pack_GSM(BaseModel):

				# Define IoT Module
				class IoT_Data_Pack_IoT_Module(BaseModel):
					
					# GSM Module Firmware
					Firmware: Optional[str]

					# Module IMEI Number
					IMEI: Optional[str]

					# Module Manufacturer
					Manufacturer: Optional[int]

					# Module Model
					Model: Optional[int]

					# Module Serial Number
					Serial: Optional[str]
				
				# Device IoT Module
				Module: Optional[IoT_Data_Pack_IoT_Module]

				# Define IoT Operator
				class IoT_Data_Pack_IoT_Operator(BaseModel):
					
					# SIM ICCID
					ICCID: Optional[str]

					# Operator Code
					Code: int

					# IP
					IP: str
					
					# RSSI
					RSSI: int
					
					# Connection Time
					ConnTime: Optional[int]
					
					# LAC
					LAC: Optional[str]
					
					# Cell ID
					Cell_ID: Optional[str]

				# IoT Operator
				Operator: IoT_Data_Pack_IoT_Operator
			
			# Device GSM
			GSM: IoT_Data_Pack_GSM

		# Device IoT
		iot: IoT_Data_Pack_IoT

	# Device
	Device: IoT_Data_Pack_Device

	# Define payload
	class IoT_Data_Pack_Payload(BaseModel):

		# TimeStamp
		TimeStamp: datetime

		# PowerStat Model Definition
		class IoT_Data_Pack_Payload_PowerStat(BaseModel):

			# Device Status
			DeviceStatus: int

			# Fault Status
			FaultStatus: int

			# Pressure Model Definition
			class IoT_Data_Pack_Payload_PowerStat_Pressure(BaseModel):
				
				# Min Pressure in Measurement Interval
				Min: Optional[float] = None

				# Max Pressure in Measurement Interval
				Max: Optional[float] = None

				# Avg Pressure of Measurement Interval
				Avg: Optional[float] = None

				# Last Readed Pressure in Measurement Interval
				Inst: Optional[float] = None

				# Slope of Pressure Trend in Measurement Interval
				Slope: Optional[float] = None

				# Offset of Pressure Trend in Measurement Interval
				Offset: Optional[float] = None

				# R2 of Pressure Trend in Measurement Interval
				R2: Optional[float] = None

				# Measured Data Count in Measurement Interval
				DataCount: Optional[int] = None

			# Pressure
			Pressure: Optional[IoT_Data_Pack_Payload_PowerStat_Pressure]

			# Energy Model Definition
			class IoT_Data_Pack_Payload_PowerStat_Energy(BaseModel):

				# Last Measured Voltage Array (R,S,T)
				Voltage: list[Optional[float]] = None

				# Last Measured Current Array (R,S,T)
				Current: list[Optional[float]] = None

				# Last Measured PowerFactor Average
				PowerFactor: Optional[float] = None

				# Total Energy Consumption Array in Send Interval (Active,Reactive)
				Consumption: list[Optional[float]] = None

				# Last Measured Frequency Value
				Frequency: Optional[float] = None

			# Energy
			Energy: Optional[IoT_Data_Pack_Payload_PowerStat_Energy]

			# Falut Control List Array
			Fault: list[Optional[bool]] = None

		# PowerStat Payload
		PowerStat: Optional[IoT_Data_Pack_Payload_PowerStat]

		# WeatherStat Model Definition
		class IoT_Data_Pack_Payload_WeatherStat(BaseModel):

			# Device Status
			DeviceStatus: int

			# Location Definition
			class IoT_Data_Pack_Payload_WeatherStat_Location(BaseModel):
				
				# Latitude Value of Device
				Latitude: float

				# Longtitude Value of Device
				Longitude: float

			# Location
			Location: Optional[IoT_Data_Pack_Payload_WeatherStat_Location]

			# Environment Measurement Definition
			class IoT_Data_Pack_Payload_WeatherStat_Environment(BaseModel):
				
				# Last Measured Air Temperature Value
				AT: Optional[float] = None

				# Last Measured Relative Humidity Value
				AH: Optional[float] = None

				# Last Measured Air Pressure Value
				AP: Optional[float] = None

				# Last Measured UV Value
				UV: Optional[int] = None

				# Last Measured Soil Temperature Value
				ST: list[Optional[float]] = None

				# Last Measured Rain Value
				R: Optional[int] = None

				# Last Measured Wind Direction Value
				WD: Optional[int] = None

				# Last Measured Wind Speed Value
				WS: Optional[float] = None

			# Environment
			Environment: IoT_Data_Pack_Payload_WeatherStat_Environment

		# WeatherStat Payload
		WeatherStat: Optional[IoT_Data_Pack_Payload_WeatherStat]

	# Payload
	Payload: IoT_Data_Pack_Payload

