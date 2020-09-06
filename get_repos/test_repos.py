from get_repos import parse_urls_from_text, download_repos
import os, pytest, shutil


@pytest.fixture
def workspace():
    path = os.path.join(os.getcwd(), '__downloaded__')
    if not os.path.isdir(path):
        os.mkdir(path)
    yield path  
    try:
        shutil.rmtree(path)
    except Exception as ex:
        print(ex)

def test_parse_urls_from_text():
    assert parse_urls_from_text("https://github.com/devonfw/devon4ng\n    \ndevonfw/devon4j/     \n     ") == ["https://github.com/devonfw/devon4ng", "https://github.com/devonfw/devon4j"] 

def test_download_repo(workspace):
    res = download_repos(['https://github.com/devonfw/getting-started'], workspace)    
    assert len(res) == 1
    assert os.path.isfile(os.path.join(workspace, 'getting-started/devonfw_getting_started.pdf')) == True 

