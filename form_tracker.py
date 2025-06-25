from tinydb import TinyDB, Query
import os

DB_PATH = "form_db.json"
db = TinyDB(DB_PATH)

def get_next_form_number(doc_type: str) -> str:
    Form = Query()
    result = db.search(Form.type == doc_type)

    if result:
        current = result[0]['counter'] + 1
        db.update({'counter': current}, Form.type == doc_type)
    else:
        current = 1
        db.insert({'type': doc_type, 'counter': current})

    return str(current).zfill(3)  # Örn: 001, 002

def reset_form_number(doc_type: str):
    Form = Query()
    db.remove(Form.type == doc_type)

# ❗ İlk çalıştırmadan önce form_db.json dosyasının bulunduğu klasörde olduğuna emin olun.
