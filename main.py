import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def request_1():
    """Produce scatterplot by csv"""
    stats = pd.read_csv('D:\\coding\\python\\world_trend\\world_trend.csv')
    stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']
    scatter = sns.scatterplot(data=stats[['BirthRate','InternetUsers', 'IncomeGroup']], x="BirthRate", y="InternetUsers", hue="IncomeGroup")
    plt.show()


def main():
    """main function"""
    request_1()


main()