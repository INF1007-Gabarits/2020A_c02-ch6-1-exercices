#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	return [max(elem) for elem in numbers]

def join_integers(numbers):
	return int("".join([str(elem) for elem in numbers]))

def generate_prime_numbers(limit):
	primes = []
	numbers = [i for i in range(2, limit)]
	while len(numbers) != 0:
		primes.append(numbers[0])
		numbers = [elem for elem in numbers if elem % numbers[0] != 0]
	return primes

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	return [
		elem + str(i)
			for i in range(1, num_combinations + 1)
			if excluded_multiples is None or i % excluded_multiples != 0
				for elem in strings
	]

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(15))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
