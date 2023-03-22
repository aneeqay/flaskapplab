from flask import Flask, render_template
from controllers.book_controller import tasks_blueprint

app = Flask(__name__)

app.register_blueprint(tasks_blueprint)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
