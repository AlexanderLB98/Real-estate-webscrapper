from bs4 import BeautifulSoup as bs
import random
import time
import pandas as pd

import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

import time


browser = uc.Chrome()

url2= 'https://www.idealista.com/venta-viviendas/barcelona-barcelona/'
browser.get(url2)


browser.implicitly_wait(10)
busqueda = 'barcelona'
csv = "scraped_data-" + busqueda + ".csv"

# busqueda = input("Introduce City: ")
busqueda = busqueda.replace(' ', '-')
x = 1
ids = []
df = pd.DataFrame(columns=['ID', 'Título', 'Enlace', 'Precio', 'Detalles', 'Descripción'])
df.to_csv(csv, mode="a", index=False, header=True)



while True:
    time.sleep(random.randint(1, 6))
    url = f'https://www.idealista.com/venta-viviendas/barcelona-barcelona/pagina-{x}.htm'
    browser.implicitly_wait(10)
    browser.get(url)
    browser.implicitly_wait(10)


    try:
        time.sleep(random.randint(1, 6))
        browser.find_element("xpath", '//*[@id="didomi-notice-agree-button"]').click()
    except:
        time.sleep(random.randint(1, 6))
        pass
    
    time.sleep(random.randint(1, 6))
    html = browser.page_source
    time.sleep(random.randint(1, 6))
    soup = bs(html, 'html.parser')
    time.sleep(random.randint(1, 6))

    # Check if the current page number matches the one displayed in pagination
    try:
        time.sleep(random.randint(1, 6))
        pagina_actual = int(soup.find('main', {'class': 'listing-items'}).find('div', {'class': 'pagination'}).find('li', {'class': 'selected'}).text)
        time.sleep(random.randint(1, 6))
    except AttributeError:
        time.sleep(random.randint(1, 6))
        print("Error: Could not find the pagination element.")
        time.sleep(random.randint(1, 6))
        break

    time.sleep(random.randint(1, 6))
    # Fetch the articles if the current page matches
    time.sleep(random.randint(1, 6))
    if x == pagina_actual:
        time.sleep(random.randint(1, 6))
        articles = soup.find('main', {'class': 'listing-items'}).find_all('article')
        time.sleep(random.randint(1, 6))
    else:
        time.sleep(random.randint(1, 6))
        break
    
    time.sleep(random.randint(1, 6))
    if not articles:
        time.sleep(random.randint(1, 6))
        print("No more apartments found.")
        time.sleep(random.randint(1, 6))
        break  # Stop if no articles are found

    time.sleep(random.randint(1, 6))
    for article in articles:
        time.sleep(random.randint(1, 6))
        id_muebles = article.get('data-element-id')
        time.sleep(random.randint(1, 6))

        # Título y enlace
        link = article.find('a', {'class': 'item-link'})
        time.sleep(random.randint(1, 6))
        title = link.get_text(strip=True) if link else "No disponible"
        time.sleep(random.randint(1, 6))
        href = link['href'] if link else "No disponible"
        time.sleep(random.randint(1, 6))
        full_link = f"https://www.idealista.com{href}" if href != "No disponible" else href
        time.sleep(random.randint(1, 6))
        
        # Precio
        price = article.find('span', {'class': 'item-price'})
        time.sleep(random.randint(1, 6))
        price_text = price.get_text(strip=True) if price else "No disponible"
        time.sleep(random.randint(1, 6))

        # Detalles adicionales
        details = article.find('div', {'class': 'item-detail-char'})
        time.sleep(random.randint(1, 6))
        details_text = details.get_text(" | ", strip=True) if details else "No disponible"
        time.sleep(random.randint(1, 6))

        # Descripción
        description = article.find('p', {'class': 'ellipsis'})
        time.sleep(random.randint(1, 6))
        description_text = description.get_text(strip=True) if description else "No disponible"
        time.sleep(random.randint(1, 6))

        # Añadir los datos al DataFrame
        new_row = pd.DataFrame({
            'ID': [id_muebles],  # Wrap the scalar in a list
            'Título': [title],
            'Enlace': [full_link],
            'Precio': [price_text],
            'Detalles': [details_text],
            'Descripción': [description_text]
        })
        time.sleep(random.randint(1, 6))
        print(new_row)
        time.sleep(random.randint(1, 6))
        
        df = pd.concat([df, new_row], ignore_index=True)
        time.sleep(random.randint(1, 6))
        
        # Escribir en el CSV después de cada artículo
        df.to_csv(csv, mode="a", index=False, header=False)
        time.sleep(random.randint(1, 6))
        
        # Pausa aleatoria para evitar sobrecargar el servidor
        time.sleep(random.randint(1, 3))

    # Check for the 'next' page link to stop if there are no more pages
    time.sleep(random.randint(1, 6))
    next_page = soup.find('a', {'class': 'icon-arrow-right-after'})
    time.sleep(random.randint(1, 6))
    if next_page is None:
        time.sleep(random.randint(1, 6))
        print("No more pages to scrape.")
        time.sleep(random.randint(1, 6))
        break  # Stop if there's no 'next' page link

    time.sleep(random.randint(1, 6))
    # Move to the next page
    x += 1

