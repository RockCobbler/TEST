from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/contact')
def contact():
    return render_template('Form.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save data to a CSV file
        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, message])

        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)