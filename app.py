from flask import Flask, render_template,redirect,url_for
from tracker import get_stats,start_track,stop_track,reset
from Keylogger import start_log,clear_log
app=Flask(__name__)

@app.route("/")
def home():
    s=get_stats()
    return render_template("index.html",stats=s)

@app.route("/start")
def start_counter():
    start_log()
    start_track()
    return redirect(url_for("home"))

@app.route("/stop") 
def stop_counter():
    stop_track()
    return redirect(url_for("home"))

@app.route("/reset")
def reset_counter():
    reset()
    clear_log()
    return redirect(url_for("home"))

if __name__=="__main__":
    app.config["PROPAGATE_EXCEPTIONS"] = False
    app.run(debug=False, use_reloader=False)
