from flask import Blueprint, request, jsonify
from chatbot_module.service import chat

chatbot_bp = Blueprint("chatbot", __name__, url_prefix="/chat")

@chatbot_bp.route("/", methods=["POST"])
def chat_endpoint():
    data = request.get_json()
    message = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "Mensaje vacío"}), 400
    return jsonify({"reply": chat(message)})