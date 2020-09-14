import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

DAYS_DATA = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all']
MONTHS_DATA = ['january', 'february', 'march', 'april', 'may', 'june','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter the city(chicago, new york city, washington): ")
        if city not in CITY_DATA.keys():
            print("Invalid Input: Please Chosse from this (chicago, new york city, washington)!!!")
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter The month if you want specific month, otherwise Enter 'all' for all months\n")
        if month not in MONTHS_DATA:
            print("Invalid Input: Please Enter month of first 6 months in the year or 'all'!!!")
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter The day if you want specific day (monday, tuesday, ... sunday), otherwise Enter 'all' for all days\n")
        if day.lower() not in DAYS_DATA:
            print("Invalid Input: Please Enter Correct Day Name!!!")
        else:
            break

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    mc_month = df['month'].mode()[0]
    print("The most common month:", mc_month)

    # display the most common day of week
    mc_day = df['day_of_week'].mode()[0]
    print("The most common day:", mc_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    
    mc_hour = df['hour'].mode()[0]
    print("The most common hour:", mc_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mc_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station: \t\"{mc_start_station}\".")

    # display most commonly used end station
    mc_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station: \t\"{mc_end_station}\".\n")

    # display most frequent combination of start station and end station trip
    start, end =df[['End Station','Start Station']].value_counts().index[0]
    print(f"The most frequent combination of start station and end station trip: \n\t---> \"{start}\" and \"{end}\".")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time: ", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    users = user_types.index
    user_count = user_types.values

    print("counts of user types:")
    for t, count in zip(users, user_count):
        print(t,'\t',count)
    print('\n'+('-'*20)+'\n')

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_c = df['Gender'].value_counts()
        genders = gender_c.index
        genders_count = gender_c.values

        print("counts of user gender:")
        for g, count in zip(genders, genders_count):
            print(g,'\t',count)
    
    else:
        print("There is no 'Gender' Column!!!")
    print('\n'+('-'*20)+'\n')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]

        print("Earliest Year Of Birth:\t\t", earliest_birth)
        print("Most Recent Year Of Birth:\t", most_recent_birth)
        print("Most Common Year Of Birth:\t", most_common_birth)
    else:
        print("There is no 'Birth Year' Column!!!")

    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
