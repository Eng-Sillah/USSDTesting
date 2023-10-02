from flask import Flask, request

app = Flask(__name__)

@app.route('/ussd', methods=['GET', 'POST'])
def ussd_callback():
    session_id = request.values.get("sessionId")
    service_code = request.values.get("serviceCode")
    phone_number = request.values.get("phoneNumber")
    text = request.values.get("text")

    # Your USSD logic goes here

if __name__ == '__main__':
    app.run(debug=True)
