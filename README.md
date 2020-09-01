# Download_repos

This is a program in Python which clones any Github repository we pass to the program, and 
will be downloaded in a folder in our directory. 

This folder is called **Downloaded_repos** and it contains in separate folder each repository that we've cloned. 

We can pass as many repos as arguments to our program, as long as these are valid names of repos, and it will clone all of them to our Downloaded_repos folder. 

# Usage

This program can be used in several ways.

One way to do it is to execute the program by itself, and another one will be to use it as a package for another Python script or for a Jupyter notebook. We'll explain both of these options later on. 

## Usage from the command line

There are several different ways we can call our program with its arguments from the commnand line. 

### .txt files

One way to do it is to pass it one (or more) **.txt files**. This file should contain in each line the name of a repository. 

**Note**: this should be a valid file contained in our current directory when we run the program.

Our porgram accepts two possible ways of naming the repository. It can either have the full URL, or it can just be the repo with the username of the author. So:

```
https://github.com/a-domingu/download_repos
a-domingu/download_repos
```
Are two perfectly valid ways of cloning the same repository.

So, in short, one possible way to run our program would be to run `python download_repos.py repos.txt` from our terminal, and this `repos.txt` file may contain something looking like this:

```
a-domingu/download_repos
https://github.com/vinta/awesome-python
tensorflow/models
...
```

### Passing the name of the repository

Instead of passing the name of a file in our directory, we can pass the name of the repositories directly to the program. These should simply be separated by a space so that our program can recognize them as different repos, and the format can also be as we explained in the last subsection.

So another possibility would be to call our program as:

```
python download_repos.py a-domingu/download_repos vinta/awesome-python https://github.com/tensorflow/models
```

### Combination of these last two ways

Lastly, any combination of .txt files and valid inputs of Github repos will be accepted by our program. So ir our arguments are `repos.txt a-domingu/download_repos`, our program will both read this `repos.txt`, download the repos whose names are contained in this file, and also clone `a-domingu/download_repos`.

### What if we pass no arguments?

If we simply call our program, without passing in any input, as `python download_repos.py` from our terminal, our program will still run correctly, but it will ask us to type one or more valid Github repositories, or a .txt file (separated by a space), and it will proceed to clone these repos.

## Usage as a package

