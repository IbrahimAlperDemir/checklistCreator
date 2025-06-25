from tinydb import TinyDB, Query
import os

db_path = "form_db.json"
db = TinyDB(db_path)

def get_next_form_number(doc_type: str) -> str:
    Form = Query()
    entry = db.get(Form.type == doc_type)

    if entry:
        next_number = entry["count"] + 1
        db.update({"count": next_number}, Form.type == doc_type)
    else:
        next_number = 1
        db.insert({"type": doc_type, "count": next_number})

    return f"{next_number:04d}"
