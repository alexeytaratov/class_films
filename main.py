from Films import Film
read_data = []
data_list = []
data_list2 = []
watched_films_list = []
need_to_watch_list = []
watched_films_index = 0
need_to_watch_films_index = 0

with open('text.txt', 'r', encoding='utf-8') as f: # читаем файл полностью в рид_дата,
                                                    # записывается в переменную, как список с 1 элементом (строкой)
    read_data.append(f.read())
f.close()

read_data = read_data[0].split('\n') # переводим в список, разделяем строки по символу
print(read_data)

for i in range(len(read_data)): # убираем пустые строки
    if read_data[i] != '':
        data_list.append(read_data[i])
print(data_list)

for i in range(len(data_list)): # убираем '---'
    if data_list[i] != '---':
        data_list2.append(data_list[i])
print(data_list2)

for i in range(len(data_list2)): # узнаем индекс начала списка фильмов из текстового файла (которые надо посмотреть)
    if '### Фильмы:' in data_list2[i]:
        need_to_watch_films_index = i
print(need_to_watch_films_index)

for i in range(len(data_list2)): # узнаем индекс начала списка фильмов из текстового файла (которые уже просмотрены)
    if '### **Просмотрено:**' in data_list2[i]:
        watched_films_index = i
print(watched_films_index)

for i in range(need_to_watch_films_index + 1, watched_films_index): # создаём обьекты в список и передаём параметры в конструктор
    need_to_watch_list.append(Film(i - 1, data_list2[i]))

#for i in range(len(need_to_watch_list)): # поочередно выводим объекты
     #print(need_to_watch_list[i].id)
     #print(need_to_watch_list[i].name)
     #print('\n')

file_need_to_watch = open('file_need_to_watch.txt', 'w', encoding='utf-8') # тут открываем файл на запись и ниже записываем
                                                             # переведенные в строки аргументы объектов в новый файл
for i in range(len(need_to_watch_list)):
    file_need_to_watch.write(str(need_to_watch_list[i].id))
    file_need_to_watch.write('\t')
    file_need_to_watch.write(str(need_to_watch_list[i].name))
    file_need_to_watch.write('\n')

for i in range(watched_films_index + 1, len(data_list2)): # создаём обьекты в список и передаём параметры в конструктор
    watched_films_list.append(Film(i - 1, data_list2[i]))

#for i in range(len(watched_films_list)): # поочередно выводим объекты
     #print(watched_films_list[i].id)
     #print(watched_films_list[i].name)
     #print('\n')

file_wached = open('file_wached.txt', 'w', encoding='utf-8') # тут открываем файл на запись и ниже записываем
                                                             # переведенные в строки аргументы объектов в новый файл
for i in range(len(watched_films_list)):
    file_wached.write(str(watched_films_list[i].id))
    file_wached.write('\t')
    file_wached.write(str(watched_films_list[i].name))
    file_wached.write('\n')