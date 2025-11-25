import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Данные (исправленная версия)
data = {
    'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    'Russia': [65.3, 65.4, 65.7, 65.9, 66.4, 66.9, 67.5, 68.1, 68.7, 69.0, 69.3,
               69.8, 70.3, 70.6, 70.9, 71.3, 71.5, 71.6, 71.7, 71.9, 72.2, 72.4, 72.7],
    'China': [71.7, 72.1, 72.5, 72.9, 73.3, 73.7, 74.1, 74.5, 74.9, 75.3, 75.7,
              76.0, 76.4, 76.7, 77.0, 77.3, 77.5, 77.9, 78.2, 78.5, 78.8, 79.1, 79.3],
    'India': [62.3, 62.7, 63.1, 63.6, 64.1, 64.6, 65.2, 65.7, 66.2, 66.6, 67.1,
              67.6, 68.1, 68.5, 68.9, 69.4, 69.9, 70.4, 70.8, 71.3, 71.7, 72.0, 72.4],
    'Zimbabwe': [43.4, 42.1, 41.1, 41.5, 42.3, 43.8, 45.3, 46.6, 48.2, 50.0, 52.4,
                 54.2, 56.1, 58.0, 59.2, 61.7, 64.4, 67.0, 59.5, 61.5, 63.0, 63.0, 63.0],
    'USA': [76.8, 76.9, 77.0, 77.2, 77.5, 77.6, 77.8, 78.1, 78.2, 78.5, 78.7,
            78.7, 78.8, 78.9, 79.0, 79.1, 79.1, 79.1, 79.1, 79.1, 79.1, 79.0, 79.1]
}

# Создание DataFrame
df = pd.DataFrame(data)

# Настройка стиля
plt.style.use('seaborn-v0_8')
plt.figure(figsize=(12, 8))

# Построение графиков для каждой страны
countries = ['Russia', 'China', 'India', 'Zimbabwe', 'USA']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

for i, country in enumerate(countries):
    plt.plot(df['Year'], df[country],
             label=country,
             color=colors[i],
             linewidth=2.5,
             marker='o',
             markersize=4)

# Настройка графика
plt.title('Динамика средней продолжительности жизни по странам (2000-2022)',
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Год', fontsize=12)
plt.ylabel('Продолжительность жизни (годы)', fontsize=12)
plt.legend(fontsize=11, loc='upper left')
plt.grid(True, alpha=0.3)

# Настройка осей
plt.xticks(range(2000, 2023, 2), rotation=45)
plt.ylim(35, 85)

# Улучшение layout
plt.tight_layout()

# Показать график
plt.show()

# Дополнительно: сохранение графика
# plt.savefig('life_expectancy_trends.png', dpi=300, bbox_inches='tight')