import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components

def create_query5_bokeh_chart(data, sort_order):

    df = pd.DataFrame(list(data))
    if df.empty:
        return None, None, None

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

    p = figure(
        y_range=list(df['status']),
        x_range=(0, df['order_count'].max() + 5),
        title="Кількість замовлень за статусом",
        width=800,
        height=400,
    )

    p.hbar(
        y=df['status'],
        right=df['order_count'],
        height=0.4,
        color="navy",
        legend_field="status",
    )

    p.xaxis.axis_label = "Кількість замовлень"
    p.yaxis.axis_label = "Статус"
    p.legend.visible = False

    script, div = components(p)
    return script, div, stats
