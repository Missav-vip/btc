from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Path ChromeDriver yang sesuai dengan sistem Anda
chrome_driver_path = "path/to/chromedriver"

# Opsi untuk membuka Chrome tanpa tampilan GUI
chrome_options = Options()
chrome_options.add_argument("--headless")  # Menjalankan Chrome tanpa GUI
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Fungsi untuk membuka CryptoTab dengan profil yang berbeda
def open_cryptotab_with_profile(profile_path):
    # Menambahkan profil yang sudah ada
    chrome_options.add_argument(f"user-data-dir={profile_path}")  # Path ke profil Chrome
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
    driver.get("https://cryptotab.net/")

    # Tunggu beberapa detik untuk memastikan halaman dimuat sepenuhnya
    time.sleep(10)  # Menunggu 10 detik agar CryptoTab dimuat

    # Menutup browser setelah selesai
    driver.quit()

# Menjalankan CryptoTab dengan 10 profil yang berbeda
profiles = ["path/to/profile1", "path/to/profile2", "path/to/profile3", 
            "path/to/profile4", "path/to/profile5", "path/to/profile6", 
            "path/to/profile7", "path/to/profile8", "path/to/profile9", 
            "path/to/profile10"]

# Menjalankan fungsi untuk setiap profil
for profile in profiles:
    open_cryptotab_with_profile(profile)
