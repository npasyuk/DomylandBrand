import dataclasses

from data import app_theme
from data.app_theme import AppTheme


@dataclasses.dataclass
class Brand:
    app_key: str
    app_name: str
    ticket_id: str
    app_metrica_key: str
    mindbox_endpoint: str
    app_theme: AppTheme


def fromJson(data):
    return Brand(app_key=data['app_key'], app_name=data['app_name'],
                 ticket_id=data['ticket_id'], app_metrica_key=data['app_metrica_key'],
                 mindbox_endpoint=data['mindbox_endpoint'],
                 app_theme=app_theme.fromJson(data['app_theme']))
