__author__ = 'Justin'
import math
from datetime import datetime, date, time, timedelta

longDeg = -111.867594
latDeg = 40.688335
longRad = math.radians(longDeg)
latRad = math.radians(latDeg)

print longRad
print latRad

# Correct for diff between timezone and actual location
LSTMDeg = -7 * 15
LSTMRad = math.radians(LSTMDeg)

print LSTMRad

#dstTime = clock time, today = actual time
dstTime = datetime.now()
today = dstTime + timedelta(0, 0, 0, 0, 0, 1, 0)
day = today.toordinal() - date(today.year, 1, 1).toordinal() + 1
B = (360 / float(365)) * (day - 81)

print day
print B

#Equation of Time: Accounts for eccentricity of orbit and LSTM throughout year
EoT = (9.87 * math.sin(2 * B) - 7.53 * math.cos(B) - 1.5 * math.sin(B))

print EoT

#Time Correction: Minutes of correction from LSTM
TC = 4 * (longDeg - LSTMDeg) + EoT

print TC

#Local Solar Time
LST = today + timedelta(0, 0, 0, 0, TC)

#Hour Angle: Distance from solar noon

HRADeg = 15 * ((LST.hour - 12) + (LST.minute / 60))
HRARad = math.radians(HRADeg)

print today
print LST
print HRADeg

#Declination Angle: Angle between equator and the sun
decAngDeg = 23.45 * math.sin(math.radians((360.0 / 365.0) * (284.0 + day)))
decAngRad = math.radians(decAngDeg)

print decAngDeg
print decAngRad

#Elevation/Altitude Angle: angular height of the sun, measured from horizontal

altAngleRad = math.asin((math.sin(decAngRad) * math.sin(latRad)) + \
                        (math.cos(decAngRad) * math.cos(latRad) * math.cos(HRARad)))
altAngleDeg = math.degrees(altAngleRad)

print altAngleDeg
print altAngleRad

#Zenith Angle: angular height of sun, measured from vertical

zenAngleRad = (2 * math.pi) - altAngleRad
zenAngleDeg = math.degrees(zenAngleRad)

print zenAngleDeg
print zenAngleRad

#Sunrise: Rearranging elevation/altitude equation

setrise = (1 / (math.pi / 12)) * math.acos((-1)*math.tan(latRad)*math.tan(altAngleDeg))
sunrise = 12 - setrise
sunset = 12 + setrise

print sunrise
print sunset
