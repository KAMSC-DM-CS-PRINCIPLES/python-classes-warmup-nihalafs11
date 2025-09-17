from bankaccount import BankAccount

def test_bankaccount_initial_balance_zero():
    """Test that account starts with balance 0 by default"""
    account = BankAccount()
    assert account.get_balance() == 0

def test_bankaccount_initial_balance_given():
    """Test that account starts with given balance"""
    account = BankAccount(100)
    assert account.get_balance() == 100

def test_bankaccount_deposit():
    """Test that deposit increases balance"""
    account = BankAccount(50)
    account.deposit(25)
    assert account.get_balance() == 75

def test_bankaccount_multiple_deposits():
    """Test multiple deposits"""
    account = BankAccount(0)
    account.deposit(10)
    account.deposit(20)
    account.deposit(30)
    assert account.get_balance() == 60

def test_bankaccount_withdraw_sufficient_funds():
    """Test withdrawal when sufficient funds are available"""
    account = BankAccount(100)
    account.withdraw(30)
    assert account.get_balance() == 70

def test_bankaccount_withdraw_insufficient_funds():
    """Test withdrawal when insufficient funds"""
    account = BankAccount(50)
    result = account.withdraw(75)
    assert result == "Insufficient Funds"
    assert account.get_balance() == 50

def test_bankaccount_withdraw_exact_balance():
    """Test withdrawal of exact balance"""
    account = BankAccount(100)
    account.withdraw(100)
    assert account.get_balance() == 0

def test_bankaccount_operations_sequence():
    """Test a sequence of operations"""
    account = BankAccount(0)
    account.deposit(100)
    account.withdraw(30)
    account.deposit(20)
    account.withdraw(15)
    assert account.get_balance() == 75
