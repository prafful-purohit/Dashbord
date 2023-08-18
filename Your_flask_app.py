# from flask import Flask, render_template , redirect, url_for, request

# app = Flask(__name__)


# # @app.route('/')
# # def home():
# #     return render_template('home.html')

# # 

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def render_form():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Process form data if needed
    # For demonstration purposes, we'll simply redirect to index.html
    return redirect(url_for('render_index'))

@app.route('/index2')
def render_index():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)


