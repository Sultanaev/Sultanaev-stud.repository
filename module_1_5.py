immutable_var = 12, 32, 'Жоккей', True
print(immutable_var)
# нельзя изменить значение элементов в кортеже, т.к кортеж это неизменяемая коллекция,
# но можно изменить значение элемента СПИСКА, котрый находится внутри кортежа

mutable_list = [12, 32, 'Жоккей',True]
print(mutable_list)
mutable_list[0] = 6
mutable_list[3] = False
print(mutable_list)