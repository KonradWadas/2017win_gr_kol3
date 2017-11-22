import unittest
import kol1

# piotrkukielka


class ClientTest(unittest.TestCase):

    def setUp(self):
        self.client = kol1.Client('Andrzej',1000)

    def test_init(self):
        self.assertEquals(self.client.name,'Andrzej')
        self.assertEquals(self.client.money, 1000)

    def test_give(self):
        self.client.give_money(100)
        self.assertEquals(self.client.money, 1100)

    def test_take(self):
        self.client.take_money(100)
        self.assertEquals(self.client.money, 900)

    def test_str(self):
        self.assertEquals(str(self.client), 'Name: Andrzej \nBalance: 1000')

class BankTest(unittest.TestCase):

    def setUp(self):
        self.bank = kol1.Bank('test_bank')

    def test_init(self):
        self.assertEquals(self.bank.name,'test_bank')

    def test_add_client(self):
        self.bank.add_client("Adam",1000)
        self.assertEquals(self.bank.clients['Adam'].money,1000)
        self.assertEquals(self.bank.clients['Adam'].name, "Adam")

    def test_transfer(self):
        self.bank.add_client("Adam",1000)
        self.bank.add_client("Jacek", 1000)
        self.bank.transfer("Adam","Jacek",100)
        self.assertEquals(self.bank.clients['Adam'].money,900)
        self.assertEquals(self.bank.clients['Jacek'].money,1100)

    def test_str(self):
        self.assertEquals(str(self.bank), 'Bank name: test_bank \nClients:\n')