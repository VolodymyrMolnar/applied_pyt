import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components


def create_query4_bokeh_chart(data, sort_order):

    df = pd.DataFrame(list(data))
    if df.empty:
        return None, None, None


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


    p = figure(
        title="Мінімальна кількість замовленого продукту",
        x_axis_label='ID Замовлення',
        y_axis_label='Мін. кількість',
        toolbar_location=None,
        tools=""
    )
    p.line(x=df['order__id'], y=df['min_quantity'], line_width=2, color="green")
    p.circle(x=df['order__id'], y=df['min_quantity'], size=10, color="orange", legend_label="Точки")

    script, div = components(p)
    return script, div, stats
