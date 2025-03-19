import matplotlib.pyplot as plt

file_path = "Москва_2021.txt"
with open(file_path, 'r') as file:
    data = file.read().splitlines()
data = sorted(list(map(int, data)))
un_data = set(data)
ages = []
freq = []
for i in un_data:
    ages += [i]
    freq += [data.count(i)]

plt.figure(figsize=(8, 5))
plt.plot(ages, freq, color='red')
plt.xlabel('Возраст')
plt.ylabel('Частота')
plt.show()

