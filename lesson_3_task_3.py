from Address import Address
from Mailing import Mailing

to_address = Address
from_address = Address
to_address = 124527, "г. Москва", "ул. Пушкина", 15, 346
from_address = 628796, "г. Ростов", "ул. Пупова", 18, 67

sending = Mailing
sending(to_address, from_address, 5200, 1454726551798)

print(
    "Отправление",
    sending.track,
    "из",
    from_address,
    "в",
    to_address,
    ". Стоимость",
    sending.cost,
    "рублей.",
)