from create_brand_feature.env import root_project_directory


def create(app_key):
    cloneable_text = f'''        {app_key} {{
            keyAlias '{app_key}'
            keyPassword 'reHuIdd123'
            storeFile file('../{app_key}.jks')
            storePassword 'reHuIdd123'
        }}'''

    # Открываем файл на чтение и получаем все строки в виде списка
    with open(f"{root_project_directory}/app/signing_configs.gradle", "r") as file:
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
    with open(f"{root_project_directory}/app/signing_configs.gradle", "w") as file:
        for line in lines:
            file.write(line)
