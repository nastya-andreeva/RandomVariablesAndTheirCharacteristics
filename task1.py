file_path = "Москва_2021.txt"
with open(file_path, 'r') as file:
    data = file.read().splitlines()
data = sorted(list(map(int, data)))
un_data = set(data)
for i in un_data:
    print(i, data.count(i))
