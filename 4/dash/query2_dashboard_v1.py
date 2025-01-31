import pandas as pd
from plotly.offline import plot
import plotly.express as px

def create_query2_chart(data, sort_order):
    df = pd.DataFrame(list(data))
    if df.empty:
        return None, None

    df['total_quantity'] = df['total_quantity'].astype(float)

    if sort_order == 'asc':
        df = df.sort_values(by='total_quantity', ascending=True)
    elif sort_order == 'desc':
        df = df.sort_values(by='total_quantity', ascending=False)

    stats = {
        'mean': df['total_quantity'].mean(),
        'median': df['total_quantity'].median(),
        'min': df['total_quantity'].min(),
        'max': df['total_quantity'].max(),
    }

    fig = px.pie(df, names='product__type', values='total_quantity', title="Загальна кількість замовлень по типах")
    chart = plot(fig, output_type='div')
    return chart, stats
