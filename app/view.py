import json

from flask import Flask, request, jsonify, Response
from app.celery_worker import process_message

app = Flask(__name__)


@app.route('/webhook/<string:user_uuid>', methods=['GET', 'POST'])
def webhook(user_uuid):
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == "12345":
            return Response(request.args.get('hub.challenge'), content_type="text/plain")
        return Response("Verification token mismatch", status=403, content_type="text/plain")

    elif request.method == 'POST':
        try:
            data = json.loads(request.data.decode('utf-8'))
            print(f"no print: {data}")
            process_message.delay(data)
            return jsonify({"status": "received"}), 202
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON"}), 400
