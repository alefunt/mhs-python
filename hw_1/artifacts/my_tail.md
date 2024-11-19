# Чтение из `stdin`

## Текст меньше 17 строк
command:
```commandline
python3 ./generate_newlines.py 15 | python3 ./number_lines.py | python3 ./my_tail.py
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
    11  |
    12  |
    13  |
    14  |
    15  |
```
## Текст больше 17 строк
command:
```commandline
python3 ./generate_newlines.py 20 | python3 ./number_lines.py | python3 ./my_tail.py
```
output:
```commandline
     4  |
     5  |
     6  |
     7  |
     8  |
     9  |
    10  |
    11  |
    12  |
    13  |
    14  |
    15  |
    16  |
    17  |
    18  |
    19  |
    20  |
```
# Чтение из файла
## Один файл
command:
```commandline
python3 ./my_tail.py ./file1.txt
```
output:
```commandline
     6  |
     7  |
     8  |
     9  |
    10  |
    11  |
    12  |
    13  |
    14  |
    15  |
```
command:
```commandline
python3 ./generate_newlines.py 12345 | python3 ./number_lines.py | python3 ./my_tail.py
```
output:
```commandline
 12329  |
 12330  |
 12331  |
 12332  |
 12333  |
 12334  |
 12335  |
 12336  |
 12337  |
 12338  |
 12339  |
 12340  |
 12341  |
 12342  |
 12343  |
 12344  |
 12345  |
```
## Несколько файлов
command:
```commandline
python3 ./my_tail.py ./file1.txt ./file2.txt
```
output:
```commandline
=> ./file1.txt <=
     6  |
     7  |
     8  |
     9  |
    10  |
    11  |
    12  |
    13  |
    14  |
    15  |

=> ./file2.txt <=
     6  |
     7  |
     8  |
     9  |
    10  |
    11  |
    12  |
    13  |
    14  |
    15  |
```
Файлы были сгенерированы с помощью утилит из предыдущего задания
```commandline
python3 ./generate_newlines.py 15 | python3 ./number_lines.py > file1.txt
python3 ./generate_newlines.py 15 | python3 ./number_lines.py > file2.txt
```