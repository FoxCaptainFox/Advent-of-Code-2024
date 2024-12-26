from utils import read_file

FILLED_CHAR = "#"
PIN_NUMBER = 5
PIN_MAX_HEIGHT = 5

schematics = read_file(25).split("\n\n")
locks, keys = [], []

for schematic in schematics:
    pin_heights = [
        sum(1 for row in schematic.split("\n")[1:-1] if row[col_index] == FILLED_CHAR)
        for col_index in range(PIN_NUMBER)
    ]
    (locks if schematic.startswith(FILLED_CHAR * PIN_NUMBER) else keys).append(pin_heights)

fitting_pairs_number = sum(
    all(key[i] + lock[i] <= PIN_MAX_HEIGHT for i in range(PIN_NUMBER))
    for lock in locks
    for key in keys
)

print(fitting_pairs_number)
