"""This is the recursive euclidian algorithm."""
import argparse


def euclid_GCD(a, b):
    """Determine the GCD of two numbers using Euclidian Algorithm."""
    if b == 0:
        return a
    return euclid_GCD(b, a % b)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('operand1',
                        type=int,
                        help='The first number for the GCD operation')
    parser.add_argument('operand2',
                        type=int,
                        help='The second number for the GCD operation')
    operand1 = parser.parse_args().operand1
    operand2 = parser.parse_args().operand2

    gcd = euclid_GCD(operand1, operand2)
  
    print(f'GCD({operand1}, {operand2}) = {gcd}')
