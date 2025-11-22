from flask import Flask, jsonify, request

app = Flask(__name__)

NOTES = [
    {"id": 1, "title": "Nota de ejemplo", "content": "Contenido de ejemplo"}
]

@app.route('/health', methods=['GET'])
def health():
    """Endpoint de salud.
    Devuelve 200 OK que nos indicaa que la aplicacion esta corriendo.
    """
    return jsonify({"status": "ok"}), 200


@app.route('/notes', methods=['GET'])
def list_notes():
    """Lista todas las notas.
    Este endpoint va ser demostrativo para verificar que la API funciona
    dentro del cluster.
    """
    return jsonify(NOTES), 200


@app.route('/notes', methods=['POST'])
def create_note():
    """Crea una nota nueva en memoria"""
    data = request.get_json() or {}
    title = data.get('title')
    content = data.get('content')
    if not title or not content:
        return jsonify({"error": "title y content son requeridos"}), 400
    new_id = max(n['id'] for n in NOTES) + 1 if NOTES else 1
    note = {"id": new_id, "title": title, "content": content}
    NOTES.append(note)
    return jsonify(note), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
