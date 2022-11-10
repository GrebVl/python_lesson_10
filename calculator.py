import telebot.types
from telebot import TeleBot
from emoji import emojize
import telebot_token as t_t
import lst_sorting as l_s
import result as r
import logger as log

bot = TeleBot(t_t.telebot_token())
print(f'Запущин {emojize(":grinning_face:")}')


@bot.message_handler(commands=['help'])
def help_command(msg: telebot.types.Message):
    log.loogger_do(msg)
    bot.send_message(chat_id=msg.from_user.id, text="/help - Выводит все команды программы\n"
                                                    "/log - скачить фаил с историей операций\n"
                                                    "/sum - команда сложения 2 2i 3 4i == 5 + 6i\n"
                                                    "/diff - команда разности 2 2i 3 4i == -1 - 2i\n"
                                                    "/div - команда деления 2 2i 3 4i == 0.666667 + 0.5i\n"
                                                    "/mult - команда умнажения 2 2i 3 4i == 6 + 8i\n"
                                                    "калькулятор не работает с комплексными числами разной степени и разными переменными\n"
                                                    "даныые(числа) указываются через пробел: пример 2 2i 3 4i или 4i2 2 2i2 3")


@bot.message_handler(commands=['sum'])
def sum_command(msg: telebot.types.Message):
    log.loogger_do(msg)
    bot.send_message(chat_id=msg.from_user.id, text="Введите числа через пробел")
    bot.register_next_step_handler(callback=sum_items, message=msg)

def sum_items(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=summation(msg.text))

def summation(msg):
    plus = '+'
    msg = l_s.list_replace(msg)
    list_us = msg
    list_ = list_us.split()
    numbers_lst = l_s.list_nums(list_)
    complex_lst = l_s.list_complex(list_)
    sum_num = l_s.process_nums(numbers_lst, plus)
    sum_complex = l_s.process_complex(complex_lst, plus)
    res = r.resukt(sum_num, sum_complex)
    log.logger(msg, 'summation', res)
    return res


@bot.message_handler(commands=['diff'])
def diff_command(msg: telebot.types.Message):
    log.loogger_do(msg)
    bot.send_message(chat_id=msg.from_user.id, text="Введите числа через пробел")
    bot.register_next_step_handler(callback=diff_items, message=msg)

def diff_items(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=difference(msg.text))

def difference(msg):
    minus = '-'
    msg = l_s.list_replace(msg)
    list_us = msg
    list_ = list_us.split()
    numbers_lst = l_s.list_nums(list_)
    complex_lst = l_s.list_complex(list_)
    diff_num = l_s.process_nums(numbers_lst, minus)
    diff_complex = l_s.process_complex(complex_lst, minus)
    res = r.resukt(diff_num, diff_complex)
    log.logger(msg, 'difference', res)
    return res


@bot.message_handler(commands=['div'])
def div_command(msg: telebot.types.Message):
    log.loogger_do(msg)
    bot.send_message(chat_id=msg.from_user.id, text="Введите числа через пробел")
    bot.register_next_step_handler(callback=div_items, message=msg)

def div_items(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=division(msg.text))

def division(msg):
    divide = '/'
    msg = l_s.list_replace(msg)
    list_us = msg
    list_ = list_us.split()
    numbers_lst = l_s.list_nums(list_)
    complex_lst = l_s.list_complex(list_)
    div_num = l_s.process_nums(numbers_lst, divide)
    div_complex = l_s.process_complex(complex_lst, divide)
    res = r.resukt(div_num, div_complex)
    log.logger(msg, 'division', res)
    return res


@bot.message_handler(commands=['mult'])
def mult_command(msg: telebot.types.Message):
    log.loogger_do(msg)
    bot.send_message(chat_id=msg.from_user.id, text="Введите числа через пробел")
    bot.register_next_step_handler(callback=mult_items, message=msg)

def mult_items(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=multiplication(msg.text))

def multiplication(msg):
    mult = '*'
    msg = l_s.list_replace(msg)
    list_us = msg
    list_ = list_us.split()
    numbers_lst = l_s.list_nums(list_)
    complex_lst = l_s.list_complex(list_)
    mult_num = l_s.process_nums(numbers_lst, mult)
    mult_complex = l_s.process_complex(complex_lst, mult)
    res = r.resukt(mult_num, mult_complex)
    log.logger(msg, 'multiplication', res)
    return res


@bot.message_handler(commands=['log'])
def log_command(msg: telebot.types.Message):
    log.loogger_do(msg)
    bot.send_message(chat_id=msg.from_user.id, text='logg')
    bot.send_document(chat_id=msg.from_user.id, document=open('log.txt', 'rb'))

@bot.message_handler()
def log_command(msg: telebot.types.Message):
    log.loogger_do(msg)
    bot.send_message(chat_id=msg.from_user.id, text='Введите команду /help')

bot.polling()