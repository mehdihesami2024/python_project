def is_happy(n):
    """ A happy numbers is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum of the
    squares of its digits, and repeat the process until the number equals
    1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

    :param n:input number
    :return: is True if n is_happy , otherwise False
    
    """

    seen_number = set()
    while (n != 1) and (n not in  seen_number):
        seen_number.add(n)
        n = sum([int(i)**2 for i in str(n)])

    return n == 1


if __name__ =="__main__":
    n = int(input("pleas enter a number: "))
    assert is_happy(n) is True, (f'{n} not is happy')
            
