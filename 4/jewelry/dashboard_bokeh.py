from bokeh.plotting import figure
from bokeh.embed import components

def create_bokeh_bar_chart(df, x_col, y_col, title="Bar Chart"):
    p = figure(x_range=list(df[x_col]), title=title, width=800, height=400)
    p.vbar(x=df[x_col], top=df[y_col], width=0.5, color="navy")
    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    script, div = components(p)
    return script, div