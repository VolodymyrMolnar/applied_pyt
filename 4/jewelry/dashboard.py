import plotly.express as px
from plotly.offline import plot

# Bar Chart
def create_bar_chart(df, x_col, y_col, title="Bar Chart"):
    fig = px.bar(df, x=x_col, y=y_col, title=title)
    return plot(fig, output_type='div')

# Pie Chart
def create_pie_chart(df, names_col, values_col, title="Pie Chart"):
    fig = px.pie(df, names=names_col, values=values_col, title=title)
    return plot(fig, output_type='div')

def create_line_chart(df):
    fig = px.line(df, x='type', y='price', title='Price Trend by Type')
    return plot(fig, output_type='div')
