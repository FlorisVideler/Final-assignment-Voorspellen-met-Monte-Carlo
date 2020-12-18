import numpy as np
import time


class NumpyRandomly:
    def __init__(self, seed: int = None):
        """
        Initiator for the Numpy random generator

        :param seed: int
            Start value for the algorithm
        """
        if seed is not None:
            np.random.seed(seed)
        self.name = 'Numpy rng'

    def randomly(self, right: int = 100, left: int = 0):
        """
        Makes the random number using Numpy

        :param right: int
            Max value
        :param left: int
            Min value
        :return: int
            The random number
        """
        return int(np.floor(np.random.rand() * right)) + left


class MiddleSquare:
    def __init__(self, seed: int = int(time.perf_counter_ns() / 1000)):
        """
        Initiator for the MiddleSquare random generator

        :param seed: int
            Start value for the algorithm
        """
        self.seed = seed
        print('seed:', seed)
        self.name = 'middle square rng'

    def randomly(self, right: int = 100, left: int = 0) -> int:
        """
        Generate a random number using the middle square algorithm

        :param right: int
            Max value
        :param left: int
            Min value
        :return: int
            The random number
        """
        next_num = abs(np.square(self.seed))
        next_num_str = str(next_num)
        # find mid
        lleft = True
        while len(next_num_str) > len(str(self.seed)):
            if lleft:
                next_num_str = next_num_str[1:]
                lleft = False
            else:
                next_num_str = next_num_str[:-1]
                lleft = True
        self.seed = int(np.floor(int(next_num_str) / int('1' + '0' * len(str(self.seed))) * right + left))
        return self.seed


class LCG:
    def __init__(self, seed: int = int(time.perf_counter_ns() / 1000), a: int = 829, c: int = 3329, m: int = 5437):
        """
        Initiator for the the LCG algorithm

        :param seed: int
            Start value for the algorithm
        :param a: int
        :param c: int
        :param m: int
        """
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

        print('seed:', seed)
        self.name = 'LCG rng'

    def randomly(self, right: int = 100, left: int = 0) -> int:
        """
        Generate a random number using the LCG algorithm

        :param right: int
            Max value
        :param left: int
            Min value
        :return: int
            The random number
        """
        next_num = (self.a * self.seed + self.c) % self.m
        next_num_str = str(next_num)
        self.seed = int(np.floor(int(next_num_str) / int('1' + '0' * len(str(self.m))) * right + left))
        return self.seed


class Mersenne:
    def __init__(self, seed: int = 5489):
        """
        Initiator for the the Mersenne twister algorithm

        :param seed: int
            Start value for the algorithm
        """
        self.name = 'Mersenne twister'
        self.seed = seed
        self.w = 32
        self.r = 31
        self.n = 624
        self.m = 397
        self.u = 11
        self.s = 7
        self.t = 15
        self.l = 18
        self.a = 0x9908b0df
        self.b = 0x9d2c5680
        self.c = 0xefc60000
        self.f = 0x6c078965
        self.compress_mask = 0xffffffff
        self.Z = [seed]
        self.random_numbers = None

        self.upmask = int('10000000000000000000000000000000', 2)
        self.lowmask = int('01111111111111111111111111111111', 2)
        self.init_seed()
        self.twist()

    def init_seed(self):
        """
        Initiator for the first block of the Mersenne twister
        """
        for i in range(self.n - 1):
            self.Z.append((self.f * (self.Z[i] ^ (self.Z[i] >> (self.w - 2))) + i) & self.compress_mask)

    def twist(self) -> list:
        """
        Generates block of random numbers using the Mersenne twister

        :return: list
            A list of random numbers
        """
        new_block = []
        mid_index = self.m
        first_index = 0
        second_index = 1

        while len(new_block) < self.n:
            mid_b = self.Z[mid_index]
            first_b = self.Z[first_index]
            second_b = self.Z[second_index]

            mid_index += 1
            first_index += 1
            second_index += 1
            if mid_index == self.n:
                mid_index = 0
            if second_index == self.n:
                second_index = 0

            concat = (first_b & self.upmask) | (second_b & self.lowmask)
            least_sig = concat & 1
            if least_sig == 0:
                out = concat >> 1
            else:
                out = (concat >> 1) ^ self.a
            new_block.append(mid_b ^ out)

        twisted_block = []
        for i in new_block:
            y = i
            y = y ^ (y >> self.u)
            y = y ^ ((y << self.s) & self.b)
            y = y ^ ((y << self.t) & self.c)
            y = y ^ (y >> self.l)
            twisted_block.append(y)
        self.random_numbers = twisted_block
        self.Z = twisted_block.copy()
        return twisted_block

    def randomly(self, right: int = 100, left: int = 0) -> int:
        """
        Generate a random number using the Mersenne twister algorithm

        :param right: int
            Max value
        :param left: int
            Min value
        :return: int
            The random number
        """
        rn = self.random_numbers[0]
        self.random_numbers.pop(0)
        if len(self.random_numbers) == 0:
            self.twist()
        return round(rn / int('1' + '0' * 10) * right + left)

