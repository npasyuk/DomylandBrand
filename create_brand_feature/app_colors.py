import re

from create_brand_feature import color_util
from create_brand_feature.env import root_project_directory
from data.app_theme import AppTheme


def change_colors(theme: AppTheme, app_key):
    colors_xml_path = f'{root_project_directory}/app/src/{app_key}/res/values/colors.xml'
    change_static_in_all_brand_color(theme, colors_xml_path)
    if theme.only_color_primary:
        set_in_all_color_primary_color(colors_xml_path)
    else:
        change_all_color(theme, colors_xml_path)


def set_in_all_color_primary_color(colors_xml_path):
    _change_colors_file_in_pattern(colors_xml_path, "LightThemePrimaryColor", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "LightThemeSecondaryColor", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "LightThemeTertiaryColor", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "LightThemeAccentColor", "@color/colorPrimary")

    _change_colors_file_in_pattern(colors_xml_path, "DarkThemePrimaryColor", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "DarkThemeSecondaryColor", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "DarkThemeTertiaryColor", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "DarkThemeAccentColor", "@color/colorPrimary")

    _change_colors_file_in_pattern(colors_xml_path, "LightThemeBrandButtonPrimary", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "LightThemeBrandButtonSecondary", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "LightThemeBrandButtonTertiary", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "LightThemeBrandButtonPressed", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "LightThemeBrandAccent", "@color/colorPrimary")

    _change_colors_file_in_pattern(colors_xml_path, "DarkThemeBrandButtonPrimary", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "DarkThemeBrandButtonSecondary", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "DarkThemeBrandButtonTertiary", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "DarkThemeBrandButtonPressed", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "DarkThemeBrandAccent", "@color/colorPrimary")


def change_all_color(theme, colors_xml_path):
    _change_colors_file_in_pattern(colors_xml_path, "LightThemePrimaryColor", theme.brand_button_primary.light)
    _change_colors_file_in_pattern(colors_xml_path, "LightThemeSecondaryColor", theme.brand_button_secondary.light)
    _change_colors_file_in_pattern(colors_xml_path, "LightThemeTertiaryColor", theme.brand_button_tertiary.light)
    _change_colors_file_in_pattern(colors_xml_path, "LightThemeAccentColor", theme.brand_accent.light)

    _change_colors_file_in_pattern(colors_xml_path, "DarkThemePrimaryColor", theme.brand_button_primary.dark)
    _change_colors_file_in_pattern(colors_xml_path, "DarkThemeSecondaryColor", theme.brand_button_secondary.dark)
    _change_colors_file_in_pattern(colors_xml_path, "DarkThemeTertiaryColor", theme.brand_button_tertiary.dark)
    _change_colors_file_in_pattern(colors_xml_path, "DarkThemeAccentColor", theme.brand_accent.dark)

    _change_colors_file_in_pattern(colors_xml_path, "LightThemeBrandButtonPrimary", theme.brand_button_primary.light)
    _change_colors_file_in_pattern(colors_xml_path, "LightThemeBrandButtonSecondary",
                                   theme.brand_button_secondary.light)
    _change_colors_file_in_pattern(colors_xml_path, "LightThemeBrandButtonTertiary", theme.brand_button_tertiary.light)
    _change_colors_file_in_pattern(colors_xml_path, "LightThemeBrandButtonPressed", theme.brand_button_pressed.light)
    _change_colors_file_in_pattern(colors_xml_path, "LightThemeBrandAccent", theme.brand_accent.light)

    _change_colors_file_in_pattern(colors_xml_path, "DarkThemeBrandButtonPrimary", theme.brand_button_primary.dark)
    _change_colors_file_in_pattern(colors_xml_path, "DarkThemeBrandButtonSecondary", theme.brand_button_secondary.dark)
    _change_colors_file_in_pattern(colors_xml_path, "DarkThemeBrandButtonTertiary", theme.brand_button_tertiary.dark)
    _change_colors_file_in_pattern(colors_xml_path, "DarkThemeBrandButtonPressed", theme.brand_button_pressed.dark)
    _change_colors_file_in_pattern(colors_xml_path, "DarkThemeBrandAccent", theme.brand_accent.dark)


def change_static_in_all_brand_color(theme: AppTheme, colors_xml_path):
    color_fingerprint_background = color_util.brighten(30, theme.brand_button_primary.light)
    date_range_color = color_util.brighten(80, theme.brand_button_primary.light)
    _change_colors_file_in_pattern(colors_xml_path, "colorPrimary", theme.brand_button_primary.light)
    _change_colors_file_in_pattern(colors_xml_path, "colorPrimaryDark", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "colorAccent", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "colorFingerprintBackground", color_fingerprint_background)
    _change_colors_file_in_pattern(colors_xml_path, "dateRangeColor", date_range_color)
    _change_colors_file_in_pattern(colors_xml_path, "zhihu_primary", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "zhihu_primary_dark", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "rrr", "@color/colorPrimary")
    _change_colors_file_in_pattern(colors_xml_path, "rrв", "@color/colorPrimary")


def _change_colors_file_in_pattern(path, tag_name, new_value):
    with open(path, 'r') as file:
        content = file.read()
    pattern = re.compile(f'("{tag_name}">)(.*?)(</color>)')
    new_content = pattern.sub(fr'\g<1>{new_value}\g<3>', content)
    with open(path,
              'w') as file:
        file.write(new_content)
