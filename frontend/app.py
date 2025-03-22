from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import ast
from stats import make_stats

app = Flask(__name__)

def load_data():
    try:
        with open("dataset.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        data = [ast.literal_eval(line.strip()) for line in lines]
        df = pd.DataFrame(data, columns=["tune", "category", "re"])
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame(columns=["tune", "category", "re"])

def load_heatmap_data():
    try:
        data = make_stats()
        df = pd.DataFrame(data, columns=["category", "positive", "neutral", "negative"])
        return df
    except Exception as e:
        print(f"Error loading heatmap data: {e}")
        return pd.DataFrame(columns=["category", "positive", "neutral", "negative"])

@app.route('/')
def index():
    df = load_data()
    heatmap_df = load_heatmap_data()

    # Создание bar chart
    if not df.empty:
        category_counts = df['category'].value_counts()
        bar_fig = px.bar(category_counts, x=category_counts.index, y=category_counts.values, 
                          labels={'x': 'Категория', 'y': 'Количество'}, 
                          title='')
        bar_chart = bar_fig.to_html(full_html=False)
    else:
        bar_chart = ""

    # Создание pie chart
    if not df.empty:
        pie_fig = px.pie(category_counts, values=category_counts.values, names=category_counts.index, 
                         title='')
        pie_chart = pie_fig.to_html(full_html=False)
    else:
        pie_chart = ""

    # Создание heatmap
    if not heatmap_df.empty:
        heatmap_fig = px.imshow(
            heatmap_df.set_index('category'), 
            labels=dict(x="Параметры", y="Категории", color="Степень недовольства"),
            title="",
            color_continuous_scale=[[0, 'blue'], [1, 'red']],  # Цветовая шкала: синий -> красный
            width=800,  # Ширина heatmap
            height=600  # Высота heatmap
        )
        heatmap_chart = heatmap_fig.to_html(full_html=False)
    else:
        heatmap_chart = ""

    return render_template('index.html', bar_chart=bar_chart, pie_chart=pie_chart, heatmap_chart=heatmap_chart)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)