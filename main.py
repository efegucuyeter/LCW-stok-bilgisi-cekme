import os
import sys
import customtkinter as ctk
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from tkinter import filedialog
import threading

def get_chromedriver_path():
    if getattr(sys, 'frozen', False):  
        application_path = sys._MEIPASS  
        chromedriver_path = os.path.join(application_path, 'chromedriver.exe')
    else:
        chromedriver_path = 'chromedriver.exe'
    
    return chromedriver_path

def get_stock_info():
    result_label.configure(text="Başlandı...")

    excel_path = input_textbox.get("1.0", "end-1c").strip()
    data = []

    try:
        df_input = pd.read_excel(excel_path)
        product_urls = df_input['Link'].tolist()

        for product_url in product_urls:
            chrome_driver_path = get_chromedriver_path()

            chrome_options = Options()
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920x1080")  
            chrome_options.add_argument("--start-maximized")  
            chrome_options.add_argument('--disable-dev-shm-usage') 
            chrome_options.add_argument("--no-sandbox")  
            chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")  

            service = Service(chrome_driver_path)
            driver = webdriver.Chrome(service=service, options=chrome_options)

            try:
                driver.get(product_url)
                
                WebDriverWait(driver, 15).until(
                    lambda d: d.execute_script('return document.readyState') == 'complete'
                )

                driver.save_screenshot('page_screenshot.png')

                try:
                    price_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[3]/div/div/div/span"))
                    )
                    price = price_element.text
                except Exception as e:
                    price = "Bulunamadı"

                try:
                    size_elements = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-tracking-label='BedenSecenekleri']"))
                    )

                    unique_sizes = set()
                    for size_element in size_elements:
                        size = size_element.get_attribute("size")
                        stock = size_element.get_attribute("data-stock")

                        if size not in unique_sizes:
                            unique_sizes.add(size)
                            data.append([product_url, price, size, stock])
                except Exception as e:
                    data.append([product_url, price, "Bulunamadı", "Bulunamadı"])

            except Exception as e:
                result_label.configure(text=f"Hata: {e}")
                data.append([product_url, "Bulunamadı", "Bulunamadı", "Bulunamadı"])

            finally:
                driver.quit()

        df_output = pd.DataFrame(data, columns=["Ürün Linki", "Fiyat", "Beden", "Stok"])
        df_output.to_excel("urun_stok_bilgisi.xlsx", index=False)
        result_label.configure(text="Veriler Excel dosyasına kaydedildi.")

    except Exception as e:
        result_label.configure(text=f"Excel dosyası hatası: {e}")

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        input_textbox.delete("1.0", "end")
        input_textbox.insert("1.0", file_path)

def run_in_thread():
    result_label.configure(text="Başlandı...")
    thread = threading.Thread(target=get_stock_info)
    thread.start()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x450")
app.title("Stok Bilgisi Çekme Aracı")

title_label = ctk.CTkLabel(app, text="Excel Dosyası Yolu", font=("Arial", 20))
title_label.pack(pady=20)

input_textbox = ctk.CTkTextbox(app, width=400, height=40)
input_textbox.pack(pady=10)

file_button = ctk.CTkButton(app, text="Dosya Seç", command=select_file)
file_button.pack(pady=10)

start_button = ctk.CTkButton(app, text="Stok Bilgisi Çek", command=run_in_thread)
start_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=20)

footer_label = ctk.CTkLabel(app, text="Efe Gücüyeter tarafından yapılmıştır", font=("Arial", 12))
footer_label.pack(side="bottom", pady=10)

app.mainloop()
