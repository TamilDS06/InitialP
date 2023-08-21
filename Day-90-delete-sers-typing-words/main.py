from flask import Flask, render_template, jsonify, request
import threading
import time
from pynput import keyboard

app = Flask(__name__)

last_key_time = 0
typing_stopped_time = 0
user_input = ""
lock = threading.Lock()

def on_key_press(key):
    global last_key_time, typing_stopped_time
    last_key_time = time.time()
    typing_stopped_time = 0

def monitor_typing_activity():
    global last_key_time, typing_stopped_time, user_input
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

    while True:
        current_time = time.time()
        if current_time - last_key_time > 5:
            typing_stopped_time += 1
            if typing_stopped_time >= 5:
                with lock:
                    user_input = ""
        else:
            typing_stopped_time = 0
        time.sleep(1)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_user_input")
def get_user_input():
    global user_input
    with lock:
        return jsonify(user_input=user_input)

@app.route("/update_user_input", methods=["POST"])
def update_user_input():
    global user_input
    data = request.json
    with lock:
        user_input = data["user_input"]
    return jsonify(success=False)

if __name__ == "__main__":
    typing_thread = threading.Thread(target=monitor_typing_activity)
    typing_thread.daemon = True
    typing_thread.start()
    
    app.run(debug=True)
