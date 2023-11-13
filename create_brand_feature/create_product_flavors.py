from create_brand_feature.env import root_project_directory


def create(app_key, mindbox_endpoint, app_metrica_branding_key, has_dark_theme, only_dark_theme):
    cloneable_text = f'''        {app_key} {{
            dimension "base"
            applicationId 'ru.domyland.{app_key}'
            signingConfig signingConfigs.{app_key}
            buildConfigField "String", "MINDBOX_ENDPOINT", '{mindbox_endpoint}'
            buildConfigField "String", "APP_METRICA_BRANDING_API_KEY", '{app_metrica_branding_key}'
            buildConfigField "boolean", "HAS_DARK_THEME", "{has_dark_theme}"
            buildConfigField "boolean", "ONLY_DARK_THEME", "{only_dark_theme}"
        }}'''

    # Открываем файл на чтение и получаем все строки в виде списка
    with open(f"{root_project_directory}/app/product_flavors.gradle", "r") as file:
        lines = file.readlines()

    # Ищем заданный текст в каждой строке и сохраняем номер первой найденной строки
    for i, line in enumerate(lines):
        if "new_home {" in line:
            line_number = i
            break

    # Вставляем новый текст между строкой, предшествующей заданному тексту, и самим заданным текстом
    new_text = f"{cloneable_text}\n"
    lines.insert(line_number, new_text)

    # Открываем файл на запись и записываем измененные строки
    with open(f"{root_project_directory}/app/product_flavors.gradle", "w") as file:
        for line in lines:
            file.write(line)
