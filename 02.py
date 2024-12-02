from utils import read_data

# Shared logic

def is_safe(report):
    is_safely_increasing = all(-3 <= report[i] - report[i+1] < 0 for i in range(len(report) - 1))
    is_safely_decreasing = all(0 < report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return is_safely_increasing or is_safely_decreasing


# Shared input processing

data_as_str_lines = read_data(2)
data = [[int(n) for n in line.split(" ")] for line in data_as_str_lines]


# Part 1

safe_reports = [report for report in data if is_safe(report)]
print(len(safe_reports))


# Part 2

safe_reports_count = 0
for report in data:
    report_variations = [report[:i] + report[i+1 :] for i in range(len(report))]
    if is_safe(report) or any(is_safe(report_variation) for report_variation in report_variations):
        safe_reports_count += 1
print(safe_reports_count)
