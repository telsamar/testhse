import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patheffects as pe

data = pd.read_excel("processed_data_reordered.xlsx")

# Функция переноса длинных словосочетаний
def split_long_words(keyword):
    words = keyword.split()
    new_words = []
    for word in words:
        if len(word) > 10:
            midpoint = len(word) // 2
            # Пытаемся найти ближайший пробел для переноса
            for idx in range(midpoint - 1, -1, -1):
                if word[idx] == ' ':
                    midpoint = idx
                    break
            new_words.append(word[:midpoint] + '\n' + word[midpoint:])
        else:
            new_words.append(word)
    return ' '.join(new_words)

data['keyword'] = data['keyword'].apply(split_long_words)

# Исключение строк с недопустимыми значениями в столбце 'count'
data = data[data['count'].apply(lambda x: str(x).isdigit())]

# Преобразование count в размер точек (масштабирование для лучшей визуализации) и увеличения базового размера и диапазона масштабирования
data['count'] = data['count'].astype(int)
data['point_size'] = (data['count'] - data['count'].min()) / (data['count'].max() - data['count'].min()) * 250 + 50

# Настройка стилей
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (15, 15)

# Папка для сохранения изображений
output_folder = "images"

# Создание папки для сохранения изображений, если она не существует
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Визуализация для каждой области
areas = data['area'].unique()
for area in areas:
    area_data = data[data['area'] == area]
    
    plt.figure()
    
    # Создание диаграммы рассеяния и добавление легенды
    labels_added = []
    for cluster in area_data['cluster'].unique():
        cluster_data = area_data[area_data['cluster'] == cluster]
        label = f"Кластер {cluster}"
        if label not in labels_added:
            plt.scatter(cluster_data['x'], cluster_data['y'], 
                        s=cluster_data['point_size'], 
                        c=cluster_data['color'], 
                        label=label, 
                        edgecolors='black', 
                        linewidths=0.5, 
                        marker='o')
            labels_added.append(label)
        else:
            plt.scatter(cluster_data['x'], cluster_data['y'], 
                        s=cluster_data['point_size'], 
                        c=cluster_data['color'], 
                        edgecolors='black', 
                        linewidths=0.5, 
                        marker='o')
    
    # Добавление подписей к точкам с белым контуром для лучшей читаемости
    for _, row in area_data.iterrows():
        plt.text(row['x'], row['y'], row['keyword'], fontsize=9, ha='center', va='center', 
                 color='black', path_effects=[plt.matplotlib.patheffects.withStroke(linewidth=1.5, foreground='white')])
    
    # Настройка графика
    plt.title(f"Диаграмма рассеяния для области: {area}")
    plt.axis('off')  # Убрать оси
    plt.legend(loc="upper right")
    
    # Добавление Footer-подписи
    plt.annotate("Это тестовое задание. Выполнил Седнев А.В.", (0.5, 0.01), 
                 xycoords='axes fraction', va='center', ha='center', fontsize=10, color='gray')
    
    # Сохранение изображения с заменой слэшей в имени файла
    filename = f"{output_folder}/{area.replace('/', '_')}_scatter_plot.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')

    # Закрытие графика
    plt.close()
