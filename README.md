# py_git_clone

<div align="center">
        <img alt="py_git_clone" src="./Screenshot/Screenshot-1.png"><br>
</div>

'py_git_clone' It is a tool to facilitate browsing the Repositories and download or save a list of them or download a dedicated list ... from the github platform.

<div align="center">
        <a href="https://youtu.be/IAPB1c6lu5w"><img alt="py_git_clone" height="100" src="https://raw.githubusercontent.com/byRo0t96/data/master/images/watch_video.png"></a>
</div>


### Languages :
* python

### System :
* Linux
* windows

# Requirements
[✓] json<br>
[✓] sys<br>
[✓] requests<br>
[✓] os<br>
[✓] for python 3 [urllib,pathlib]<br>
[✓] for python 2 [urllib2,pathlib2]<br>


# How to get this tool from github
## linux
```
git clone https://github.com/byRo0t96/py_git_clone.git
cd py_git_clone
```


# How to run
```
pip install -r requirements.txt
python2 start.py {User} {Options} # for python 2
               OR
python3 start.py {User} {Options} # for python 3
```




# Help
    -h | -H | -help | -HELP  : Open help paragraph.
    -l | -L | -list | -LIST |+| ['.txt' file name]  : In order to save the list of warehouses in one file.
    -d | -D | -download | -DOWNLOAD : Download Repositories from .txt file.
    -a | -A | -about | -ABOUT : View tool information.

    a Number [1-->infinity]  : The number of Repositories that are displayed.
    Repository Name          : Repository View information.

# Usage
In order to view the Repositories information for an account only.
```
python start.py {User}
```

Review a certain number of Repositories.
```
python start.py {User} {a Number }
```

Review a certain number of Repositories.
```
python start.py {User} {a Number }
```

Repository View information.
```
python start.py {User} {Repository}
```

Keep a list of all Repositories and save it as '{User}.txt'
```
python start.py {User} -l
```


Keep a list of all Repositories and save it as 'your_txt_file_name.txt'
```
python start.py {User} -l your_txt_file_name.txt
```

Download the list of Repositories from the same account.
```
python start.py {User} -d repositories_list.txt
```

Download the list of warehouses from separate accounts [.txt file type is (user:Repository).] 
```
python start.py -d repositories_list.txt
```


# SUPPORTED DISTRIBUTIONS
|Distribution | Version Check | supported | status |Everything works|
----------|-------|------|-------|-------|
|Kali Linux|2020.1 | yes | working   | yes|
|windwos|10,8,7 | yes | working   |no|

## Release History
```
- Version 1.0.2 [10-07-2020]
...
```


### Contact :
##### Mail : by.root96@gmail.com

## License
Copyright (C) 2010 - 2020 [byRo0t96](https://byro0t96.github.io/)

<div align="center">
        <a href="https://byro0t96.github.io/"><img alt="byRo0t96" height="100" src="https://raw.githubusercontent.com/byRo0t96/data/master/images/Ro0t-96_v.3.1.png"></a>
</div>

