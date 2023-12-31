# Часть 1. Работа с данными

## Описание
Эта программа предназначена для обработки данных из файла Excel, присваивания цветов кластерам на основе определенных критериев и сохранения обработанных данных в новый файл Excel.

## Требования
- Python 3.x
- pandas
- openpyxl

## Установка зависимостей
Перед запуском программы убедитесь, что у вас установлены все необходимые библиотеки:
```
pip install pandas openpyxl
```

## Использование
1. Поместите ваш исходный файл Excel (например, "test.xlsx") в ту же директорию, что и программа.
2. Запустите программу.
3. После завершения выполнения программы проверьте созданный файл "processed_data_reordered.xlsx" в той же директории.

## Особенности
- Программа автоматически назначает цвета из предопределенной палитры Tableau для каждого кластера в каждой области.
- Дубликаты словосочетаний в каждой области удаляются.
- Данные сортируются по области, кластеру, названию кластера и количеству.
- Заголовки в выходном файле Excel закреплены, а также включен фильтр для удобства анализа.