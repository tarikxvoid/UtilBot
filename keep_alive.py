from flask import Flask
import threading

app = Flask('')

@app.route('/')
def home():
    return "Utility Bot made by unkn0wn_sh4d0w succesfully started on the Provided Host and Port!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()
    