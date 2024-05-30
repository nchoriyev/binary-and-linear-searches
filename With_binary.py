import random

data = [random.randint(1, 100) for i in range(20)]
data.sort()
print(f"data: {data}")

def binary_search(data, target):
    low = 0
    high = len(data) - 1
    s = 0

    while low <= high:
        s += 1
        mid = (low + high) // 2
        n = data[mid]

        if n == target:
            return mid, s
        elif n > target:
            high = mid - 1
        else:
            low = mid + 1

    return None, s


target = int(input("Target: "))
target2, attempts = binary_search(data, target)

if target2 is not None:
    print(f"""
        Maqsad: {target}
        Urinishlar soni: {attempts}
    """)
else:
    print(f"""
        Maqsad topilmadi!
        Urinishlar soni: {attempts}
    """)


