from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('https://www.scrapethissite.com/pages/ajax-javascript/  ')

years = [2012, 2013, 2014, 2015]

for year in years:
    year_button = driver.find_element(By.ID, str(year))
    year_button.click()

    table = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "table")))
    wait.until(lambda driver: len(driver.find_elements(By.CLASS_NAME, "film")) > 0)
    films = driver.find_elements(By.CLASS_NAME, "film")
    
    films_data = []
    
    for film in films:
        title = film.find_element(By.CLASS_NAME, "film-title").text.strip()
        
        nominations = film.find_element(By.CLASS_NAME, "film-nominations").text.strip()
        awards = film.find_element(By.CLASS_NAME, "film-awards").text.strip()
        
        nominations = int(nominations)
        awards = int(awards)
        
        film_info = {
            "year": year,
            "title": title,
            "nominations": nominations,
            "awards": awards
        }
        films_data.append(film_info)

    filename = f"films_{year}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(films_data, f, indent=4, ensure_ascii=False)
    
    print(f"Сохранен файл: {filename} с {len(films_data)} фильмами")

print("Готово") 

driver.quit()
