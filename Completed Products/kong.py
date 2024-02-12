import json
from docx import Document
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

# Open the Word file
doc = Document('datalist.docx')

# Open the Jomashop website

array1 = []
array2 = []
array3 = []

for table in doc.tables:
    for row in table.rows:
        driver = webdriver.Chrome()
        product_name = row.cells[0].text
        product_price = row.cells[1].text

        print(product_name, product_price)
        driver.get("https://www.jomashop.com/search?q=" + product_name)
        wait = WebDriverWait(driver,20)
        results = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "productItem")))
        
        if len(results) == 1:
            text = driver.find_element(By.CLASS_NAME,"now-price").find_elements(By.TAG_NAME,"span").pop().text
            price = driver.find_elements(By.CLASS_NAME,"after-price")
            if len(price):
                text = price[0].text.split()[0]
            print(text)
            if text != product_price:
                array1.append(product_name)
        elif len(results)==0:
            array2.append(product_name)
        else:
            array3.append(product_name)
        driver.close()
        

print("1 -> ", array1)
print("0 -> ", array2)
print("other -> ", array3)

data = {
    "the price is incorrect":array1,
    "no product":array2,
    "multiple products":array3
}

# Specify the file path where you want to save the JSON data
file_path = "data.json"

# Save the JSON data to a file
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)