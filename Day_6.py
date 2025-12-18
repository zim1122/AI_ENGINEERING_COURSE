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
