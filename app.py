from flask import Flask, render_template, request, session, redirect, url_for
import pandas as pd
import random
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.permanent_session_lifetime = timedelta(minutes=2)

@app.route('/')
def index():
    session.permanent = True
    return render_template('index.html')

@app.route('/transaction', methods=['POST'])
def transaction():
    sender = request.form['sender']
    receiver = request.form['receiver']
    amount = request.form['amount']
    remarks = request.form['remarks']
    date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Load reference numbers from Excel
    reference_df = pd.read_excel('reference_numbers.xlsx')
    reference_number = random.choice(reference_df['Reference Number'].tolist())

    # Load transaction IDs from Excel
    transaction_df = pd.read_excel('transaction_ids.xlsx')
    transaction_id = random.choice(transaction_df['Transaction Id'].tolist())

    return render_template('transaction.html', 
                           sender=sender, 
                           receiver=receiver, 
                           amount=amount, 
                           remarks=remarks, 
                           date_time=date_time, 
                           reference_number=reference_number,
                           transaction_id=transaction_id)

if __name__ == '__main__':
    app.run(debug=True)