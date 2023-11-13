import logging
import os.path
import shutil
import zipfile

from flask import Flask, jsonify, request, abort, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename

import check_auth
import create_brand_feature.brand_creator
from create_brand_feature.clear_all_resources import clear_all_resource
from create_brand_feature.env import new_project_resource_directory
from data import brand
from data.custom_error import CustomError

app = Flask(__name__)
CORS(app)

# logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

ticket_number = None


@app.after_request
def log_request(response):
    with open('app.log', 'a') as f:
        f.write('Request: {} {}\n'.format(request.method, request.url))
        f.write('Response: {}\n\n'.format(response.status_code))
    return response


@app.errorhandler(CustomError)
def handle_custom_error(error):
    return {"errorMessage": error.message, "result": "false"}, error.status_code


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/api/brand_creator/auth', methods=['POST'])
def auth():
    data = request.get_json()
    ticket_title = check_auth.get_ticket_full_name_by_id(data.get('ticket_id'))
    check_auth.check_access_key(data.get("access_key"))
    response = {'result': 'success', 'data': {'ticket_title': ticket_title}}
    return jsonify(response)


@app.route('/api/brand_creator/upload_resource', methods=['POST'])
def upload_resource():
    global file_name
    ticket_id = request.values.get('ticket_id')
    root_folder_path = f'{new_project_resource_directory}/{ticket_id}'
    if not os.path.exists(root_folder_path):
        os.makedirs(root_folder_path)
    upload_files = request.files.getlist('file')
    for file in upload_files:
        file_name = secure_filename(file.filename)
        file.save(os.path.join(root_folder_path, file_name))
        with zipfile.ZipFile(f'{root_folder_path}/{file_name}', 'r') as zip_ref:
            zip_ref.extractall(root_folder_path)
        shutil.move(f'{root_folder_path}/{os.path.splitext(os.path.basename(f"{root_folder_path}/{file_name}"))[0]}',
                    f'{root_folder_path}/resource')
    response = {'result': 'success', 'data': {'file_name': file_name}}
    return jsonify(response)


@app.route('/api/brand_creator/create', methods=['POST'])
def create():
    new_brand = None
    try:
        request_data = request.get_json()
        new_brand = brand.fromJson(request_data)
        title: str = create_brand_feature.brand_creator.init(new_brand)
        response = {'result': 'success', 'data': {'message': f'Ветка с брендингом: {title}'}}
        return jsonify(response)
    except Exception:
        if new_brand is not None:
            clear_all_resource(new_brand.ticket_id)
        raise CustomError("Произошла ошибка при создании брендинга попробуйте еще раз", 400)


if __name__ == '__main__':
    app.run(port=8000)
