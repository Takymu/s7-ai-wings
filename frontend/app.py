from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import ast
from stats import make_stats

app = Flask(__name__)

def load_data():
    with open("dataset.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    data = [ast.literal_eval(line.strip()) for line in lines]
    df = pd.DataFrame(data, columns=["tune", "category", "re"])
    return df

def load_heatmap_data():
    data = make_stats()
    df = pd.DataFrame(data, columns=["category", "positive", "neutral", "negative"])
    return df

@app.route('/')
def index():
    df = load_data()
    heatmap_df = load_heatmap_data()

    # Создание bar chart
    category_counts = df['category'].value_counts()
    bar_fig = px.bar(category_counts, x=category_counts.index, y=category_counts.values, 
                      labels={'x': 'Категория', 'y': 'Количество'}, 
                      title='Распределение отзывов по категориям')
    bar_chart = bar_fig.to_html(full_html=False)

    # Создание pie chart
    pie_fig = px.pie(category_counts, values=category_counts.values, names=category_counts.index, 
                     title='Распределение отзывов по категориям')
    pie_chart = pie_fig.to_html(full_html=False)

    # Создание heatmap
    heatmap_fig = px.imshow(
        heatmap_df.set_index('category'), 
        labels=dict(x="Параметры", y="Категории", color="Интенсивность"),
        title="Heatmap отзывов по категориям",
        color_continuous_scale=[[0, 'blue'], [1, 'red']],  # Цветовая шкала: синий -> красный
        width=800,  # Ширина heatmap
        height=600  # Высота heatmap
    )
    heatmap_chart = heatmap_fig.to_html(full_html=False)

    return render_template('index.html', bar_chart=bar_chart, pie_chart=pie_chart, heatmap_chart=heatmap_chart)

if __name__ == '__main__':
    app.run(debug=True)