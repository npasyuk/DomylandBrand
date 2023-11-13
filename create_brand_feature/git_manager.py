import git

from create_brand_feature.env import root_project_directory

directory_path = f"{root_project_directory}"


def new_working_branch(ticket_title):
    repo = git.Repo(directory_path)
    print(ticket_title)
    repo.git.fetch()
    current_branch = repo.active_branch.name
    main_local_branch = None
    for branch in repo.branches:
        if branch.name == "brand":
            main_local_branch = branch
            break

    if current_branch != "brand":
        _delete_main_branch(main_local_branch, repo)
        repo.git.checkout("brand")
        _create_work_branch_and_checkout(ticket_title, repo)
    else:
        new_branch = repo.create_head("temp_brand_creator_branch", "brand")
        repo.head.reference = new_branch
        repo.head.reset(index=True, working_tree=True)
        _delete_main_branch(main_local_branch, repo)
        repo.git.checkout("brand")
        repo.delete_head("temp_brand_creator_branch", force=True)
        _create_work_branch_and_checkout(ticket_title, repo)


def _create_work_branch_and_checkout(ticket_title, repo):
    repo.create_head(ticket_title, "brand")
    repo.git.checkout(ticket_title)


def _delete_main_branch(main_local_branch, repo):
    if main_local_branch:
        repo.delete_head(main_local_branch, force=True)


def all_commit_and_push(ticket_title):
    repo = git.Repo(directory_path)
    repo.git.add(all=True)  # Добавление всех неотслеживаемых файлов
    repo.index.commit(ticket_title)  # Создание коммита
    repo.git.push('--set-upstream', 'origin', ticket_title)


def remove_working_branch(ticket_title):
    repo = git.Repo(directory_path)
    repo.git.add(all=True)
    repo.index.commit(ticket_title)
    repo.git.checkout("brand")
    repo.delete_head(ticket_title, force=True)
