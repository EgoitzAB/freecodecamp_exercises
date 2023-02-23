#!/usr/bin/python3

import pandas as pd

data = 'adult.data.csv'

def demographic_analyzer(print_responses=True):
    """ Function to analyze and get the required values from FCC exercise """
    df = pd.read_csv(data)
    #Update the code so all variables set to "None" are set to the appropriate calculation or code
    df.fillna(method='ffill', inplace=True)
    #How many people of each race are represented in this dataset? This should be a
    #Pandas series with race names as the index labels. (race column)
    race_counting = (df['race'].value_counts()).to_string(index=False)
    #What is the average age of men?
    men_age_average = df[df['sex'] == 'Male']['age'].mean().round(1)
    #What is the percentage of people who have a Bachelor's degree?
    bachelor_degree_per = df['education'].value_counts(normalize=True).mul(100).round(1)['Bachelors']
    #What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education= df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_earning_high = advanced_education['salary'].value_counts(normalize=True).mul(100).round(1)['>50K']
    #What percentage of people without advanced education make more than 50K?
    low_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_earning_low = low_education['salary'].value_counts(normalize=True).mul(100).round(1)['>50K']
    #What is the minimum number of hours a person works per week?
    minimum_hours_week = df['hours-per-week'].min()
    #What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    percentage_high_salary = df[df['hours-per-week'] == 1]['salary'].value_counts(normalize=True).mul(100).round(1)['>50K']
    #What country has the highest percentage of people that earn >50K and what is that percentage?
    country_more_50k = df[df['salary'] == '>50K']['native-country'].mode()
    country_and_per_more_50k = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True).mul(100).round(1)[country_more_50k].to_string()
    #Identify the most popular occupation for those who earn >50K in India.
    india = df[df['native-country'].str.contains('India')]#['salary'] == '>50K'
    indian_plus_50 = india[india['salary'] == '>50K']['occupation'].mode().to_string(index=False)

    #print if true, and return dict for better testing.

    if print_responses:
        print("How many people of each race are represented in this dataset?\n", race_counting)
        print("What is the average age of men?\n", men_age_average)
        print("What is the percentage of people who have a Bachelor's degree?\n", bachelor_degree_per)
        print("What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?\n", percentage_earning_high)
        print("What percentage of people without advanced education make more than 50K?\n", percentage_earning_low)
        print("What is the minimum number of hours a person works per week?\n", minimum_hours_week)
        print("What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?\n", percentage_high_salary)
        print("What country has the highest percentage of people that earn >50K and what is that percentage?\n", country_and_per_more_50k)
        print("Identify the most popular occupation for those who earn >50K in India.\n", indian_plus_50)

    return {
    'race_count': race_counting,
    'average_age_men': men_age_average,
    'bachelors_degree_per': bachelor_degree_per,
    'percentage_high_earning_high_edu': percentage_earning_high,
    'percentage_high_earning_low_edu': percentage_earning_low,
    'min_work_hours_week': minimum_hours_week,
    'rich_percentage': percentage_high_salary,
    'highest_earning_country': percentage_high_salary,
    'highest_earning_country_percentage':
    country_and_per_more_50k,
    'high_salary_occupation_India': indian_plus_50
    }

if __name__=='__main__':
    demographic_analyzer()
