import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components


def create_query1_bokeh_chart(data, sort_order):

    df = pd.DataFrame(list(data))

    if df.empty:
        return None, None, None

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

    p = figure(
        x_range=list(df['type']),
        title="Середня ціна продуктів по типах",
        toolbar_location=None,
        tools=""
    )
    p.vbar(
        x=df['type'],
        top=df['avg_price'],
        width=0.5,
        color="blue"
    )

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.axis_label = "Тип продукту"
    p.yaxis.axis_label = "Середня ціна"

    script, div = components(p)
    return script, div, stats
