from create_brand_feature.brand_resources import remove_resource_by_ticket_id
from create_brand_feature.git_manager import remove_working_branch
from create_brand_feature.kaiten_data_source import get_ticket_full_name_by_id


def clear_all_resource(ticket_id):
    branch_name = get_ticket_full_name_by_id(ticket_id)
    remove_resource_by_ticket_id(ticket_id)
    remove_working_branch(branch_name)
