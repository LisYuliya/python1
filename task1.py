# 1.Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for j in range(2, 11):
    for i in range(2, 6):
        result = i * j
        print(f"{i} x {j} = {result}\t", end="\t")
    print()

print()
for l in range(2, 11):
    for k in range(6, 10):
        result = k * l
        print(f"{k} x {l} = {result}\t", end="\t")
    print()
