dict = {"k1":"v1","k2":
    "v2","k3":
    "v3"}
for key in dict:
    print(key+":",dict[key])

for value in dict.values():
    print(value)

dict["k4"]="v4"
print(dict["k1"])