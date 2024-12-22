from math import floor
from utils import read_data


# Shared logic

NUMBER_OF_SECRET_GENERATION = 2000

def generate_next(secret_number):
    secret_number = ((secret_number * 64) ^ secret_number) % 16777216
    secret_number = (floor(secret_number / 32) ^ secret_number) % 16777216
    secret_number = ((secret_number * 2048) ^ secret_number) % 16777216
    return secret_number


# Part 1

secret_numbers = [int(x) for x in read_data(22)]
result_sum = 0
for secret_number in secret_numbers:
    for _ in range(NUMBER_OF_SECRET_GENERATION):
        secret_number = generate_next(secret_number)
    result_sum += secret_number
print(result_sum)


# Part 2

SEQUENCE_LENGTH = 4

secret_numbers = [int(x) for x in read_data(22)]
prices_by_sequence = {}

for secret_number in secret_numbers:
    prices = [secret_number % 10]
    for _ in range(NUMBER_OF_SECRET_GENERATION):
        secret_number = generate_next(secret_number)
        prices.append(secret_number % 10)
    occured_sequences = []
    for price_index in range(SEQUENCE_LENGTH, len(prices)):
        sequence = ()
        for sequence_index in reversed(range(SEQUENCE_LENGTH)):
            this_price = prices[price_index - sequence_index]
            previos_price = prices[price_index - sequence_index - 1]
            sequence = sequence + (this_price - previos_price ,)
        if sequence in occured_sequences:
            continue
        occured_sequences.append(sequence)
        prices_by_sequence[sequence] = prices_by_sequence.get(sequence, 0) + prices[price_index]

print(max(prices_by_sequence.values()))
