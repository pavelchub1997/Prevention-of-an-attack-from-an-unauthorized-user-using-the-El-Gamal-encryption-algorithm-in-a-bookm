import coeff, random, sympy, class_auth
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt

class Coeff(QtWidgets.QMainWindow, coeff.Ui_MainWindow):
    def __init__(self, bool_shit):
        self.bool_shit = bool_shit
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.psh_btn)
        self.pushButton_2.clicked.connect(self.psh_btn_1)
        self.pushButton_3.clicked.connect(self.selected_choise_1)

    def enter_value(self):

        res_list, res_lst = [], []
        res_list.append(int(self.lineEdit.text()))
        res_list.append(int(self.lineEdit_2.text()))
        res_list.append(int(self.lineEdit_3.text()))
        res_lst.append(int(self.lineEdit_4.text()))
        res_lst.append(int(self.lineEdit_5.text()))
        return res_list, res_lst

    def value_prob(self):

        res_buff = []
        buff_list, res_lst = self.enter_value()
        sum_1 = calc_sum(buff_list)
        sum_2 = calc_sum(res_lst)
        res_buff = ins_val(buff_list, 0, sum_1, res_buff)
        res_buff = ins_val(res_lst, len(buff_list), sum_2, res_buff)
        return res_buff

    def psh_btn(self):
        print(self.bool_shit)
        res_list = self.value_prob()
        if self.bool_shit == False: random.shuffle(res_list)
        x = [i for i in range(0, 3)]
        plt.plot(x, res_list[0:3])
        plt.title('Вероятность исхода')
        plt.ylabel('Значение вероятности')
        plt.xlabel('"0" - Победа, "1" - Ничья, "2" - Поражение')
        plt.show()

    def psh_btn_1(self):
        res_list = self.value_prob()
        if self.bool_shit == False: random.shuffle(res_list)
        x = [i for i in range(0, 2)]
        plt.plot(x, res_list[3:5])
        plt.title('Вероятность исхода')
        plt.ylabel('Значение вероятности')
        plt.xlabel('"0" - Забитые голы, "1" - Пропущенные голы')
        plt.show()

    def psh_btn_2(self, res_coeff, index, res_lst):

        print(res_coeff)
        if res_lst[index] == 0:
            coeff = 100
            res_coeff *= coeff
        elif res_lst[index] < 0.25:
            coeff = res_lst[index] * 10
            res_coeff *= coeff
        elif res_lst[index] == 0.25 or (res_lst[index] > 0.25 and res_lst[index] < 0.5):
            coeff = res_lst[index] * 5
            res_coeff *= coeff
        elif res_lst[index] == 0.5 or (res_lst[index] > 0.5 and res_lst[index] < 1):
            coeff = res_lst[index] * 2
            res_coeff *= coeff
        return res_coeff

    def selected_choise_1(self):

        res_lst = self.value_prob()
        res_coeff = float(self.lineEdit_6.text())
        self.lineEdit_6.setText('')
        if self.checkBox.isChecked(): res_coeff = self.psh_btn_2(res_coeff, 0, res_lst)
        if self.checkBox_2.isChecked(): res_coeff = self.psh_btn_2(res_coeff, 1, res_lst)
        if self.checkBox_3.isChecked(): res_coeff = self.psh_btn_2(res_coeff, 2, res_lst)
        if self.checkBox_4.isChecked(): res_coeff = self.psh_btn_2(res_coeff, 3, res_lst)
        if self.checkBox_5.isChecked(): res_coeff = self.psh_btn_2(res_coeff, 4, res_lst)
        if self.bool_shit == False:
            self.lineEdit_6.insert(str(random.randint(100, 1000)*0.01))
            ins_bd(res_lst, res_coeff)
        else: self.lineEdit_6.insert(str(round(res_coeff, 2)))

def calc_sum(lst):
    sum = 0
    for elem in lst:
        sum += elem
    return sum

def ins_val(lst, index, sum, res_buff):
    for elem in lst:
        res_buff.insert(index, round(elem / sum, 2))
        index += 1
    return res_buff

def calc_elem_lst(buff_lst):
    for elem in range(len(buff_lst)): buff_lst[elem] = int(buff_lst[elem] * 100)
    return buff_lst

def cipher(p, q, y, k, m):

    return pow(q, k, p), (pow(y, k) * m)%p

def decryption(a, b, x, p):

    return (b * pow(a, (p - 1 - x)))%p

def gener_key():
    p = sympy.randprime(pow(2, 10), pow(2, 20))
    q = random.randint(1, p - 1)
    x = random.randint(2, p - 2)
    y = pow(q, x, p)
    return p, q, y

def proc_encr(buff_lst):

    res_lst = []
    p, q, y = gener_key()
    k = random.randint(2, p - 2)
    if len(buff_lst) == 1:
        a, b = cipher(p, q, y, k, buff_lst[0])
        return [a, b]
    else:
        for elem in buff_lst:
            a, b = cipher(p, q, y, k, elem)
            res_lst.append([a, b])
        return res_lst

def ins_bd(buff_lst_1, res_coeff):
    buff = int(res_coeff*100)
    buff = proc_encr([buff])
    print(buff)
    buff_lst = calc_elem_lst(buff_lst_1)
    buff_lst = proc_encr(buff_lst)
    print(buff_lst[2][1])
    db = class_auth.con()
    cursor = db.cursor()
    try:
        cursor.execute('insert into val_coeff (val_prob_win_p_1, val_prob_win_p_2, val_prob_nich_p_1, '
                       'val_prob_nich_p_2, val_prob_lose_p_1, val_prob_lose_p_2, val_prob_z_g_p_1, '
                       'val_prob_z_g_p_2, val_prob_pr_g_p_1, val_prob_pr_g_p_2, val_coeff_p_1, val_coeff_p_2) '
                       'values ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' %
                       (buff_lst[0][0], buff_lst[0][1], buff_lst[1][0], buff_lst[1][1], buff_lst[2][0],
                        buff_lst[2][1], buff_lst[3][0], buff_lst[3][1], buff_lst[4][0], buff_lst[4][1], buff[0], buff[1]))
        db.commit()
    except: db.rollback()
    db.close()
