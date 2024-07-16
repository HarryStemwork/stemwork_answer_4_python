#values are 1100 652 946 821 955 1024 1155
val = (1100,652,946,821,955,1024,1155)
mean = sum(val) / len(val)
print(f"Mean: {mean}")

var = 0
for v in val:
    var += ((v-mean)**2)
var = var / len(val)
print(f"Variance: {var}")

sd = 0
for v in val:
    sd += ((v-mean)**2)
sd = (sd / len(val)) ** 0.5
#or just like this
#sd = var ** 0.5
print(f"Standard Deviation: {sd}")
