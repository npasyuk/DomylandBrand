import shutil

from create_brand_feature.env import root_project_directory


def copy_folder(app_key):
    original_folder_path = f"{root_project_directory}/app/src/new_home"
    new_folder_path = f"{root_project_directory}/app/src/" + app_key
    shutil.copytree(original_folder_path, new_folder_path)
