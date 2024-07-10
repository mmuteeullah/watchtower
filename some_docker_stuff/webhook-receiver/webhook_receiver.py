from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    alert = request.json
    print(request.json)
    if alert:
        print("Received alert:", alert)
        return jsonify({"message": "Received alert"}), 200
    else:
        return jsonify({"error": "No JSON received"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
