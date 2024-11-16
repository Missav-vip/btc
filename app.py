from flask import Flask, render_template, jsonify, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

# Fungsi untuk mengambil saldo CryptoTab berdasarkan user_id
def get_crypto_balance(user_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Jalankan tanpa tampilan
    driver = webdriver.Chrome(options=chrome_options)

    # Gunakan URL dengan ID pengguna yang relevan
    driver.get(f'https://cryptotabbrowser.com/{user_id}')  # Link berdasarkan user_id yang diberikan
    time.sleep(5)  # Tunggu halaman memuat

    # Ambil saldo (gantilah ID elemen saldo yang relevan)
    try:
        balance = driver.find_element_by_id('balance_id').text  # Sesuaikan ID elemen saldo
    except:
        balance = "Gagal mengambil saldo"
    driver.quit()

    return balance

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/get_balance', methods=['GET'])
def get_balance():
    user_id = request.args.get('user_id')  # Ambil ID pengguna dari parameter URL
    if user_id:
        balance = get_crypto_balance(user_id)
        return jsonify({'saldo': balance})
    else:
        return jsonify({'error': 'User ID tidak diberikan'}), 400

if __name__ == "__main__":
    app.run(debug=True)
