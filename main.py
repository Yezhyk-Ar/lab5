import re

def sort_custom(words):
    """
    Сортування слів за алфавітом, спочатку українські, потім англійські, незалежно від регістру.
    """
    ua_letters = 'абвгґдеєжзийіклмнопрстуфхцчшщьюя'
    en_letters = 'abcdefghijklmnopqrstuvwxyz'

    def sort_key(word):
        lower_word = word.lower()
        if re.match(f"^[{ua_letters}]", lower_word, re.IGNORECASE):
            return (0, lower_word)
        elif re.match(f"^[{en_letters}]", lower_word, re.IGNORECASE):
            return (1, lower_word)
        return (2, lower_word)

    return sorted(words, key=sort_key)

def read_and_process_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        # Знаходження першого речення
        first_sentence = re.split(r'[.!?]', text.strip())[0]
        print("Перше речення з файлу:")
        print(first_sentence)

        # Витягування слів без пунктуації
        words = re.findall(r'\b\w+\b', text)
        sorted_words = sort_custom(words)

        print("\nВідсортовані слова:")
        print(sorted_words)
        print(f"\nЗагальна кількість слів: {len(words)}")

    except FileNotFoundError:
        print(f"Помилка: файл '{filename}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    file_name = "text.txt"
    read_and_process_file(file_name)
