from urllib.parse import urljoin

import httpx
from config import settings
from services.template import get_template_service


def welcome_letter(event_data: dict) -> dict:
    print(event_data)
    payload = event_data['payload']
    user_id: str = payload['user_id']
    event_type: str = event_data['event_type']

    response = httpx.get(f"{settings.url_auth_service}/notification/{user_id}")
    json_data = response.json()

    # Template
    service = get_template_service()
    template = service.get_template_by_event_type(event_type=event_type)

    return {
        "context": {
            **payload,
            "first_name": json_data["first_name"],
            "last_name": json_data["first_name"],
            "email": json_data["email"]
        },
        "template_id": template.id
    }


handlers = {
    "welcome_letter": welcome_letter
}
