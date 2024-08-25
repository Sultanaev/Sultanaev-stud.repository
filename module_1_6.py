my_dict = {'Аманда': 1962, 'Ибрагим': 1982, 'Чан-Ху': 1987}
print(my_dict)
print(my_dict['Аманда'])
my_dict['Мирослава'] = 1977
print(my_dict['Мирослава'])
my_dict.update({'Мойша': 1990, 'Митхун': 1968})
a = my_dict.pop('Аманда')
print(a)
print(my_dict)

my_set = {4,8,7,4,12,17,7,12}
print(my_set)
my_set.update({24,47})
print(my_set.remove(4))
print(my_set)