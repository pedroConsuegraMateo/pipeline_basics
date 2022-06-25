from m_acquisition import m_acquisition as mac
from m_wrangling import m_wrangling as mwr
from m_analysis import m_analysis as man

input_year = input('Introduzca el año de fabricación: ')
input_year = int(input_year)

# pipeline
if __name__ == '__main__':
    df_raw = mac.acquisition('./data/vehicles.csv')
    df_wrangled = mwr.wrangling(df_raw, input_year)
    result = man.analysis(df_wrangled, 'Make', 'Combined MPG', './data/result.csv')


