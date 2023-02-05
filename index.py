from flask import Flask, render_template

app = Flask(__name__)  # file is main

# routes
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


# validate yes the __name__ parameter is main
if __name__ == '__main__':
    app.run(debug=True, port=3010)
