import pandas as pd
from plotly.offline import plot
import plotly.express as px

def create_query4_chart(data, sort_order):

    df = pd.DataFrame(list(data))
    if df.empty:
        return None, None

    df['min_quantity'] = df['min_quantity'].astype(float)

    if sort_order == 'asc':
        df = df.sort_values(by='min_quantity', ascending=True)
    elif sort_order == 'desc':
        df = df.sort_values(by='min_quantity', ascending=False)
    else:
        df = df.sort_values(by='order__id', ascending=True)  # Сортування за замовчуванням

    stats = {
        'mean': df['min_quantity'].mean(),
        'median': df['min_quantity'].median(),
        'min': df['min_quantity'].min(),
        'max': df['min_quantity'].max(),
    }

    fig = px.line(
        df,
        x='order__id',
        y='min_quantity',
        title="Мінімальна кількість замовленого продукту",
        labels={'order__id': 'ID Замовлення', 'min_quantity': 'Мін. кількість'}
    )
    fig.update_layout(xaxis_title="ID Замовлення", yaxis_title="Мін. кількість", title_font_size=20)

    chart = plot(fig, output_type='div')
    return chart, stats
