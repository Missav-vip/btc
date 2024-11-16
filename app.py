from flask import Flask, render_template, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

# Fungsi untuk mengambil saldo CryptoTab
def get_crypto_balance():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Jalankan tanpa tampilan
    driver = webdriver.Chrome(options=chrome_options)

    # Akses CryptoTab dan login
    driver.get('https://cryptotab.net')
    time.sleep(5)  # Tunggu halaman memuat

    # Login ke akun
    login_button = driver.find_element_by_xpath("//button[text()='Login']")
    login_button.click()

    time.sleep(2)

    username_field = driver.find_element_by_id("username")
    password_field = driver.find_element_by_id("password")
    username_field.send_keys('your_username')  # Gantilah dengan username Anda
    password_field.send_keys('your_password')  # Gantilah dengan password Anda

    submit_button = driver.find_element_by_xpath("//button[text()='Login']")
    submit_button.click()

    time.sleep(5)

    # Ambil saldo (gantilah ID elemen saldo yang relevan)
    balance = driver.find_element_by_id('balance_id').text  # Sesuaikan ID elemen saldo
    driver.quit()

    return balance

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/get_balance')
def get_balance():
    balance = get_crypto_balance()
    return jsonify({'saldo': balance})

if __name__ == "__main__":
    app.run(debug=True)
