# Shell_language

# Инструмент командной строки для перевода XML

### Условие задачи

Разработать инструмент командной строки для учебного конфигурационного языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из входного формата в выходной. Синтаксические ошибки выявляются с выдачей сообщений.

- Входной текст на языке XML принимается из стандартного ввода.
- Выходной текст на учебном конфигурационном языке попадает в стандартный вывод.

**Поддерживаемые конструкции:**

- Многострочные комментарии:
  ```
  /#
  Это многострочный
  комментарий
  #/
  ```
- Словари:
  ```
  dict(
      имя = значение,
      имя = значение,
      ...
  )
  ```
- Имена:
  `[_A-Z][_a-zA-Z0-9]*`
- Значения:
  - Числа.
  - Словари.

**Работа с константами:**

- Объявление константы: `set имя = значение;`
- Использование константы: `@[имя]`

Все конструкции языка должны поддерживать вложенность и быть протестированы.

# Инструмент командной строки для перевода XML

Программа преобразует XML-текст в учебный конфигурационный язык и проверяет синтаксические ошибки.

## Возможности

- Перевод XML-текста в целевой формат.
- Поиск и вывод ошибок с пояснениями.
- Поддержка:
  - Многострочных комментариев:
    ```
    /#
    Это комментарий
    #/
    ```
  - Словарей:
    ```
    dict(
        ключ = значение,
        ключ = значение
    )
    ```
  - Констант:
    - Объявление: `set имя = значение;`
    - Использование: `@[имя]`

## Установка и использование

1. Запустите программу:
   ```bash
   python main.py < input.xml > output.txt
   ```
2. Для тестирования выполните:
   ```bash
   python3  input.xml
   ```

## Примеры
Пример вывода:


Значение на ввод:

<img width="360" alt="image" src="https://github.com/user-attachments/assets/366c56e9-c8e3-4172-bee9-2cd160cb3f77">

Значение на вывод:
<img width="203" alt="image" src="https://github.com/user-attachments/assets/847d1a3b-060c-44ae-af30-cfcc5c81fca8">






## Тестирование (Unittest)

Чтобы проверить работу программы, выполните:
```bash
python3 test_script.py
```

## Структура проекта

- `main.py`: Основной код программы.
- `test_script.py`: Тесты для проверки работы.
- `README.md`: Описание проекта.

