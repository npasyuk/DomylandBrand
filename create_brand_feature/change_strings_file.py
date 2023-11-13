import re

from create_brand_feature.env import root_project_directory


def change_app_name(app_name, app_key):
    with open(f'{root_project_directory}/app/src/{app_key}/res/values/strings.xml',
              'r') as file:
        content = file.read()
    pattern = re.compile(r'("app_name">)(.*?)(</string>)')
    new_content = pattern.sub(fr'\g<1>{app_name}\g<3>', content)
    with open(f'{root_project_directory}/app/src/{app_key}/res/values/strings.xml',
              'w') as file:
        file.write(new_content)


def change_all_app_key_in_string_xml(app_key):
    with open(f'{root_project_directory}/app/src/{app_key}/res/values/strings.xml',
              'r') as file:
        content = file.read()
    pattern = re.compile(r'newhome+')
    new_content = re.sub(pattern, app_key, content)
    with open(f'{root_project_directory}/app/src/{app_key}/res/values/strings.xml',
              'w') as file:
        file.write(new_content)
