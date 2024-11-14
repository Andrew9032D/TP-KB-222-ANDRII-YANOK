'''2)	Програма конвертування іноземної валюти в українську гривню.
Для отримання актуальних курсів валют необхідно використовувати API НБУ та модуль,
що надає можливість виконувати запити до сторонніх сервісів requests.
Достатня умова роботи – можливість конвертації для трьох іноземних валют EUR, USD, PLN.
Користувачу надається можливість введення кількості та типу валюти, результат роботи програми – конвертоване значення в українських гривнях.'''



import requests

def eurCurr():
    r = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
    eurCurr = 0
    for elem in r.json():
        if elem['cc'] == 'EUR':
            eurCurr = elem['rate']
    return eurCurr

def usdCurr():
    r = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
    usdCurr = 0
    for elem in r.json():
        if elem['cc'] == 'USD':
            usdCurr = elem['rate']
    return usdCurr

def plnCurr():
    r = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
    plnCurr = 0
    for elem in r.json():
        if elem['cc'] == 'PLN':
            plnCurr = elem['rate']
    return plnCurr

value = int(input("Enter the amount: "))

EurCurr = eurCurr()
print(f"EUR to UAH rate: {EurCurr}")

UsdCurr = usdCurr()
print(f"USD to UAH rate: {UsdCurr}")

PlnCurr = plnCurr()
print(f"PLN to UAH rate: {PlnCurr}")

print(f"Result of {value} EUR in UAH = {EurCurr * value}")
print(f"Result of {value} USD in UAH = {UsdCurr * value}")
print(f"Result of {value} PLN in UAH = {PlnCurr * value}")
