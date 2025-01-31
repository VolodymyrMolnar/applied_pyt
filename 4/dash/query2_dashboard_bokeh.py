import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.palettes import Category20c
from bokeh.transform import cumsum
from math import pi

def create_query2_bokeh_chart(data, sort_order):
    df = pd.DataFrame(list(data))
    if df.empty:
        return None, None, None

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

    df['angle'] = df['total_quantity'] / df['total_quantity'].sum() * 2 * pi
    df['color'] = Category20c[len(df)]

    p = figure(
        height=400,
        title="Загальна кількість замовлень за типами продуктів",
        toolbar_location=None,
        tools="hover",
        tooltips="@product__type: @total_quantity",
        x_range=(-0.5, 1.0),
    )

    p.wedge(
        x=0,
        y=1,
        radius=0.4,
        start_angle=cumsum('angle', include_zero=True),
        end_angle=cumsum('angle'),
        line_color="white",
        fill_color='color',
        legend_field='product__type',
        source=df,
    )

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    script, div = components(p)
    return script, div, stats
