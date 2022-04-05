from datetime import datetime
import os


def isdecimal(num):
    num = str(num).replace(',', '.') 
    try:
        num = float(num)
    except ValueError:
        return False 
    return True 

def date_verification(date: str):
    try:
        datetime.strptime(date, '%d/%m/%Y')
    except ValueError:
        return False 
    return True


def installments_verification(installments: str):
    try:
        paid, total = [int(val) for val in installments.split('/')]
        assert paid <= total
    except:
        return False
    return True


def verification(function, information_msg, error_msg):
    while True:
        answer = str(input(information_msg))
        
        if function(answer):
            return answer
        
        print(error_msg)
        os.system('pause')


def canblank(func):
    def verification(verified):
        if verified.replace(' ', '') == '':
            return True 
        return func(verified)
    return verification


def proceed(options, information_msg):
    while True:
        answer = input('\n' + information_msg)
        if answer in options:
            return answer

