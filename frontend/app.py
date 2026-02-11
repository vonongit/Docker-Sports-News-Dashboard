from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # This serves the actual visual dashboard to the user
    return render_template('index.html')

if __name__ == '__main__':
    # Listen on port 3000 so it doesn't clash with the backend
    app.run(host='0.0.0.0', port=3000)