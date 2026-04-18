from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import time

options = Options()

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

def get_product_from_flipkart(a , b , c):

    url = f"https://www.flipkart.com/search?q={a}+{b}+GB+{c}+GB storage"
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    try:
        cross = wait.until(
            ec.element_to_be_clickable((By.XPATH, "//button[contains(text() , '✕')]"))
        )
        cross.click()
        
    except:
        print("Cross does not found")
    
        result = []
        whole_div = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR , '.jIjQ8S' )))
        for  idx ,  div  in enumerate(whole_div):
            name = div.find_element(By.CSS_SELECTOR , '.RG5Slk').text
            product_link = div.find_element(By.CSS_SELECTOR , '.k7wcnx').get_attribute("href")
            price_reference = div.find_element(
                        By.XPATH, ".//div[contains(@class , 'hZ3P6w ')]"
                    ).text
            result.append({"Name":name , "Price":price_reference , "Site":"Flipkart" , "Specification" :"Go through link for specification" , "Product Link": product_link})
            if idx == 4:
                break
    
    return result

def get_product_from_amazon(name, ram, storage):
    query = f"{name} {ram}GB {storage}GB".replace(" ", "+")
    url = f"https://www.amazon.in/s?k={query}"
    
    driver.get(url)
    wait = WebDriverWait(driver, 15)
    amazon_results = []

    try:
      
        items = wait.until(ec.presence_of_all_elements_located((By.XPATH , "//div[@class = 'a-section']")))

        for idx, item in enumerate(items):
            if idx == 5: break
            
            try:
                
                p_name = item.find_element(By.CSS_SELECTOR, "h2.a-spacing-none.a-color-base span").text
                
                try:
                    p_price = item.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
                except:
                    p_price = "N/A"
                    
                try:
                    product_link = item.find_element(By.CSS_SELECTOR , '.a-link-normal.s-no-outline').get_attribute('href')
                except:
                    product_link = "N/A"
                amazon_results.append({
                    "Site": "Amazon",
                    "Name": p_name,
                    "Price": f"₹{p_price}",
                    "Specification" :"Go through link for specification" , 
                    "Product Link" : product_link
                })
               

            except:
                continue
        return amazon_results
    except Exception as e:
        return []

Mobile_name = input("Enter mobile name: ")
Enter_ram = input("Enter how much ram do you want: ")
Enter_storage = input("Enter how much storage you want in GB: ")


data = get_product_from_flipkart(Mobile_name , Enter_ram , Enter_storage)
amazon_data = get_product_from_amazon(Mobile_name, Enter_ram, Enter_storage)
all_data = data + amazon_data

if all_data:
    df = pd.DataFrame(all_data)
    file_name = "price-comparison.xlsx"
    
    links_list = df['Product Link'].tolist()
    df['Product Link'] = "" 
    
    writer = pd.ExcelWriter(file_name, engine="xlsxwriter")
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    
    workbook = writer.book 
    worksheet = writer.sheets['Sheet1']
    
    link_format = workbook.add_format({
        'font_color': 'blue',
        'underline': 1,
        'font_size': 10
    })

    try:
        link_col_idx = df.columns.get_loc("Product Link")
        for row_num, link_url in enumerate(links_list):
            if link_url and str(link_url).startswith('http'):
                
                formula = f'=HYPERLINK("{link_url}", "Click to Open")'
                worksheet.write_formula(row_num + 1, link_col_idx, formula, link_format)
            else:
                worksheet.write(row_num + 1, link_col_idx, "No Link")
    except Exception as e:
        print(f"Excel Error: {e}")

   
    worksheet.set_column(link_col_idx, link_col_idx, 20)
    writer.close()
    print(f"\nFile ready: {file_name}")
else:
    print("nothing found")
driver.quit()
