from math import sqrt


def average(data):
    return sum(data)/len(data)


def variance(data):
    av = average(data)
    un_data = set(data)
    ages = []
    freq = []
    for i in un_data:
        ages += [i]
        freq += [data.count(i)]
    var = sum([(ages[i] - av) ** 2 * freq[i] for i in range(len(un_data))]) / sum(freq)
    return var


def quar_mean(data):
    return sqrt(variance(data))


def check_rule(data):
    av = average(data)
    quar_m = quar_mean(data)

    one_sigma_range = (av - quar_m, av + quar_m)
    two_sigma_range = (av - 2 * quar_m, av + 2 * quar_m)
    three_sigma_range = (av - 3 * quar_m, av + 3 * quar_m)

    one_sigma_count = sum(1 for x in data if one_sigma_range[0] <= x <= one_sigma_range[1])
    two_sigma_count = sum(1 for x in data if two_sigma_range[0] <= x <= two_sigma_range[1])
    three_sigma_count = sum(1 for x in data if three_sigma_range[0] <= x <= three_sigma_range[1])

    one_sigma_per = (one_sigma_count / len(data)) * 100
    two_sigma_per = (two_sigma_count / len(data)) * 100
    three_sigma_per = (three_sigma_count / len(data)) * 100

    print(one_sigma_per, 'примерно 68')
    print(two_sigma_per, 'примерно 95')
    print(three_sigma_per, 'примерно 99.7')


file_path = "Москва_2021.txt"
with open(file_path, 'r') as file:
    data = file.read().splitlines()
data = list(map(int, data))
check_rule(data)
