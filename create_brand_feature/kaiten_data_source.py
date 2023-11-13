import requests as requests


def get_ticket_full_name_by_id(card_id):
    endpoint = f"https://domyland.kaiten.ru/api/latest/cards/{card_id}"
    headers = {"Authorization": "Bearer 2378df77-efc6-484f-828a-6bf37e38bdea"}
    a = requests.get(endpoint, headers=headers)
    ticket_title = a.json().get("title")
    ticket_full_name = f"#{card_id} {ticket_title}"
    ticket_full_name = ticket_full_name.replace(" ", "_")
    return ticket_full_name
