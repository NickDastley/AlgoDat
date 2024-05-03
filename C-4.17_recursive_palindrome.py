def recursive_palindrome(s):
    if len(s) <= 1:
        return True

    first_letter = s[0]
    last_letter = s[-1]

    if first_letter == last_letter:
        rest_of_s = s[1:-1]
        return recursive_palindrome(rest_of_s)
    else:
        return False


print(recursive_palindrome("test"))
print(recursive_palindrome("racecar"))
print(recursive_palindrome("anna"))
print(recursive_palindrome("gohangasalamiimalasagnahog"))