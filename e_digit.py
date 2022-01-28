from math import e


def e_with_precision(n):
    """Return euler's number to the n-th decimal place
    :param n: number of decimal places to return
    :type n: int
    :return: euler's number with n decimal places
    :rtype: str
    """
    return '%.*f' % (n, e)

if __name__ == '__main__':
    correct_input = False
    while not correct_input:
        print('Precision must be between 1 and 51')
        precision = int(input('Number of decimal places: '))
        if 51 >= precision > 0:
            correct_input = True
    print(e_with_precision(precision))