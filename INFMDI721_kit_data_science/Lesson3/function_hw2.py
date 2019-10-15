def stars_mean(g, user_pseudo):
    repos = g.get_user(user_pseudo).get_repos()
    total_stars = 0
    for repo in repos:
        total_stars +=repo.stargazers_count
    # in case repos do not have any stars
    if repos.totalCount == 0:
        print(user_pseudo)
        result = 0
    else:
        result = total_stars/repos.totalCount
    return result