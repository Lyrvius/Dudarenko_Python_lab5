import re

# Функція читання першого речення
def read_first_sentence(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            #Збереження першого речення в змінну
            first_sentence = re.split(r'[.!?]', text)[0]
            print("Перше речення:", first_sentence)
            return first_sentence
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
    except Exception as e:
        print("Помилка при читанні файлу:", e)

# Функція очищення пунктуації та сортування (спершу українські слова, потім англійські)
def clean_and_sort_words(text):
    # Видалення пунктуації та розділення на слова
    words = re.findall(r'\b\w+\b', text.lower())
    # Відокремлення українських та англійських слів
    ukr_words = sorted([word for word in words if re.match(r'^[а-яєіїґ]', word)])
    eng_words = sorted([word for word in words if re.match(r'^[a-z]', word)])
    sorted_words = ukr_words + eng_words
    print("Відсортовані слова:", sorted_words)
    print("Кількість слів:", len(sorted_words))


file_path = 'text.txt'
first_sentence = read_first_sentence(file_path)
if first_sentence:
    clean_and_sort_words(first_sentence)