from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_base64 = None
    if request.method == 'POST':
        upi_id = request.form['upi_id']
        name = request.form['name']
        amount = request.form['amount']
        upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"
        qr = qrcode.make(upi_url)
        buf = io.BytesIO()
        qr.save(buf, format='PNG')
        qr_code_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    return render_template('index.html', qr_code=qr_code_base64)

if __name__ == '__main__':
    app.run(debug=True)
