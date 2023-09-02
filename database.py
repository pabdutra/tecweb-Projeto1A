import sqlite3
from dataclasses import dataclass



@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name+'.db')
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL)''')
        self.conn.commit()

    def add(self, note):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO note (title, content) VALUES (?, ?)''', (note.title, note.content))
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.cursor()
        cursor = self.conn.execute('''SELECT id, title, content FROM note''')
        notes = []
        for r in cursor:
            note = Note(id=r[0], title=r[1], content=r[2])
            notes.append(note)
        return notes
    
    def get(self, note_id):
        cur = self.conn.cursor()
        cursor = cur.execute("SELECT id, title, content FROM note WHERE id = ?", (note_id,))
        note = [(Note(linha[0], linha[1], linha[2])) for linha in cursor]
        return note[0]
    
    def update(self, entry):
        cursor = self.conn.cursor()
        cursor.execute('''UPDATE note SET title= ?, content= ? WHERE id= ?''', (entry.title, entry.content, entry.id))
        self.conn.commit()

    def delete(self, note_id):
        cursor = self.conn.cursor()
        cursor.execute('''DELETE FROM note WHERE id = ?''', (note_id,))
        self.conn.commit()