#словарь
my_dict= {'Max': 1958 , 'Sasha': 1978, 'Lena': 1997, 'Alex': 1999} #словарь
print(my_dict)
print (my_dict ['Max']) # обращение к конкретному значению через список
print (my_dict.get('Max')) # иной способ обращения
print (my_dict.get('Misha')) # поиск отсутствующего значения
print (my_dict.get('Misha', "такого значения нет!")) # поиск отсутствующего значения с пояснением вместо None
my_dict.update ({'Misha': 2000, 'Murad': 2001}) #добавление в список
print (my_dict) # список расширеный
my_dict['Егор']= 2002 # добваление ранее отсутсвующего значения в словарь (НЕ РАЗОБРАЛСЯ можно ли два значения добвать , напрмер ['Misha'] = 2005
print (my_dict)
del my_dict ['Alex'] # удаление значения по ключу
print (my_dict) # вывод ранее отсутсвующего
my_dict.pop ('Murad') # даление значения методом pop
print (my_dict) # вывод ранее отсутсвующего

# множества
my_set= {1,1, 'set' , 'set', 1.1 , 1.1}
print (my_set)
(my_set.add(7.62,)) #('2'))) # добавляется только один элемент , разобраться
print (my_set)
(my_set.add((7.62, 8.88))) # добавление кортежа
(my_set.discard(1)) #удаление элемента
print (my_set) #вывод; можно ли убрать "None" МОЖНО если удалить print перед командой изменения
