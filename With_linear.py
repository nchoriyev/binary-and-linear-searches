import random

data = []
for i in range(20):
    data.append(random.randint(1, 100))

print(data)

target = int(input("Target: "))
counter = 0
for i in data:
    counter = counter + 1
    if i == target:
        print(f"Maqsad: {i}")
        print(f"Urinishlar soni: {counter}")
        break
