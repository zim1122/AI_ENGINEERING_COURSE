d={"zim":75438750,"mohtasim":583490578,"billah":47398567}
print(d)
print(d["zim"])
d["sam"]="456738959"
print(d)
del d["zim"]
print(d)
for key in d:
    print("key:",key,"value:",d[key])
    

d.clear()
print(d)

# tuple is nothing but a list of values group together    
# list all the values have similar meaning
# tuple all the values have different meaning
point=(5,9)
print(point[0])
# Modules in python
import math
print(math.sqrt(16))
print(math.pow(2,5))
print(math.pi)
print(math.log10 (100))
print(math.floor(2.3))
import calendar

cal=calendar.month(2026,1)
print(cal)
print(cal.isleap(2026))

