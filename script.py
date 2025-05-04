import json

# Загружаем JSON файл
input_file = 'result.json'  # Путь к твоему JSON файлу
output_file = 'vocab.py'  # Файл, куда будем записывать словарь

# Читаем данные из JSON
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Создаём пустой словарь для перевода
vocab = {}

# Проходим по сообщениям в JSON и извлекаем пары слов
for message in data['messages']:
    # Извлекаем английское слово и русский перевод
    if len(message['text']) >= 2:
        english_word = message['text'][0].strip().replace(" -", "")  # Убираем дефис из английского слова
        russian_word = message['text'][1]['text'].strip() if isinstance(message['text'][1], dict) else ""
        
        # Добавляем пару в словарь, если оба слова не пустые
        if english_word and russian_word:
            vocab[english_word] = russian_word

# Записываем результат в Python файл в формате словаря
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("vocab = {\n")
    for i, (word, translation) in enumerate(vocab.items()):
        # Убираем запятую после последней записи
        if i == len(vocab) - 1:
            f.write(f'    "{word}": "{translation}"\n')
        else:
            f.write(f'    "{word}": "{translation}",\n')
    f.write("}\n")

print(f"Словарь сохранён в {output_file}")