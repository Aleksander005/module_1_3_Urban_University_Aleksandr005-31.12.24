immutable_var=_tuple_1= (1, 'Urban', 6.0, )
print(immutable_var)
#immutable_var[0]=2 # возможно, используется при основе кода, для минимизации изменений во избежание ошибок и их поиска
mutable_list = [ 'Aleksandr', 'Katy', 'Vika', 'Maru' ]
print(mutable_list) # вывод списка
mutable_list [1] = 'Katerina' # замена в списке
print(mutable_list) # вывод нового списка
mutable_list.extend('Viktoria') # добавление в список каждого символа отдельно
print(mutable_list) # вывод нового списка
mutable_list.extend (['Viktoria']) #  понимаю почему нет изменениц в [] скобках
print(mutable_list)
mutable_list.remove ('Aleksandr') #убрать из списка
print(mutable_list)
print ('Altksandr' in mutable_list) #проверка в списке (True / False)
print ('Altksandr' not in mutable_list) #проверка в списке (True / False)
print(mutable_list[1:3]) # часть списка, последняя цифра не входит в список