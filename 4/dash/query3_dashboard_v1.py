import pandas as pd
from plotly.offline import plot
import plotly.express as px


def create_query3_chart(data, sort_order):

    df = pd.DataFrame(list(data))
    if df.empty:
        return None, None


    df['max_price'] = df['max_price'].astype(float)


    if sort_order == 'asc':
        df = df.sort_values(by='max_price', ascending=True)
    elif sort_order == 'desc':
        df = df.sort_values(by='max_price', ascending=False)


    stats = {
        'mean': df['max_price'].mean(),
        'median': df['max_price'].median(),
        'min': df['max_price'].min(),
        'max': df['max_price'].max(),
    }


    fig = px.bar(
        df,
        x='type',
        y='max_price',
        title="Найдорожчий продукт по категоріях",
        labels={'type': 'Категорія', 'max_price': 'Ціна'},
    )
    fig.update_layout(xaxis_title="Категорія", yaxis_title="Ціна", title_font_size=20)


    chart = plot(fig, output_type='div')
    return chart, stats
