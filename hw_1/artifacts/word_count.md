# Чтение из файла
## Один файл
```commandline
python3 ./word_count.py ./file1.txt
```
output:
```commandline
20 40 180 ./file1.txt
```
## Несколько файлов
```commandline
python3 ./word_count.py ./file1.txt ./file2.txt
```
output:
```commandline
20 40 180 ./file1.txt
10000000 20000000 99000002 ./file2.txt
10000020 20000040 99000182 total
```
# Чтение из `stdin`
```commandline
echo Hello world! | python3 ./word_count.py
```
output:
```commandline
1 2 13
```
Результаты совпадают с выводом `wc` кроме красивого форматирования,
не понимаю как у wc получается заранее знать длину столбца

Файлы были сгерированы с помощью утилит из предыдущего задания