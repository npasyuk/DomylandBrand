import dataclasses

from data import theme_color
from data.theme_color import ThemeColor


@dataclasses.dataclass
class AppTheme:
    only_color_primary: bool
    brand_button_primary: ThemeColor
    brand_button_secondary: ThemeColor
    brand_button_tertiary: ThemeColor
    brand_button_pressed: ThemeColor
    brand_accent: ThemeColor


def fromJson(data):
    return AppTheme(only_color_primary=data['only_color_primary'],
                    brand_button_primary=theme_color.fromJson(data['brand_button_primary']),
                    brand_button_secondary=theme_color.fromJson(data['brand_button_secondary']),
                    brand_button_tertiary=theme_color.fromJson(data['brand_button_tertiary']),
                    brand_button_pressed=theme_color.fromJson(data['brand_button_pressed']),
                    brand_accent=theme_color.fromJson(data['brand_accent']))
