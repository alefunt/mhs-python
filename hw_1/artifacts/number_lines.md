# Вывод моей програмы

command:
```commandline
python3 ./generate_newlines.py | python3 ./number_lines.py
```
output:
```commandline
     1  |
     2  |
     3  |
     4  |
     5  |
     6  |
     7  |
     8  |
     9  |
    10  |
```
# Вывод утилиты nl
```commandline
python3 ./generate_newlines.py | nl -b a
```
output:
```commandline
     1  |
     2  |
     3  |
     4  |
     5  |
     6  |
     7  |
     8  |
     9  |
    10  |
```

# Форматирование вывода
Для проверки длинных текстов написал `./test.py` что бы убедиться что отступы работают правильно
```commandline
python3 ./generate_newlines.py 10_000_000 | nl -b a
```
output:
```commandline
...
9999999 |
10000000        |
```
результат идентичен

# Чтение из файла

```commandline
python3 ./generate_newlines.py 10 > tmp.txt
python3 ./number_lines.py tmp.txt
```
output:
```commandline
     1  |
     2  |
     3  |
     4  |
     5  |
     6  |
     7  |
     8  |
     9  |
    10  |
```
