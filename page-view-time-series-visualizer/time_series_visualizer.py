import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
from datetime import datetime
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv').set_index('date')

# Clean data
df = df[(df ['value'] >= df['value'].quantile(0.025))&
     (df['value'] <= df['value'].quantile(0.975))
     ]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(12, 6))
    x_axis = pd.to_datetime(df.index)
    y_axis = df['value']
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.plot(x_axis, y_axis, color='red')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year'] = pd.to_datetime(df.index).year
    df_bar['month'] = pd.to_datetime(df.index).month
    df_bar = df_bar.groupby(["year", "month"])["value"].mean()
    df_bar = df_bar.unstack()
    # Draw bar plot
    fig = df_bar.plot(kind="bar", legend=True, figsize=(15, 10)).figure
    plt.xlabel("Years", fontsize=10)
    plt.ylabel("Average Page Views", fontsize=10)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.legend(fontsize=10, title="Months", labels=[
               'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [datetime.strptime(d, '%Y-%m-%d').strftime('%Y') for d in df_box.date]
    df_box['month'] = [datetime.strptime(d, '%Y-%m-%d').strftime('%b') for d in df_box.date]
    df_box.sort_values(by=['year','date'],ascending=[True, False], inplace=True)

    # Draw box plots (using Seaborn)

    fig, (figure1,figure2) = plt.subplots(1,2)
    fig.set_figwidth(20)
    fig.set_figheight(10)
    figure1.set_title('Year-wise Box Plot (Trend)')
    figure1 = sns.boxplot(data=df_box, x='year', y='value', ax=figure1)
    figure1.set_xlabel('Year')
    figure1.set_ylabel('Page Views')

    figure2.set_title('Month-wise Box Plot (Seasonality)')
    figure2 = sns.boxplot(data = df_box, x='month', y='value', order=[
                 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ax=figure2)
    figure2.set_xlabel('Month')
    figure2.set_ylabel('Page Views')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
