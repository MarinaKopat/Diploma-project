import base64
import json


def get_user_id_from_jwt(token: str):
    try:
        parts = token.split('.')
        if len(parts) < 2:
            return None
        payload_b64 = parts[1] + "==="
        payload_json = base64.b64decode(payload_b64).decode('utf-8')
        return json.loads(payload_json).get("sub")
    except Exception as e:
        print(f"Ошибка декодирования токена: {e}")
        return None
