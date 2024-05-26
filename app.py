from flask import Flask, render_template, request, redirect, url_for
import csv

# Specify the current directory as the templates folder
app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('Home.html')  # Ensure 'Home.html' matches the exact filename

@app.route('/contact')
def contact():
    return render_template('Form.html')  # Ensure 'Form.html' matches the exact filename

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
    app.run(debug=False, host='0.0.0.0')
