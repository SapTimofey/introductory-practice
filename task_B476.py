"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов, используя форматирование
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  при этом не делить слова.
"""

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    text = ' '.join(lines)
    text = ''.join([c for c in text if c.isalpha() or c.isspace()])
    words = text.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    for i, (word, count) in enumerate(sorted_word_counts):
        print(f"{i+1} place --- {word} --- {count} times")
        text = text.replace(word, 'PYTHON')
    with open('output.txt', 'w', encoding='utf-8') as f:
        while len(text) > 100:
            space_index = text.rfind(' ', 0, 100)
            if space_index == -1:
                space_index = 100
            f.write(text[:space_index] + '\n')
            text = text[space_index+1:]
        f.write(text)


# Вызов функции
process_file('input.txt')
