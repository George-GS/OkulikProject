# Есть список цен в виде строк: ["$100", "$200", "$300"]
# Нужно: убрать символ $ и преобразовать в числа
# Используй map

price = ["$100", "$200", "$300"]

# result = []
# def del_dol(lst):
#     for x in lst:
#         x = list(x)
#         x.pop(0)
#         x = ''.join(x)
#         x = int(x)
#         result.append(x)
#     return result
#
# del_dol(price)
# print(result)


def del_dol(x):
    return int(x[1:])

result = map(del_dol, price)
print(list(result))