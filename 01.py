
zrp = [22000, 15000, 19500, 24000, 20000, 12365, 23000]

count = 0
for i in zrp:
    if i < 20000:
        count += 1

print(f"Работников, получающих меньше 20000: {count} чел.")

