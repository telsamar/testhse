# Часть 2. Построение графиков

## Описание
Данная программа создает диаграммы рассеяния для каждой уникальной области (area) на основе данных из файла Excel. Графики сохраняются в папке "images".

## Требования
1. Python 3.x
2. Библиотеки:
   - pandas
   - matplotlib
   - seaborn

## Использование
1. Установите необходимые библиотеки с помощью pip:

```
pip install pandas matplotlib seaborn
```

2. Скопируйте ваш файл данных `processed_data_reordered.xlsx` в ту же директорию, где находится программа.

3. Запустите программу:

```
python main2.py
```

4. После выполнения программа создаст папку "images", в которой будут сохранены диаграммы рассеяния для каждой уникальной области.