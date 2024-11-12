from bs4 import BeautifulSoup as bs
import random
import time
import pandas as pd
import undetected_chromedriver as uc
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
    url = f'https://www.idealista.com/venta-viviendas/barcelona-barcelona/pagina-{x}.htm'
    browser.implicitly_wait(10)
    browser.get(url)
    browser.implicitly_wait(10)

    try:         
        browser.find_element("xpath", '//*[@id="didomi-notice-agree-button"]').click()
    except:
        pass
    
    html = browser.page_source
    soup = bs(html, 'html.parser')

    # Check if the current page number matches the one displayed in pagination
    try:         
        pagina_actual = int(soup.find('main', {'class': 'listing-items'}).find('div', {'class': 'pagination'}).find('li', {'class': 'selected'}).text)
    except AttributeError:
        print("Error: Could not find the pagination element.")
        break

     
    # Fetch the articles if the current page matches
     
    if x == pagina_actual:        
        articles = soup.find('main', {'class': 'listing-items'}).find_all('article')         
    else:
        break
     
    if not articles:
        print("No more apartments found.")
        break  # Stop if no articles are found
     
    for article in articles:         
        id_muebles = article.get('data-element-id')
         
        # Título y enlace
        link = article.find('a', {'class': 'item-link'})
        title = link.get_text(strip=True) if link else "No disponible"
        href = link['href'] if link else "No disponible"
        full_link = f"https://www.idealista.com{href}" if href != "No disponible" else href
        
        # Precio
        price = article.find('span', {'class': 'item-price'})
        price_text = price.get_text(strip=True) if price else "No disponible"
         
        # Detalles adicionales
        details = article.find('div', {'class': 'item-detail-char'})
        details_text = details.get_text(" | ", strip=True) if details else "No disponible"
         
        # Descripción
        description = article.find('p', {'class': 'ellipsis'})
        description_text = description.get_text(strip=True) if description else "No disponible"
         
        # Añadir los datos al DataFrame
        new_row = pd.DataFrame({
            'ID': [id_muebles],  # Wrap the scalar in a list
            'Título': [title],
            'Enlace': [full_link],
            'Precio': [price_text],
            'Detalles': [details_text],
            'Descripción': [description_text]
        })
        
        print(new_row)        
        
        df = pd.concat([df, new_row], ignore_index=True)
         
        # Escribir en el CSV después de cada artículo
        df.to_csv(csv, mode="a", index=False, header=False)
         
        # Pausa aleatoria para evitar sobrecargar el servidor
        time.sleep(random.randint(1, 3))

    # Check for the 'next' page link to stop if there are no more pages     
    next_page = soup.find('a', {'class': 'icon-arrow-right-after'})     
    if next_page is None:         
        print("No more pages to scrape.")         
        break  # Stop if there's no 'next' page link
     
    # Move to the next page
    x += 1

