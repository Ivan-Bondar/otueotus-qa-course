# Создание тестовых файлов
def test_one():
    print(" >>> I'm test one!")
    assert 2 + 2 == 4


# Так тоже можно, но не нужно и с модулем не заработает
def test_wo():
    assert "Here" == "Where?"


# Создание тестовых классов
class TestClass:

    def test_one(self):
        list_to_test1 = []
        list_to_test2 = []
        assert list_to_test1 is list_to_test2

    def test_two(self):
        print("I'm test 4")
        assert 1 is 1
