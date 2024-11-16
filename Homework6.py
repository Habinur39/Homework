#2. Организуйте программу:
my_string = input('Доброго времени суток, как Вас зовут? ')
print(len(my_string))

#3. Работа с методами строк:
#1
my_string_upper = input('Доброго времени суток, как Вас зовут? ')
print('очень приятно ', my_string_upper .upper())
#2
my_string_lower = input('Напиши что-то капсом: ')
print('опа, буковки маленькие: ', my_string_lower .lower())
#3
my_string_no = input('Напиши несколько слов (Пример: дерево, собака, дом, огород): ')
print('Оп, а пробелов нет :)', my_string_no .replace(' ',''))
#4
print('Первая буква Твоего имени это: ' , my_string[0])
#5
print('А последняя: ' , my_string[-1])
