# Copyright 2016-2023 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Pythagorean triple module

* *Pythagorian* triple are three integers `a, b, c` where `a**2 + b**2 = c**2`
* such a triple is primative when `a, b, c > 0` and `gcd(a, b, c) = 1`
* geometrically `a, b, c` represent the sides of a right triangle
"""

from __future__ import annotations

from typing import Callable, Iterator, Tuple
from grscheller.boring_math import gcd, iSqrt

__all__ = ['Pythag3']

class Pythag3():
    """Class supporting the generation of primative Pythagorean triples"""
    def __init__(self, last_square: int=500):
        last_h = last_square if last_square % 2 == 1 else last_square - 1
        if last_h < 5:
            last_h = 5

        # Create perfect square lookup dictionary
        self.squares = {h*h: h for h in range(5, last_h + 1, 2)}
        self.last_h = last_h

    def extend_squares(self, last_to_square):
        """Extend self.squares, the perfect square lookup table"""
        last_h = last_to_square if last_to_square % 2 == 1 else last_to_square - 1
        if last_h > self.last_h:
            # Extend perfect square lookup dictionary
            for h in range(self.last_h + 2, last_h + 1, 2):
                self.squares[h*h] = h
            self.last_h = last_h

    @staticmethod
    def cap_sides(a_max: int, max: int=0) -> Tuple(int, Callable[[int], int], int):
        """Returns capped max values for sides a,b,c"""
        a_cap = 2 if a_max < 3 else a_max

        b_final = lambda a: (a**2 - 1) // 2  # theoretically, given side a there are no
        if max < 1:                          # more triples beyond this value for side b
            b_cap = b_final
        else:
            cap = 4 if max < 5 else max 
            if cap < a_cap + 2:
                a_cap = cap - 2
            b_cap = lambda a: min(b_final(a), iSqrt(cap**2 - a**2))

        c_cap = iSqrt(a_cap**2 + b_cap(a_cap)**2) + 1

        return a_cap, b_cap, c_cap

    def triples(self, a_start: int=3, a_max: int=3, max: int=0) -> Iterator:
        """Returns an iterator of all possible primative pythagorean triples

        * `(a, b, c)` where `a_start <= a <= a_max` and `0 < a < b < c < max`
        * for `max = 0` all theoretically possible *Pythagorean* triples are generated
        """
        a_init = 3 if a_start < 3 else a_start
        a_cap, b_cap, c_cap = self.cap_sides(a_max, max)
        self.extend_squares(c_cap)

        # Calculate Pythagorean triples
        for side_a in range(a_init, a_cap + 1):
            for side_b in range(side_a + 1, b_cap(side_a) + 1, 2):
                csq = side_a**2 + side_b**2
                if csq in self.squares:
                    if gcd(side_a, side_b) == 1:
                        yield side_a, side_b, self.squares[csq]
