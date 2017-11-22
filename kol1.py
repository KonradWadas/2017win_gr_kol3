#!/usr/bin/python
import pickle

class Bank:
    '''create a bank'''

    def __init__(self, bank_name):
        self.name = bank_name
        self.clients = {}

    def __str__(self):
        return(
                'Bank name: %s \nClients:\n%s' % (
                    str(self.name),
                    '\n'.join([str(self.clients[i]) for i in self.clients])
                    )
                )

    def add_client(self, client_name, money):
        self.clients[client_name] = Client(client_name, money)

    def transfer(self, sender, receiver, amount):
        self.clients[sender].take_money(amount)
        self.clients[receiver].give_money(amount)

class Client:
    '''create a client'''

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __str__(self):
        return ('Name: %s \nBalance: %s' % (str(self.name), str(self.money)))

    def give_money(self, amount):
        self.money += amount

    def take_money(self, amount):
        self.money -= amount

class Interface:
    '''keeps tracks of all the banks, allows for money transfers between banks'''

    def __init__(self):
        self.banks = {} 
        self.transfers_history = [] 

    def list_banks(self):
        return '\n'.join(self.banks.keys())

    def create_bank(self, name):
        self.banks[name] = Bank(name)

    def bank_info(self, name):
        return self.banks[name]
    
    def add_client(self, bank_name, client_name, money):
        self.banks[bank_name].add_client(client_name, money)

    def transfer(self, bank1, client1, bank2, client2,  amount):
        self.banks[bank1].clients[client1].take_money(amount)
        self.banks[bank2].clients[client2].give_money(amount)
        self.transfers_history.append("From %s in bank %s to %s in bank %s, amount: %s" %
                                (client1, bank1, client2, bank2, str(amount)))

    def save(self):
        with open('bank_data.pkl', 'wb') as output:
            pickle.dump(self.__dict__, output, pickle.HIGHEST_PROTOCOL)

    def load(self):
        with open('bank_data.pkl', 'rb') as input:
            tmp = pickle.load(input)                     
            self.__dict__.update(tmp)
    def show_history(self):
        return '\n'.join(self.transfers_history)

def list_banks():
    print(interface.list_banks())
    
def create_bank():
    name = raw_input("Type the name of the new bank: ")
    interface.create_bank(name)

def add_client():
    bank_name = raw_input("Enter the name of the bank in which you want to create an account: ")
    name = raw_input("Type the name of the client: ")
    money_amount = raw_input("Type the amount of money the client has: ")
    interface.add_client(bank_name, name, float(money_amount))

def bank_info():
    bank_name = raw_input("Enter the name of the bank: ")
    print(interface.bank_info(bank_name))


def transfer():
    senders_bank = raw_input("Type the name of senders bank: ")
    sender = raw_input("Type the name of the sender: ")
    receivers_bank = raw_input("Type the name of receivers bank: ")
    receiver = raw_input("Type the name of the receiver: ")
    amount = raw_input("Enter the amount of money you want to transfer: ")
    interface.transfer(senders_bank, sender, receivers_bank, receiver, float(amount))

def dump():
    interface.save()

def load():
    interface.load()

def show_history():
    print(interface.show_history())

def wrong_choice():
    print "No such option"


def main():
    menu_options = {'0': list_banks,
                    '1': create_bank,
                    '2': add_client,
                    '3': transfer,
                    '4': bank_info,
                    '5': dump,
                    '6': load,
                    '7': show_history}
                            
    while True:
        print(  "\n0) List banks\n"
                "1) Create a bank\n"
                "2) Create an account\n"
                "3) Transfer money\n"
                "4) Give informations about the bank and its clients\n"
                "5) Dump data\n"
                "6) Load data\n"
                "7) Show transfers history\n"
                "Type quit to exit the program\n")
        choice = raw_input("Choose an action by typing its number: ")
        if "quit" == choice:
            return
        ToDo = menu_options.get(choice, wrong_choice)
        try:
            ToDo() 
        except (KeyError, ValueError):
            print("You've made a mistake, try again")


if __name__ == "__main__":
    #testing:
    test_interface = Interface()
    test_interface.create_bank('PKO')
    test_interface.add_client('PKO','Adam Kowalski',1000)
    test_interface.add_client('PKO','Ewa Kowalska',5000)
    print(test_interface.bank_info('PKO'))
    test_interface.transfer('PKO', 'Adam Kowalski', 'PKO', 'Ewa Kowalska', 500)
    print("###after transfer")
    print(test_interface.bank_info('PKO'))
    test_interface.save()
    del test_interface
    loaded_interface = Interface()
    loaded_interface.load()
    loaded_interface.list_banks()
    print("###after loading from file")
    print(loaded_interface.bank_info('PKO'))
    print("###list banks")
    print(loaded_interface.list_banks())
    print("###show history")
    print(loaded_interface.show_history())
    #end of testing
    interface = Interface() 
    main()
    

