from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


#this is for drowsiness_yawn.py
@app.route('/run_script')
def run_script():
    # execute the drowsiness.py script
    subprocess.call(['python', 'drowsiness_yawn.py'])
    
    # return an empty response
    return ''

if __name__ == "__main__":
    app.run()