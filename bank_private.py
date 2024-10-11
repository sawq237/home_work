class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостаточно средств")

    def get_balance(self):
        return self.__balance



account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())

#Код моделирует банковский счет
#Необходимость создания приватного поля нужно для защиты данных
#Метод deposit:
#Принимает параметр amount и добавляет его к балансу, если amount положительный.
#Обновляет приватное поле __balance.
#Метод withdraw:
#Принимает параметр amount и вычитает его из баланса, если amount положительный и не превышает текущий баланс.
#В противном случае выводит сообщение "Недостаточно средств".
#Метод get_balance:
#Возвращает текущее значение баланса, доступное через публичный метод.
