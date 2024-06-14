# erster Versuch, man darf nicht *, / verwenden
def is_even(number):
    couldBeEven = True
    for i in range(number):
        couldBeEven = not couldBeEven

    return couldBeEven

def is_even_from_Tutor(number):
    # wenn der erste Bit 0 ist,
    # dann ist die Zahl gerade
    return number&1 == 0

print(is_even(6))