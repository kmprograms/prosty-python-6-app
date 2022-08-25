"""
Przygotuj program, która pozwoli z listy liczb całkowitych wybrać te liczby,
które posiadają parzystą sumę cyfr.
"""

from typing import Callable
from dataclasses import dataclass

class NumberOperation:
    @staticmethod
    def sum_digits(n: int) -> int:
        return sum([int(d) for d in str(abs(n))])

@dataclass
class NumbersManager:
    numbers: list[int]

    def get_numbers(self, condition: Callable[[int], bool]) -> 'NumbersManager':
        return NumbersManager([n for n in self.numbers if condition(n)])


def main() -> None:
    nm1 = NumbersManager([23, 12, 11, 46, 13])
    print(nm1)

    nm2 = nm1.get_numbers(lambda x: NumberOperation.sum_digits(x) % 2 == 0)
    print(nm2)

    nm3 = nm1.get_numbers(lambda x: x > 10).get_numbers(lambda x: x % 10 == 2)
    print(nm3)

if __name__ == '__main__':
    main()




