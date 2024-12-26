from collections import Counter
from utils import read_data


# Shared logic

def get_value_of_variable(gate_values, variable_prefix):
    return int("".join([str(value) for key, value in dict(sorted(gate_values.items(), reverse=True)).items() if key.startswith(variable_prefix)]), 2)


# Shared data processing

data = read_data(24)
separator_index = data.index("")
initial_gate_values = { line.split(": ")[0]: int(line.split(": ")[1]) for line in data[ : separator_index]}
gate_operations = []
for line in data[separator_index  + 1: ]:
    gate_operation = {}
    gate_operation["input1"] = line.split(" ")[0]
    gate_operation["operation"] = line.split(" ")[1]
    gate_operation["input2"] = line.split(" ")[2]
    gate_operation["output"] = line.split(" ")[4]
    gate_operations.append(gate_operation)


# Part 1
gate_values = initial_gate_values.copy()
queue = gate_operations[:]
while len(queue) > 0:
    gate_operation = next(go for go in queue if go["input1"] in gate_values and go["input2"] in gate_values)
    queue.remove(gate_operation)
    match gate_operation["operation"]:
        case "AND":
            gate_values[gate_operation["output"]] = gate_values[gate_operation["input1"]] & gate_values[gate_operation["input2"]]
        case "OR":
            gate_values[gate_operation["output"]] = gate_values[gate_operation["input1"]] | gate_values[gate_operation["input2"]]
        case "XOR":
            gate_values[gate_operation["output"]] = gate_values[gate_operation["input1"]] ^ gate_values[gate_operation["input2"]]

z_value = get_value_of_variable(gate_values, "z")
print(z_value)


# Part 2

# Prints graph structure for dreampuf.github.io/GraphvizOnline (dot engine recommended)
# to manually check for inconsistencies

print("digraph G {")
for go in gate_operations:
    print(go["input1"] + " -> " + go["output"] + "_" + go["operation"])
    print(go["input2"] + " -> " + go["output"] + "_" + go["operation"])
    print(go["output"] + "_" + go["operation"] + " -> " + go["output"])
print("}")
