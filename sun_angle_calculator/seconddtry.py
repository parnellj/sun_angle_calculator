__author__ = 'Justin'
import math
from math import cos, sin, tan, acos, asin, atan
from datetime import datetime, date, time, timedelta

longDeg = -111.867594
longRad = math.radians(longDeg)
latDeg = 40.688335
latRad = math.radians(latDeg)
dstTime = datetime.now()
today = dstTime + timedelta(0, 0, 0, 0, 0, -1, 0)
day = today.toordinal() - date(today.year, 1, 1).toordinal() + 1

B = (360 * (day - 81)) / float(365)

EOT = (9.87 * math.sin(2 * B)) - (7.53 * math.cos(B)) - (1.5 * math.sin(B))
LSoT = today + timedelta(minutes=4 * (longDeg + 105) + EOT)
HourAngle = ((LSoT.hour + (LSoT.minute / 60.0)) - 12) * 15
HourAngleRad = math.radians(HourAngle)

dec = 23.45 * math.sin(math.radians((360 / float(365)) * (284 + day)))
decRad = math.radians(dec)

altAngRad = math.asin(
    (math.cos(latRad) * math.cos(decRad) * math.cos(HourAngleRad)) + (math.sin(latRad) * math.sin(decRad)))
altAng = math.degrees(altAngRad)

azAngRad = math.acos(
    (math.sin(altAngRad) * math.sin(latRad) - math.sin(decRad)) / (math.cos(altAngRad) * math.cos(latRad)))
azAng = math.degrees(azAngRad)

altHoriz = -0.8333 - 0.347 * math.sqrt(1319)



print "Altitude Angle ", altAng
print "Azimuth Angle ", azAng
print "Clock Time ", dstTime.time()
print "Local Solar Time ", LSoT.time()
print "Hour Angle ", HourAngle
print "Declination ", dec
print "Equation of Time (Minutes) ", EOT
print "Horizon altitude ", altHoriz

# a = (sin(latRad) * sin(decRad))
# b = cos(latRad) * cos(decRad)
# c = (-1 * a) / b
# d = acos(c)
# e = (math.degrees(d) * 4) + 90
#
# print e
# sunrise = datetime.combine(date.today(), time(hour=12))
# print sunrise
