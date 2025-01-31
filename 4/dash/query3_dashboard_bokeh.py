import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components


def create_query3_bokeh_chart(data, sort_order):

    df = pd.DataFrame(list(data))
    if df.empty:
        return None, None, None

    df['max_price'] = df['max_price'].astype(float)

    if sort_order == 'asc':
        df = df.sort_values(by='max_price', ascending=True)
    elif sort_order == 'desc':
        df = df.sort_values(by='max_price', ascending=False)
    else:
        df = df.sort_values(by='type', ascending=True)  # За замовчуванням сортування за категорією

    stats = {
        'mean': df['max_price'].mean(),
        'median': df['max_price'].median(),
        'min': df['max_price'].min(),
        'max': df['max_price'].max(),
    }

    p = figure(
        x_range=list(df['type']),
        title="Найдорожчий продукт у кожній категорії",
        width=800,
        height=400,
    )
    p.vbar(x=df['type'], top=df['max_price'], width=0.5, color="navy")
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.axis_label = "Категорія"
    p.yaxis.axis_label = "Ціна"

    script, div = components(p)
    return script, div, stats
