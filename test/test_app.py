import json
import sys
from pathlib import Path

# Aseguramos que el directorio raiz del proyecto este en sys.path para poder localizar el paquete `app`
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import app


def test_health():
    client = app.test_client()
    resp = client.get('/health')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data.get('status') == 'ok'


def test_list_notes():
    client = app.test_client()
    resp = client.get('/notes')
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
