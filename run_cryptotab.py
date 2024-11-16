from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Path ke lokasi ChromeDriver yang telah Anda unduh
driver_path = "path_to_your_chromedriver"

# URL CryptoTab
url = "https://cryptotabbrowser.com/"

# Fungsi untuk menjalankan CryptoTab di setiap profil
def run_cryptotab(profile_name):
    # Menyiapkan opsi untuk setiap profil
    options = Options()
    options.add_argument(f"user-data-dir=path_to_your_browser_profiles/{profile_name}")
    
    # Membuka Chrome dengan profil tertentu
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    
    # Buka URL CryptoTab
    driver.get(url)
    
    # Tunggu beberapa detik untuk memastikan halaman dimuat
    time.sleep(10)

    # Anda bisa menambahkan langkah-langkah lainnya di sini seperti login, memulai mining, dll.
    print(f"CryptoTab dimulai pada profil {profile_name}")
    
    # Menunggu beberapa waktu untuk mining
    time.sleep(3600)  # 1 jam, bisa diatur sesuai kebutuhan
    
    # Menutup browser setelah sesi selesai
    driver.quit()

# Jalankan CryptoTab di 10 profil berbeda
for i in range(1, 11):
    run_cryptotab(f"profile_{i}")
