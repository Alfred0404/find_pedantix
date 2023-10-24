import csv
import itertools
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://cemantix.certitudes.org/pedantix")



def brute_force_search(path, word_lenght) :

    search_bar = driver.find_element(By.ID, "pedantix-guess")

    with open(path, 'r') as file :
        reader = csv.reader(file)

        for row in reader :
            word = row[0]

            if len(word) == word_lenght:
                search_bar.clear()
                search_bar.send_keys(word)
                search_bar.send_keys(Keys.RETURN)
                time.sleep(0.03)

                if "Mot trouvé" in driver.page_source:
                    print("Mot trouvé :", word)
                    break

    driver.quit()

brute_force_search("mots.txt", 4)