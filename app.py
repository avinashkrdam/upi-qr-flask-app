
from flask import Flask, render_template
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/')
def show_qr():
    # ✅ Final UPI Payment Link with ₹500 and 91club name
    upi_link = "upi://pay?pa=BHARATPE.8H0o0Q8D0N01452@fbpe&pn=91club&am=500&cu=INR"

    # Generate QR Code
    qr = qrcode.make(upi_link)
    img_io = io.BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)
    img_base64 = base64.b64encode(img_io.read()).decode('ascii')

    return render_template('index.html', qr_code=img_base64)

if __name__ == '__main__':
    app.run(debug=True)
