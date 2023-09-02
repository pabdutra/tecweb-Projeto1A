import os
from pathlib import Path
from database import Database, Note



CUR_DIR = Path(__file__).parent
db = Database('data/banco')

def extract_route (request):
    return request.split()[1][1:] if len(request.split()) > 1 else ""

def read_file(path):
    return open(path, 'rb').read()

def load_data():
    notes = db.get_all()
    return notes

def load_data_id(id):
    note = db.get(id)
    return note.title, note.content

def add_data(data):
    db.add(Note(title=data[0], content=data[1]))

def update_data(data):
    db.update(Note(id=data[0], title=data[1], content=data[2]))

def delete_data(id):    
    db.delete(id)

def load_template(template_filename):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'templates', template_filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    return data

def build_response(body='', code=200, reason='OK', headers=''):
    status_line = f'HTTP/1.1 {code} {reason}\n'
    response_headers = headers if headers else 'Content-Type: text/html\n'
    response = f'{status_line}{response_headers}\n{body}'
    return response.encode()