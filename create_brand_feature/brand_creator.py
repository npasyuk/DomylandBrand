from data.app_theme import AppTheme
from . import create_product_flavors, create_signing_configs, create_signing_key, replace_res_files
from .app_colors import change_colors
from .change_strings_file import change_app_name, change_all_app_key_in_string_xml
from .copy_branding_folder import copy_folder
from .git_manager import new_working_branch, all_commit_and_push
from .kaiten_data_source import get_ticket_full_name_by_id
from data.brand import Brand


def init(brand: Brand):
    ticket_title = get_ticket_full_name_by_id(brand.ticket_id)
    new_working_branch(ticket_title)
    copy_folder(brand.app_key)
    change_app_name(brand.app_name, brand.app_key)
    change_all_app_key_in_string_xml(brand.app_key)
    create_product_flavors.create(brand.app_key, brand.mindbox_endpoint, brand.app_metrica_key, "true", "false")
    create_signing_configs.create(brand.app_key)
    create_signing_key.create(brand.app_key)
    theme: AppTheme = brand.app_theme
    change_colors(theme, brand.app_key)
    replace_res_files.replace_files(brand.app_key, brand.ticket_id)
    replace_res_files.replace_other_files(brand.app_key, brand.ticket_id)
    all_commit_and_push(ticket_title)
    return ticket_title
