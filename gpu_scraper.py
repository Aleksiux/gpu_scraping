import time

from bs4 import BeautifulSoup
import requests


page_range = range(1, 9)


def gpu_scraping(gpu_that_needed):
    for n in page_range:
        url = f'https://pigu.lt/lt/kompiuterine_technika/kompiuteriu_komponentai/vaizdo_plokstes_vga?page={n}'
        source = requests.get(url)
        soup = BeautifulSoup(source.content, 'html.parser')
        cards = soup.find_all('div', {'class': 'product-item-inner heightResponse'})

        for card in cards:
            try:
                gpu_name = card.find('p', class_='product-name').text.strip()
                full = card.find('div', class_='product-price')
                getting_price = full.find('span', class_='price notranslate').text.strip()
                replacing_price_euro = getting_price.replace("€", "")
                full_price_fix = replacing_price_euro.replace(" ", "")
                full_price = full_price_fix[:-2] + "." + full_price_fix[-2:]
                if gpu_that_needed in gpu_name:
                    new_dict = {
                        'GPU': gpu_name,
                        'GPU_price': float(full_price)
                    }
                    gpu.append(new_dict)
            except AttributeError:
                pass

    gpu.sort(key=lambda x: x["GPU_price"])
    for dictionary in gpu:
        print(dictionary)


while True:
    choise = input("Write from 1-2 what you want to do:\n1.-Search for gpu\n2.-End program\n")
    if choise == "1":
        gpu = []
        gpu_that_needed = input("Write gpu that you want to search:\n")
        gpu_scraping(gpu_that_needed)
    elif choise == "2":
        print("Program ended job")
        time.sleep(3)
        break
    else:
        print("You can only choose from 1 - 2")
