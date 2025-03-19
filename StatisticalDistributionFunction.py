import matplotlib.pyplot as plt


def cumulative_freq(data):
    cumulative_s = 0
    cumulative_lst = []
    for i in data:
        cumulative_s += data.count(i)
        cumulative_lst.append(cumulative_s / len(data) / 1000)
    return cumulative_lst


file_path = "Москва_2021.txt"
with open(file_path, 'r') as file:
    data = file.read().splitlines()
data = sorted(list(map(int, data)))

plt.step(data, cumulative_freq(data), color='red')
plt.xlabel('Возраст')
plt.ylabel('Накопленные частоты')
plt.show()

