import pandas as pd
from plotly.offline import plot
import plotly.express as px


def create_query1_chart(data, sort_order):

    df = pd.DataFrame(list(data))

    if df.empty:
        return None, None

    df['avg_price'] = df['avg_price'].astype(float)

    if sort_order == 'asc':
        df = df.sort_values(by='avg_price', ascending=True)
    elif sort_order == 'desc':
        df = df.sort_values(by='avg_price', ascending=False)

    stats = {
        'mean': df['avg_price'].mean(),
        'median': df['avg_price'].median(),
        'min': df['avg_price'].min(),
        'max': df['avg_price'].max(),
    }

    fig = px.bar(
        df,
        x='type',
        y='avg_price',
        title="Середня ціна продуктів по типах",
        labels={'type': 'Тип продукту', 'avg_price': 'Середня ціна'}
    )

    fig.update_layout(
        xaxis_title="Тип продукту",
        yaxis_title="Середня ціна",
        title_font_size=20,
        xaxis_tickangle=-45
    )

    chart = plot(fig, output_type='div')
    return chart, stats
