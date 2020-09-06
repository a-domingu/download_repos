import git, os

def _url_last_chunk(url):
    """Get last chunk form url, i.e. part after last '/'"""
    return url[url.rfind("/")+1:]

def _complete_url(site):
    """Expand string s withouth 'http' prefix to http://github.com/{s} and strip last '/'"""
    if _url_last_chunk(site) == '':
        site = site[:-1]
    if not site[:4] == 'http':
        return f'https://github.com/{site}'
    else:
        return site   

def parse_urls_from_text(txt):
    """Parse multi-line text into list of git repo urls, optionally prefixed with http://github.com/ and strip ultimate '/'"""
    fragments = txt.split('\n')
    sites = [s.strip() for s in fragments if len(s.strip()) > 0]
    return [_complete_url(s) for s in sites]

def download_repos(lst_repos, to_base_path):
    """Clone list of git repos with depth=1 (no history); all to base path. Url of the repo name may not contain ending '/'"""
    res = []
    for repo in lst_repos:
        to_path = os.path.join(to_base_path, _url_last_chunk(repo))
        res.append(git.Repo.clone_from(repo, to_path, depth=1))
    return res

def clone_repos(lst_repos, to_base_path):
    """Clone list of git repos; all to base path. Url of the repo name may not contain ending '/'"""
    res = []
    for repo in lst_repos:
        to_path = os.path.join(to_base_path, _url_last_chunk(repo))
        res.append(git.Repo.clone_from(repo, to_path))
    return res

