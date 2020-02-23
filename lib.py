import random

def enter_arg():

    print('Введите значения ч/з пробел\n(Количество побед, ничьих, поражений'
          'Количество голов первой команды'
          'Количество голов второй команды)')
    res_buff = list(map(int, input().split(' ')))
    return res_buff

def value_prob():

    res_buff = []
    sum_1, sum_2 = 0, 0
    buff_list = enter_arg()
    for index, elem in enumerate(buff_list):
        if index > 2:
            sum_1 += elem
        else:
            sum_2 += elem
    for index, elem in enumerate(buff_list):
        if index>2:
            res_buff.append(round(elem / sum_1, 2))
        else:
            res_buff.append(round(elem / sum_2, 2))
    print(res_buff)
    return res_buff

def coefficient(elem_list, res_coeff):

    #res_coeff = 1
    if elem_list == 0:
        coeff = 100
        res_coeff *= coeff
    elif elem_list < 0.25:
        coeff = elem_list * 15
        res_coeff *= coeff
    elif elem_list > 0.25 and elem_list < 0.5:
        coeff = elem_list * 7
        res_coeff *= coeff
    elif elem_list > 0.5 and elem_list < 1:
        coeff = elem_list * 3
        res_coeff *= coeff

    return res_coeff

def val_user(res_coeff):

    value_user = int(input('Пользователь, введите значение: '))
    return res_coeff*value_user

def check_enter_val(index, res_coeff, res_buff):

    if res_coeff / coefficient(res_buff[index - 1], res_coeff) == 1:
        print('Бессмысленно ставить на победы обеих команд и ничью')
    else:
        res_coeff *= coefficient(res_buff[index - 1], res_coeff)
        print(res_coeff)
    return res_coeff