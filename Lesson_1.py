# num = int(input("Enter a number 0-9: "))
# print(type(num))
#
# while num <= 10:
#     print(num)
#     num += 1

i = 0

while True:
    i += 1
    if i >= 10:
        break
    if i % 2 == 0:
        continue
    print(i)
