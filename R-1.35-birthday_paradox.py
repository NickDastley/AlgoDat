# P-1.35 The birthday paradox says that the probability that two people in a room will have the same birthday
# is more than half, provided n, the number of people in the room,
# is more than 23.
# This property is not really a paradox, but many people find it surprising.
# Design a Python program that can test this paradox by a series of experiments on randomly generated birthdays,
# which test this paradox for n = 5,10,15,20,...,100.
import random


def create_random_birthdays(number_of_persons):
    birthday_list = []
    for i in range(number_of_persons):
        birthday_list.append(random.randint(1, 365))  # both included
    return birthday_list


def has_duplicates(birthday_list):
    for i in range(len(birthday_list)):
        for j in range(i + 1, len(birthday_list)):
            if birthday_list[i] == birthday_list[j]:
                return True
    return False


number_of_persons = 5
while number_of_persons <= 100:
    birthday_list = create_random_birthdays(number_of_persons)
    people_with_same_birthday = has_duplicates(birthday_list)
    print(str(number_of_persons) + ": " + str(people_with_same_birthday))
    #print(str(birthday_list))
    number_of_persons += 5
