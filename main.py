# 1
'''
def is_alive(health):
    if health <= 0:
        return False
    else:
        return True

print(is_alive(int(input())))
'''

# 2
'''
def season_events(number_of_month):
    moth_name = ''
    moth_discription = ''

    if number_of_month > 0 and number_of_month <= 12:
        if number_of_month == 1:
            moth_name = 'январе'
        elif number_of_month == 2:
            moth_name = 'феврале'
        elif number_of_month == 3:
            moth_name = 'марте'
        elif number_of_month == 4:
            moth_name = 'апреле'
        elif number_of_month == 5:
            moth_name = 'мае'
        elif number_of_month == 6:
            moth_name = 'июне'
        elif number_of_month == 7:
            moth_name = 'июле'
        elif number_of_month == 8:
            moth_name = 'августе'
        elif number_of_month == 9:
            moth_name = 'сентябре'
        elif number_of_month == 10:
            moth_name = 'октябре'
        elif number_of_month == 11:
            moth_name = 'ноябре'
        elif number_of_month == 12:
            moth_name = 'декабре'

        if number_of_month == 1 or number_of_month == 2 or number_of_month == 12:
            moth_discription = 'За окном падал белый снег'
        elif number_of_month >= 3 and number_of_month <= 5:
            moth_discription = 'Птицы пели прекрасные песни'
        elif number_of_month >= 6 and number_of_month <= 8:
            moth_discription = 'Солнце светило ярче чем когда-либо'
        elif number_of_month >= 9 and number_of_month <= 11:
            moth_discription = 'Урожай был невероятным'

        return 'Вы родились в ' + moth_name + '. ' + moth_discription

    else:
        return 'Такого месяца нет!'

print(season_events(int(input('Введите месяц в котором родились (Число): '))))
'''

# 3
'''
def check_pass(pswd):
    err = ''

    condition_lenght = False
    condition_up_letter = False
    condition_down_letter = False
    condition_number = False
    condition_special_symbols = False

    text_condition_lenght = 'Пароль имеет не восемь символов.'
    text_condition_up_letter = 'Пароль не содержит заглавные буквы.'
    text_condition_down_letter = 'Пароль не содержит маленькие буквы.'
    text_condition_number = 'Пароль не содержит цифры.'
    text_condition_special_symbols = 'Пароль не содержит специальные символы.'

    global_condition_password = 'Пароль не идеален!'

    if len(pswd) == 8:
        condition_lenght = True

    for i in pswd:
        if pswd.upper():
            condition_up_letter = True
        if pswd.lower():
            condition_down_letter = True
        if pswd.isdigit:
            condition_number = True

    if pswd.count('*') > 0 or pswd.count('-') > 0 or pswd.count('#') > 0:
        condition_special_symbols = True

    if condition_lenght:
        text_condition_lenght = 'Пароль содержит восемь символов.'
    if condition_up_letter:
        text_condition_up_letter = 'Пароль содержит заглавные буквы.'
    if condition_down_letter:
        text_condition_down_letter = 'Пароль содержит маленькие буквы.'
    if condition_number:
        text_condition_number = 'Пароль содержит цифры.'
    if condition_special_symbols:
        text_condition_special_symbols = 'Пароль содержит специальные символы.'

    if condition_lenght and condition_up_letter and condition_down_letter and condition_number and condition_special_symbols:
        global_condition_password = 'Пароль идеальный!'

    err = ('\n' + text_condition_lenght + '\n' + text_condition_up_letter + '\n' + text_condition_down_letter + '\n' + text_condition_number + '\n'
           + text_condition_special_symbols) + '\n'+'\n' + global_condition_password

    return err


print('Пароль должен быть восемь символов.')
print('Пароль должен содержать заглавные и строчные буквы, числа, а также символы "*-#".')
password = str(input('Введите пароль: '))

print(check_pass(password))
'''

# 4
'''
def is_divisible_by_6(number):

    number_str = str(number)
    len_str_number = len(number_str)
    summ = 0

    for i in range(0, len_str_number):
        summ += int(number_str[i])

    if number != 0 and number % 2 == 0 and summ % 3 == 0:
        return 'Число '+ str(number) +' делится на 6'
    else:
        return 'Число '+ str(number) +' неделимо на 6'

a = int(input('Введите число: '))

print(is_divisible_by_6(a))
'''

# 5
'''
def search_substr(subst, st):

    subst_transform = subst.upper()
    st_transform = st.upper()
    text_repeat = st_transform.count(subst_transform)

    if text_repeat != 0:
        return 'Есть контакт!'
    else:
        return 'Мимо!'

string = input('Введите строку: ')
sub_string = input('Введите какой элемент нужно найти в строке: ')

print(search_substr(sub_string, string))
'''

# 6

# сколько успел