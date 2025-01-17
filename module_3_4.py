# Самостоятельная работа по уроку "Произвольное число параметров".

# Задача "Однокоренные":

# Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word,
# а далее неограниченную последовательность в параметр *other_words.
# Функция должна составить новый список same_words только из тех слов списка other_words,
# которые содержат root_word или наоборот root_word содержит одно из этих слов.
# После вернуть список same_words в качестве результата своей работы.

# Пункты задачи:
# 1. Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
# 2. Создайте внутри функции пустой список same_words, который пополнится нужными словами.
# 3. При помощи цикла for переберите предполагаемо подходящие слова.
# 4. Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
# 5. После цикла верните образованный функцией список same_words.
# 6. Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.


def single_root_words(root_word, *other_words):  # объявление функции

    same_words = []     # создание пустого списка

    for i in other_words:   # условие с for
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)

    return same_words   # возвращение списка

# вызов функции и вывод на экран
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)