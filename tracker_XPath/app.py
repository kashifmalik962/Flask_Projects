from flask import Flask, render_template, request, jsonify
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.action_chains import ActionChains
# from webdriver_manager.chrome import ChromeDriverManager
import time
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load_url', methods=['POST'])
def load_url():
    # url = request.form['url']
    # global driver
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.get(url)
    # return ""
    return jsonify({'status': 'URL Loaded'}) 

@app.route('/save_xpath', methods=['POST'])
def save_xpath():
    xpath = request.form['xpath']
    with open('xpaths.txt', 'a') as file:
        file.write(f"{[xpath]},\n")
    return 'XPath saved', 200

@app.route('/get_html', methods=['GET'])
def get_html():
    global driver
    return driver.page_source

def close_driver():
    global driver
    if driver:
        driver.quit()

if __name__ == '__main__':
    driver = None
    app.run(debug=True)
    threading.Thread(target=close_driver).start()