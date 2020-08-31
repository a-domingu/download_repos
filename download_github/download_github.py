import git
import os
import sys
'''

def funcion(x):
    return x**2


if __name__ == '__main__':
    try:
        x = float(sys.argv[1])
    except IndexError:
        print('inserte un número')
        x = float(input())
    y = funcion(x)
    print(y)

'''

def get_files(item):
    #'item' can either be a .txt file or the name of a Github repostitory
    if item.endswith('.txt'):
        with open(item) as file:
            for line in file:
                download(line)
    else: #this means that 'item' is the name of a git repository
        download(item)

def download(repo):
    start = 'https://github.com/'
    if not repo.startswith(start):
        index = repo.find('/')
        name = repo[index+1:]
        repo = start + repo
    else: #we need to get the name of the repo so that we can create the directory
        i = -1
        while True: 
            if repo[i] == '/':
                name = repo[i+1:]
                break
            else:
                i -= 1
    #now we can create the directory in our main directory with the name 'name'
    path = os.path.join(os.getcwd(), 'Downloaded_repos')
    print(path)
    print(name)
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    #and now we finally create a folder within 'Downloaded_repos' with the name 'name' and that clones the repo
    new_path = os.path.join(path, name)
    print('##############################')
    print(new_path)
    os.mkdir(new_path)
    git.Repo.clone_from(repo, new_path, depth=1)



if __name__ == '__main__':
    if len(sys.argv) > 1:
        for item in sys.argv[1:]:
            get_files(item)
    else:
        x = input()
        y = x.split(' ')
        for item in y:
            get_files(item)
