import os
import zipfile
import pandas as pd
import urllib3
import shutil
import sys

def download_if_needed(url, filename, out=sys.stdout):
    if os.path.exists(filename):
        out.write((filename + ' already exists'))
        return filename + ' already exists'
    else:
        print('downloading', filename)
        http = urllib3.PoolManager()
        with http.request('GET',url, preload_content=False) as resp, open(filename, 'wb') as out_file:
            shutil.copyfileobj(resp, out_file)
            resp.release_conn()


def get_pronto_data():
    download_if_needed('http://s3.amazonaws.com/pronto-data/open_data_year_one.zip', 
                       'open_data_year_one.zip')

def get_trip_data():
    get_pronto_data()
    zf = zipfile.ZipFile('open_data_year_one.zip')
    zf.filelist
    file_handle = zf.open('open_data_year_one/2015_trip_data.csv')
    return pd.read_csv(file_handle)
def get_weather_data():
    get_pronto_data()
    zf = zipfile.ZipFile('open_data_year_one.zip')
    zf.filelist
    file_handle = zf.open('open_data_year_one/2015_weather_data.csv')
    return pd.read_csv(file_handle)

def get_trips_and_weather():
    """
    Clean, process, and join the trips and weather data
    """
    trips = get_trip_data()
    weather = get_weather_data()
    datatime = pd.DatetimeIndex(trips['starttime'])
    trips_by_day = trips.pivot_table('trip_id', aggfunc='count', 
                 index=datatime.date, columns='usertype')
    weather = weather.iloc[:-1]
    weather.index = pd.DatetimeIndex(weather['Date'])
    return weather.join(trips_by_day)


def plot_daily_totals():
    data = get_trips_and_weather()
    fig, ax = plt.subplots(2, figsize=(14, 6), sharex=True)
    data['Annual Member'].plot(ax=ax[0], title='Annual Member')
    data['Short-Term Pass Holder'].plot(ax=ax[1], title='Short-Term Pass Holder')
    fig.savefig('daily_totals.png')

def remove_data():
    """
    deletes cached data, including the zip file
    """
    if os.path.exists('open_data_year_one.zip'):
        os.remove('open_data_year_one.zip')