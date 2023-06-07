from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def form():
    return render_template('form.html')

@app.route("/schedule")
def schedule():
    return render_template('schedule.html')

@app.route("/boxscore/<team>")
def boxscore(team):
    return render_template('boxscore.html', team=team)

if __name__ == "__main__":
    app.run()