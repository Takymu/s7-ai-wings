from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import ast

app = Flask(__name__)

def load_data():
    with open("dataset.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    data = [ast.literal_eval(line.strip()) for line in lines]
    df = pd.DataFrame(data, columns=["tune", "category", "re"])
    return df

@app.route('/')
def index():
    df = load_data()
    category_counts = df['category'].value_counts()

    # Создание bar chart
    bar_fig = px.bar(category_counts, x=category_counts.index, y=category_counts.values, 
                      labels={'x': 'Категория', 'y': 'Количество'}, 
                      title='Распределение отзывов по категориям')
    bar_chart = bar_fig.to_html(full_html=False)

    # Создание pie chart
    pie_fig = px.pie(category_counts, values=category_counts.values, names=category_counts.index, 
                     title='Распределение отзывов по категориям')
    pie_chart = pie_fig.to_html(full_html=False)

    return render_template('index.html', bar_chart=bar_chart, pie_chart=pie_chart)

if __name__ == '__main__':
    app.run(debug=True)