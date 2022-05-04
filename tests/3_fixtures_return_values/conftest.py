import random
import math
import pytest

from src.Account import Account

#Из лекции --------------------------------------------------------------

def test_random_value(randome_value_fixture):
    assert randome_value_fixture==20

class Test_Class:
    ##Конструктор
    def __init__(self,mod1,mod2):
        self.mod1 = mod1
        self.mod2 = mod2
    #Метод
    def hello(self,name):
        return  f"Hello, {name}"

@pytest.fixture
def fixture_return_class():
    return Test_Class(mod1=random,mod2=math)

#Из лекции end--------------------------------------------------------------

@pytest.fixture
def empty_account():
    return Account("Test", 0)


@pytest.fixture
def activated_account():
    return Account("Test", 100, True)

@pytest.fixture
def randome_value_fixture():
    return random.randint(1,100)
