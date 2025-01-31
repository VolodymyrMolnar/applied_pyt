import pandas as pd
from plotly.offline import plot
import plotly.express as px

def create_query5_chart(data, sort_order):

    df = pd.DataFrame(list(data))
    if df.empty:
        return None, None

    df['order_count'] = df['order_count'].astype(float)

    if sort_order == 'asc':
        df = df.sort_values(by='order_count', ascending=True)
    elif sort_order == 'desc':
        df = df.sort_values(by='order_count', ascending=False)

    stats = {
        'mean': df['order_count'].mean(),
        'median': df['order_count'].median(),
        'min': df['order_count'].min(),
        'max': df['order_count'].max(),
    }

    fig = px.bar(
        df,
        x='order_count',
        y='status',
        orientation='h',
        title="Кількість замовлень за статусом",
        labels={'order_count': 'Кількість замовлень', 'status': 'Статус'},
        color='order_count',
        color_continuous_scale='Blues',
    )

    fig.update_layout(
        xaxis_title="Кількість замовлень",
        yaxis_title="Статус",
        yaxis=dict(categoryorder="total ascending"),
        height=500,
        margin=dict(l=40, r=40, t=40, b=40),
    )

    chart = plot(fig, output_type='div')
    return chart, stats
