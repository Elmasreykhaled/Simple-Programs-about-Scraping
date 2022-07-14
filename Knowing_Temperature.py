import requests
from bs4 import BeautifulSoup

try:
    page = requests.get(
        'https://www.arabiaweather.com/ar/%D8%AA%D9%88%D9%82%D8%B9%D8%A7%D8%AA-%D8%A7%D9%84%D8%B7%D9%82%D8%B3/%D8%A7%D9%84%D9%82%D8%A7%D9%87%D8%B1%D8%A9/488/eg')
    content = page.content
    soup = BeautifulSoup(content, 'html.parser')
    day = soup.find('div', class_='day-part white')
    Date = day.find('span', class_='date').get_text()
    day_Temperature = day.find(
        'p', class_='font-42 trans temp-container ltr').get_text()
    night = soup.find('div', class_='night-part white')
    night_Temperature = night.find(
        'p', class_='font-42 trans temp-container ltr').get_text()
    print("Welcome in our small program\n")
    print(f"The Date of Today is {Date}\n")
    print(f"The Temperature at day-part is {day_Temperature[:-1]}\n")
    print(f"The Temperature at night-part is {night_Temperature[:-1]}\n")
    print("Have a good day")
except:
    print("Please cheack your internet and try again later")
