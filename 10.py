# Сдвиг списка

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(keys)
print(f"Видимые кнопки: {keys[0:5]}")
print("Сдвигаем...")

# Сдвиг влево
tmp = keys[0]
for i in range(len(keys) - 1):
    keys[i] = keys[i + 1]
keys[i + 1] = tmp
print(keys)
print(f"Видимые кнопки: {keys[0:5]}")

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Сдвиг в право
tmp = keys[len(keys) - 1]
for i in range(len(keys) - 1, 0, -1):
    keys[i] = keys[i - 1]
keys[0] = tmp
print(keys)
print(f"Видимые кнопки: {keys[0:5]}")

