
def test_the_class(fixture_return_class):
    assert fixture_return_class.mod2.pow(2,3) ==8
    assert fixture_return_class.mod1.choice(['a','b','c']) =='a'


def test_the_class2(fixture_return_class):
    assert fixture_return_class.hello('Vasya')=='Hello, Vova'




def test_account_not_activated_by_default(empty_account):
    assert not empty_account.activated


def test_account_deposit(empty_account):
    empty_account.deposit(100)
    assert empty_account.balance == 100


def test_not_activated_account_cant_transfer(empty_account, activated_account):
    empty_account.deposit(100)
    balance_before_transfer = activated_account.balance
    operation_result = empty_account.transfer(activated_account, 100)
    assert operation_result is None
    assert activated_account.balance == balance_before_transfer, "Баланс не должен измениться"
