"""Import in Python helps you to refer to the code, i.e., .functions/objects 
that are written in another file. It is also used to import python libraries/packages 
are installed using pip(python package manager), and you need then to use in your code.
"""
import time
import pandas as pd
import numpy as np
 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
 
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
 
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    #list of three cities Chicago, New York City and Washington
    city = ''
    while city not in ['Chicago', 'New York City', 'Washington']:
        city = input('Choose one of the cities above:\n').title()
 
 
    #tuple of months including the all option
    month = input("\nWhich month are you looking at? January, February, March, April, May, June or type 'all' if dont have a choice?").title()
    while month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
        month = input("Sorry, I didn't find your choice. Try again.\n").title()
 
 
    #tuple of days including the all option
    day = input("\nWhich day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or type  'All' if you  dont have a choice?").title()
    while day not in ('Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday','Saturday', 'Sunday'):
        day = input("Sorry, I didn't find your choice. Try again.\n").title()
 
 
    print('-'*40)
    return city, month, day
 
 
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
 
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
        
    """
    df = pd.read_csv(CITY_DATA[city.lower()])
 
    # converting Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
 
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    #data['Date'].dt.weekday_name
    #data['Start Time'].dt.weekday_name
 
    # filter by month
    if month != 'all':
 
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        
        # creating dataframe for month
        df = df[df['month'] == month]
 
        if day != 'all':
            df = df[df['day_of_week'] == day.title()]
    
 
    return df
 
 
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
 
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
 
    
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)
 
 
    
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)
 
 
    
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)
 
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
 
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
 
    
    start_station = df['Start Station'].value_counts().idxmax()
 
    
    end_station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', end_station)
 
 
    combination_of_station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', start_station, " & ", end_station)
 
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
 
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
 
    
    totaltime = sum(df['Trip Duration'])
    print('Total travel time:', totaltime / 86400, " Days")
 
 
    meantime = df['Trip Duration'].mean()
    print('Mean travel time:', meantime / 60, " Minutes")
 
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def user_stats(df):
    """Displays statistics on bikeshare users."""
 
    print('\nCalculating User Stats...\n')
    start_time = time.time()
 
    
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)
 
 
    
    try:
        gender_types = df['Gender'].value_counts()
        print('\nGender Types:\n', gender_types)
    except KeyError:
        print("\nGender Types:\nNo data available for this month.")
 
 
    try:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year:', earliest_year)
    except KeyError:
        print("\nEarliest Year:\nNo data available for this month.")
 
    try:
        most_recent_year = df['Birth Year'].max()
        print('\nMost Recent Year:', most_recent_year)
    except KeyError:
        print("\nMost Recent Year:\nNo data available for this month.")
 
    try:
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', most_common_year)
    except KeyError:
        print("\nMost Common Year:\nNo data available for this month.")
 
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
 
 """   Displays 5 rows of data from the csv file for the selected city.
    Args:
        (df): The data frame you wish to work with.
    Returns:
        None."""
    
 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
 
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        while True:
            viewData = input("Would you like to see the raw data? Type 'Yes' or 'No'.")
            if viewData == "Yes":
                row = 0
                print(df[row:row+5])
                row += 5
            else:
                break
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
 
 
if __name__ == "__main__":
	main()
 
 
