import pandas as pd
from plotly.offline import plot
import plotly.express as px

def create_query6_chart(data, sort_order):


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
        'max': df['avg_price'].max()
    }

    fig = px.bar(
        df,
        x='product__type',
        y='avg_price',
        title="Середня ціна продукту в замовленнях",
        labels={'product__type': 'Тип продукту', 'avg_price': 'Середня ціна'},
        color='avg_price',
        color_continuous_scale='Greens',
    )

    fig.update_layout(
        xaxis_title="Тип продукту",
        yaxis_title="Середня ціна",
        height=500,
        margin=dict(l=40, r=40, t=40, b=40),
    )

    return fig.to_html(full_html=False), stats
