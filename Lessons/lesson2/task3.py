# Задание на закрепление знаний по модулю yaml.
# Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
# Подготовить данные для записи в виде словаря,
# в котором первому ключу соответствует список, второму — целое число, третьему — вложенный словарь, где значение
# каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
# При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а
# также установить возможность работы с юникодом: allow_unicode = True;
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

import yaml

def main():
    dict_name = {
        'key1':['test',123,'wer1'],
        'key2':530,
        'key3': {'key4':785}
    }

    file_name = 'file.yaml'
    yaml.dump(dict_name, open(file_name, mode='w'), sort_keys=True, indent=4)

    with open(file_name) as f:
        for i in f:
            print(i)


if __name__ == '__main__':
    try:
        main()
    except Exception as answer:
        print(answer)



main()