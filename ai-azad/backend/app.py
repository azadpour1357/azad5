# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from services.search_service import perform_search
from services.document_service import add_document, get_documents, update_document, delete_document
from models.roberta_model import classify_text
from models.t5_model import summarize_text
from models.chatbot_model import generate_response
from services.tax_calculation_service import calculate_tax
from services.ocr_service import extract_text_from_image, extract_text_from_pdf
from utils.db_utils import connect_postgres, connect_redis
import logging

app = Flask(__name__)
CORS(app)

# تنظیمات JWT
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

# سیستم لاگ‌زنی
logging.basicConfig(level=logging.INFO)

# ایجاد جداول PostgreSQL
def init_postgres():
    conn = connect_postgres()
    cursor = conn.cursor()

    with open('create_tables.sql', 'r') as file:
        sql_script = file.read()

    cursor.execute(sql_script)
    conn.commit()
    cursor.close()
    conn.close()

@app.before_first_request
def initialize():
    init_postgres()

# اندپوینت ورود کاربران
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username != 'admin' or password != 'admin123':
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

# اندپوینت جستجو
@app.route('/search', methods=['POST'])
@jwt_required()
def search():
    query = request.json.get('query')
    logging.info(f"Search query received: {query}")
    results = perform_search(query)
    return jsonify(results), 200

# اندپوینت اضافه کردن مستند
@app.route('/add-document', methods=['POST'])
@jwt_required()
def add_document_endpoint():
    data = request.json
    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        return jsonify({"message": "Title and content are required."}), 400

    response = add_document(title, content)
    return jsonify(response), 201

# اندپوینت لیست مستندات
@app.route('/get-documents', methods=['GET'])
@jwt_required()
def get_documents_endpoint():
    documents = get_documents()
    return jsonify(documents), 200

# اندپوینت ویرایش مستند
@app.route('/update-document', methods=['PUT'])
@jwt_required()
def update_document_endpoint():
    data = request.json
    title = data.get('title')
    new_content = data.get('new_content')

    if not title or not new_content:
        return jsonify({"message": "Title and new content are required."}), 400

    response = update_document(title, new_content)
    return jsonify(response), 200

# اندپوینت حذف مستند
@app.route('/delete-document', methods=['DELETE'])
@jwt_required()
def delete_document_endpoint():
    title = request.json.get('title')
    if not title:
        return jsonify({"message": "Title is required."}), 400

    response = delete_document(title)
    return jsonify(response), 200

# اندپوینت طبقه‌بندی متن
@app.route('/classify-text', methods=['POST'])
@jwt_required()
def classify_text_endpoint():
    text = request.json.get('text')
    if not text:
        return jsonify({"message": "Text is required."}), 400

    classification = classify_text(text)
    return jsonify({"classification": classification}), 200

# اندپوینت خلاصه‌سازی متن
@app.route('/summarize-text', methods=['POST'])
@jwt_required()
def summarize_text_endpoint():
    text = request.json.get('text')
    if not text:
        return jsonify({"message": "Text is required."}), 400

    summary = summarize_text(text)
    return jsonify({"summary": summary}), 200

# اندپوینت چت‌بات
@app.route('/chatbot', methods=['POST'])
@jwt_required()
def chatbot_endpoint():
    question = request.json.get('question')
    if not question:
        return jsonify({"message": "Question is required."}), 400

    response = generate_response(question)
    return jsonify({"response": response}), 200

# اندپوینت محاسبه مالیات
@app.route('/calculate-tax', methods=['POST'])
@jwt_required()
def calculate_tax_endpoint():
    income = request.json.get('income')
    tax_rate = request.json.get('tax_rate')

    if not income or not tax_rate:
        return jsonify({"message": "Income and tax rate are required."}), 400

    try:
        income = float(income)
        tax_rate = float(tax_rate)
        tax_amount = calculate_tax(income, tax_rate)
        return jsonify({"tax_amount": round(tax_amount, 2)}), 200
    except ValueError:
        return jsonify({"message": "Invalid input for income or tax rate."}), 400

# اندپوینت OCR
@app.route('/extract-text', methods=['POST'])
@jwt_required()
def extract_text_endpoint():
    file = request.files['file']
    if not file:
        return jsonify({"message": "File is required."}), 400

    if file.content_type.startswith('image'):
        text = extract_text_from_image(file.read())
    elif file.content_type == 'application/pdf':
        text = extract_text_from_pdf(file.read())
    else:
        return jsonify({"message": "Unsupported file type."}), 400

    return jsonify(text), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')