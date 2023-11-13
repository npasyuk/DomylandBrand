import os
import shutil

from create_brand_feature.env import root_project_directory, new_project_resource_directory


# Функция для замены файлов
def replace_files(app_key, ticket_id):
    source_folder = f'{new_project_resource_directory}/{ticket_id}/resource'
    target_folder = f'{root_project_directory}/app/src/{app_key}/res'
    for root, dirs, files in os.walk(source_folder):
        relative_path = os.path.relpath(root, source_folder)
        target_path = os.path.join(target_folder, relative_path)

        # Создаем соответствующую папку в целевом каталоге, если ее нет
        os.makedirs(target_path, exist_ok=True)

        # Копируем и заменяем файлы
        for file in files:
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_path, file)

            # Заменяем файлы с одинаковыми именами
            shutil.copy2(source_file, target_file)


def replace_other_files(app_key, ticket_id):
    path_a = f'{new_project_resource_directory}/{ticket_id}/resource/other'
    path_b = f'{root_project_directory}/app/src/{app_key}'
    other_folder = f'{root_project_directory}/app/src/{app_key}/res/other'

    for root, dirs, files in os.walk(path_b):
        for file in files:
            # Полный путь к текущему файлу в папке Б
            current_file = os.path.join(root, file)
            # Полный путь к соответствующему файлу в папке А
            corresponding_file = os.path.join(path_a, file)
            # Если файл с таким же названием существует в папке А
            if os.path.exists(corresponding_file):
                # Заменяем файл в папке Б файлом из папки А
                shutil.copy2(corresponding_file, current_file)
    shutil.rmtree(other_folder)
