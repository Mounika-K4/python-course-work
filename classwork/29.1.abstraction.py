from abc import ABC, abstractmethod

class Bankaccount(ABC):
    def deposit(self):
        print('you can deposit the amount')
    def checkbalance(self):
        print('ypu can check your balance')

    @abstractmethod
    def withdraw(self):
        pass
    def viewhistory(self):
        print('you can check the history')

class CurrentAccount(Bankaccount):
    def withdraw(self):
        print('You can withdraw Extra amount')

class SavingAccount(Bankaccount):
    def withdraw(self):
        print('You can withdraw the amount')

mouni=CurrentAccount()
haari=SavingAccount()
mouni.checkbalance()
mouni.deposit()
mouni.viewhistory()
mouni.withdraw()
haari.checkbalance()
haari.deposit()
haari.viewhistory()
haari.withdraw()