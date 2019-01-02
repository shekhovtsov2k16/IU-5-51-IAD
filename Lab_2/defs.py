def find_minimum(array):
    minimum = array[0]
    for i in range(array.__len__()):
        if array[i] <= minimum:
            minimum = array[i]
    return minimum


def find_avg(array):
    total = 0
    for i in range(array.__len__()):
        total += array[i]
    avg = total / array.__len__()
    return avg


def turn_over_string(greeting):
    answer = greeting[::-1]
    return answer


def filter_emps(emps, age):
    filtered = []
    for emp in emps:
        if emp['children']['age'] >= age:
            filtered.append(emp)
    return filtered
