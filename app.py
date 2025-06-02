from flask import Flask, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def generate_qr():
    # Static UPI Info
    upi_id = "BHARATPE.8H0o0Q8D0N01452@fbpe"
    name = "91club"
    amount = 500

    # UPI payment URL
    upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"

    # Generate QR Code
    qr = qrcode.make(upi_url)
    buf = io.BytesIO()
    qr.save(buf, format='PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')
