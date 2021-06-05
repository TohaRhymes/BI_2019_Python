number_list = [int(x) for x in input().split()]
number_list.sort()
if len(number_list) % 2 == 1:
    print(str(number_list[len(number_list) // 2]))
else:
    print(str((number_list[len(number_list) // 2 - 1] + number_list[len(number_list) // 2]) / 2))
