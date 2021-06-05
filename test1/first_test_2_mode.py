number_list = [int(x) for x in input().split()]
frequency_dict = {}

for number in number_list:
    if number in frequency_dict:
        frequency_dict.update({number: frequency_dict[number] + 1})
    else:
        frequency_dict.update({number: 1})

maximum = float('-inf')
for k in frequency_dict:
    if frequency_dict[k] > maximum:
        maximum = frequency_dict[k]
list_number = []
for k in frequency_dict:
    if frequency_dict[k] == maximum:
        list_number.append(str(k))
list_number.sort()
for k in list_number:
    print(k, end=' ')
