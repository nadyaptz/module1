immutable_var=('Nadya', 'Fomina', 2002, 2007, True)
print('Immutable tuple:', immutable_var)
# immutable_var[2]=2000 Ошибка! нельзя изменить элемент кортежа!
mutable_list=['Nadya', 'Fomina', 2002, 2007, True]
mutable_list[2]='October 2002'
mutable_list[3]='June 2007'
mutable_list.append('family')
print('Mutable list:', mutable_list)