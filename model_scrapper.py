import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


base_url = 'https://polyhedra.tessera.li/'

def find_polyhedra_links(driver):
    driver.get(base_url)

    # Wait for the page to load and the polyhedra to be displayed
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'a'))) 

    # Find all polyhedra ids
    all_links = driver.find_elements(By.TAG_NAME, 'a')  
    ids = []
    for p in all_links:
        # print('='*75)
        # print(f'WebElement: \t{p}')
        # print(f'CLASS: \t\t{p.get_attribute('class')}')
        # print(f'ID: \t\t{p.get_attribute('id')}')
        # print(f'HREF: \t\t{p.get_attribute('href')}')
        # print()
        
        if p.get_attribute('id'):
            ids.append(p.get_attribute('id').replace('-', '_'))
        
    return ids

def download_obj(driver: webdriver.Firefox, polyhedra_name: str, output_dir: str):
    driver.get(base_url + polyhedra_name + '/info')
    
    download_buttons = driver.find_elements(By.CLASS_NAME, '_14pkh80')
    
    for link in download_buttons:
        if '.obj' in link.get_attribute('download'):
            obj_url = link.get_attribute('href')
            output_path = output_dir + polyhedra_name.replace('-', '_') + '.obj'

            driver.get(obj_url)
            with open(output_path, 'wb') as f:
                obj_contents = str(driver.page_source.encode('utf-8'), encoding='utf-8')
                obj_contents = obj_contents[obj_contents.find('v') : obj_contents.find('<')]
                f.write(obj_contents)
            print(f"Downloaded {obj_url} to {output_path}")
            

if __name__ == '__main__':
    # Set up Selenium WebDriver for Firefox
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    
    webdriver_service = Service('/usr/local/bin/geckodriver')  

    # Create the driver
    driver = webdriver.Firefox(service=webdriver_service, options=firefox_options)
    wait = WebDriverWait(driver, 10)
    
    # Find the polyhedra for extraction
    polyhedra_names = find_polyhedra_links(driver)
    for id in polyhedra_names:
        print(f'id: {id}')
        
    # Visit each link, downloading the .obj
    output_dir = 'resources/'
    os.makedirs(output_dir, exist_ok=True)
    for id in polyhedra_names:
        download_obj(driver, id, output_dir)
    
    driver.quit()