import pandas as pd

data = pd.read_excel("test.xlsx")

# Копирование нужных колонок для  обработки
data_cleaned = data[["area", "cluster", "cluster_name", "keyword", "x", "y", "count"]].copy()

# Определение цветовой палитры из Tableau
color_palette = [
    "#1F77B4", "#FF7F0E", "#2CA02C", "#D62728", "#9467BD", 
    "#8C564B", "#E377C2", "#7F7F7F", "#BCBD22", "#17BECF"
]

# Добавление колонки для цвета и назначение цветов кластерам внутри каждой области
data_cleaned["color"] = ""
for area in data_cleaned["area"].unique():
    subset = data_cleaned[data_cleaned["area"] == area]
    clusters = subset["cluster"].unique()
    
    for i, cluster in enumerate(clusters):
        data_cleaned.loc[(data_cleaned["area"] == area) & (data_cleaned["cluster"] == cluster), "color"] = color_palette[i % len(color_palette)]

# Удаление дубликатов словосочетаний в каждой области
data_cleaned = data_cleaned.drop_duplicates(subset=["area", "keyword"], keep="first")

# Сортировка данных
data_sorted = data_cleaned.sort_values(by=["area", "cluster", "cluster_name", "count"], ascending=[True, True, True, False])

# Переупорядочивание колонок
data_reordered = data_sorted[["area", "cluster", "cluster_name", "keyword", "x", "y", "count", "color"]]

# Сохранение обработанных данных в файл Excel с закрепленными заголовками и включенными фильтрами
output_reordered_filename = "processed_data_reordered.xlsx"
with pd.ExcelWriter(output_reordered_filename, engine='openpyxl') as writer:
    data_reordered.to_excel(writer, sheet_name="Data", index=False, freeze_panes=(1, 0))
    worksheet = writer.sheets["Data"]
    for idx, column in enumerate(data_reordered.columns, 1):
        worksheet.column_dimensions[chr(64 + idx)].auto_size = True
    worksheet.auto_filter.ref = worksheet.dimensions
