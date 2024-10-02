import os

# Список файлов, которые нужно объединить
file_names = ['1.txt', '2.txt']  # Укажите ваши файлы здесь

# Словарь для хранения имени файла и его количества строк
file_info = {}

# Считываем информацию о каждом файле
for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        file_info[file_name] = len(lines)

# Сортируем файлы по количеству строк
sorted_files = sorted(file_info.items(), key=lambda item: item[1])

# Создаем итоговый файл
with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_name, line_count in sorted_files:
        # Записываем имя файла и количество строк
        result_file.write(f"{file_name}\n{line_count}\n")
        
        # Записываем содержимое файла
        with open(file_name, 'r', encoding='utf-8') as f:
            result_file.writelines(f.readlines())

print("Файлы успешно объединены в result.txt")