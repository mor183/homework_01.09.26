import pytest

from string_utils import StringUtils

string_util = StringUtils()
#TC 1: Тестирование функциональности "capitalize"
@pytest.mark.parametrize('string, result', [
    #Позитивные проверки:
    ("sergey", "Sergey"),
    ("seRgey", "Sergey"),
    ("mister Sergey", "Mister sergey"),
    ("ser'Gey", "Ser'gey"),
    ("sergey1", "Sergey1"),
    ("sergey-1", "Sergey-1"),
    #Негативные проверки:
    ("", ""),
    ("Sergey", "Sergey"),
    ("SERGEY", "Sergey"), 
    ("123sergey", "123sergey"), 
    ("  leading space", "  leading space"),  
    ("trailing space  ", "Trailing space  ") 
])

def test_capitalize(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.capitalize(string)
    print(f"Actual result: {res}")
    assert res == result

#TC 2: Тестирование функциональности "trim"
@pytest.mark.parametrize('string, result', [
    #Позитивыне проверки
    ("  abc", "abc"),
    ("  ABC", "ABC"),
    (  "123", "123"),
    ("  /abc", "/abc"),
    ("   ABC   ", "ABC   "),
    #Негативные проверки
    ("", ""),
    ("Py ton", "Py ton"),
    ("fish","fish"),
    ("one  ", "one  ")
])
def test_trim (string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.trim(string)
    print(f"Actual result: {res}")
    assert res == result

#T C 3: Тестирование функциональности "contains"
@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные проверки:
    ("", "", True),
    ("Sergey", "S", True),
    ("Sergey", "r", True),
    ("Sergey", "y", True),
    ("123", "2", True),
    ("ARM", "R", True),
    #Негативные проверки:
    ("Sergey", "s", False),
    ("sergey", "S", False),
    ("Sergey", "w", False),
    ("world", "?", False),
    ("world", "word", False)
])

def test_contains(string, symbol, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Inputed symbol: {symbol}")
    print(f"Expected result: {result}")
    res = string_util.contains(string, symbol)
    print(f"Actual result: {res}")
    assert res == result

#TC 4: Тестирование функциональности "delete_symbol"
@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные проверки:
    ("Sergey", "S", "ergey"),
    ("Sergey", "erg", "Sey"),
    ("Sergey", "e", "Srgy"),
    ("1234", "2", "134"),
    ("Sergey!", "!", "Sergey"),
    #Негативные проверки:
    ("", "", ""),
    ("Sergey", "", "Sergey"),
    ("", "v", ""),
    ("Sergey", "w", "Sergey")
    ])

def test_delete_symbol(string, symbol, result):
    string_util = StringUtils()
    res = string_util.delete_symbol(string, symbol)
    assert res == result