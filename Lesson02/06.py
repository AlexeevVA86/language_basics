my_struct_list = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "упак."})
]

my_result_dict = {}

for structure in my_struct_list:
    struct_number, struct_info_dict = structure
    for key, value in struct_info_dict.items():
        value_list = my_result_dict.get(key, [])
        if value not in value_list:
            value_list.append(value)
        my_result_dict[key] = value_list

print(my_result_dict)
