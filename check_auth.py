import requests as requests
from flask import Response

from data.custom_error import CustomError


def get_ticket_full_name_by_id(card_id):
    endpoint = f"https://domyland.kaiten.ru/api/latest/cards/{card_id}"
    headers = {"Authorization": "Bearer 2378df77-efc6-484f-828a-6bf37e38bdea"}
    a = requests.get(endpoint, headers=headers)
    if a.status_code != 200:
        raise CustomError("Такой задачи не существет", 403)
    ticket_title = a.json().get("title")
    ticket_full_name = f"#{card_id} {ticket_title}"
    ticket_full_name = ticket_full_name.replace(" ", "_")
    return ticket_full_name


def check_access_key(access_key):
    if access_key != "Q40Khc":
        raise CustomError("Неверный ключ", 401)
