
# Номер элемента
n = "311"
parking = ["-", "-", "132", "155", "-", "521", "311", "-", "555", "839"]

park = None
p1 = 0

while park == None and p1 < len(parking):
    if parking[p1] == n:
        park = p1
    p1 += 1

if park != None:
    print(f"Автомобиль стоит на {park} месте.")
else:
    print("Автомобиля на стоянке нет.")

for i in range(len(parking)):
    if parking[i] == n:
        park = i

if park != None:
    print(f"Автомобиль стоит на {park} месте.")
else:
    print("Автомобиля на стоянке нет.")




