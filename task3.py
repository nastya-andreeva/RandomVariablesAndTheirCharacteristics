from math import sqrt

file_path = "Москва_2021.txt"
with open(file_path, 'r') as file:
    data = file.read().splitlines()
data = list(map(int, data))


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


def coeff_var(data):
    return quar_mean(data) / average(data) * 100


def moda(data):
    un_data = set(data)
    ages = []
    freq = []
    for i in un_data:
        ages += [i]
        freq += [data.count(i)]
    max_freq = max(freq)
    ind = freq.index(max_freq)
    return ages[ind], max_freq


def mediana(data):
    mid = len(data) // 2
    return (data[mid - 1] + data[mid]) / 2


def max_m(data):
    return max(data)


def min_m(data):
    return min(data)


def scope(data):
    return max(data) - min(data)


def asim(data):
    av = average(data)
    n = len(data)
    quar_m = quar_mean(data)
    return sum((x - av) ** 3 for x in data) / (n * quar_m ** 3)


def ecc(data):
    av = average(data)
    n = len(data)
    quar_m = quar_mean(data)
    return sum((x - av) ** 4 for x in data) / (n * quar_m ** 4) - 3


print('средняя', average(data))
print('дисперсия', variance(data))
print('среднее квадратическое', quar_mean(data))
print('коэффициент вариации', coeff_var(data))
print('мода, частота', moda(data))
print('медиана', mediana(data))
print('макс', max_m(data))
print('мин', min_m(data))
print('размах', scope(data))
print('асимметрия', asim(data))
print('эксцесс', ecc(data))
