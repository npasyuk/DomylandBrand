import shutil

from create_brand_feature.env import new_project_resource_directory


def remove_resource_by_ticket_id(ticket_id):
    ticket_source_folder = f'{new_project_resource_directory}/{ticket_id}'
    shutil.rmtree(ticket_source_folder)
