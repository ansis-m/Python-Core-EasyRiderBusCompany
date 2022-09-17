# square_list = []
# for i in range(1, 10):
#     if i % 2 == 0:
#         square_list.append(i ** 2)



square_list = [i**2 for i in range(1,10) if not i % 2]
print(square_list)