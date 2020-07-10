#!/usr/bin/env python
import json
import sys
import requests
import os

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
    import pathlib
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
    import pathlib2
def c_dir(dirname):
    pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)
def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])

# s help
def help(name):
    help = """
Usage:
    python """+name+""" {User} {Options}

Options:
    -h | -H | -help | -HELP  : Open help paragraph.
    -l | -L | -list | -LIST |+| ['.txt' file name]  : In order to save the list of warehouses in one file.
    -d | -D | -download | -DOWNLOAD : Download Repositories from .txt file.
    -a | -A | -about | -ABOUT : View tool information.

    a Number [1-->infinity]  : The number of Repositories that are displayed.
    Repository Name          : Repository View information.

    -u | -U | -update | -UPDATE : soon.
"""
    return help
#e help

# s about
def about():

    logo = """
┌─┐┬ ┬  ┌─┐┬┌┬┐  ┌─┐┬  ┌─┐┌┐┌┌─┐
├─┘└┬┘  │ ┬│ │   │  │  │ ││││├┤ 
┴   ┴   └─┘┴ ┴   └─┘┴─┘└─┘┘└┘└─┘
"""

    a_file = open("version.txt")
    lines = a_file.readlines()
    for line in lines:
        version = "Version : "+line+""
        version_n = line.replace(".", "")
    tool_name = "Tool Name : py_git_clone\n"
    pro_by = "programmed by : byRo0t96\n"
    website = "WebSite : https://byro0t96.github.io/\n"
    github = "Github : https://github.com/byRo0t96/\n"
    email = "E-mail : by.root96@gmail.com\n"
    

    about=logo+"\n"+version+tool_name+pro_by+website+github+email+"\n"+new_version(version_n)+"\n"
    return about
# e about


# s new version
def new_version(version_n):
    url = "https://raw.githubusercontent.com/byRo0t96/py_git_clone/master/version.txt"
    request = requests.get(url)
    if request.status_code == 200:
        response = urlopen(url)
        data = response.read().decode("utf-8")
        data_n = data.replace(".", "")
    else:
        data_n="000"

    if data_n > version_n:
        new_version = "There is a new version of this tool\033[05m "+data+" \033[25m"
    elif data_n == version_n:
        new_version = "You are using the latest version of this tool."
    else:
        new_version = "There are no updates currently."
    return new_version
# e new version


# s download_repo_opt
def download_repo_opt(opt,user,nn):
    if opt=="all" or opt=="ALL":
        url = ("https://api.github.com/users/"+user+"/repos?per_page="+nn)
        # check user
        request = requests.get(url)
        if request.status_code == 200:
            #print (url)
            cls()
            response = urlopen(url)
            data = response.read().decode("utf-8")
            jsondata = json.loads(data)
            r = 0
            for i in jsondata:
                try:
                    n = str(r+1)
                    c_dir(user)
                    repo_name=jsondata[r]["name"]
                    linux = "git clone https://github.com/"+user+"/"+repo_name+".git "+user+"/"+repo_name
                    windows = ''
                    os.system([linux, windows][os.name == 'nt'])
                except ValueError:
                    rep = "ss"
                r = r + 1
    elif opt.isdigit()==True:
        url = ("https://api.github.com/users/"+user+"/repos?per_page="+nn)
        # check user
        request = requests.get(url)
        if request.status_code == 200:
            #print (url)
            cls()
            response = urlopen(url)
            data = response.read().decode("utf-8")
            jsondata = json.loads(data)
            try:
                ssss = int(opt)-1
                #n_opt = opt - 1
                c_dir(user)
                repo_name=jsondata[ssss]["name"]
                linux = "git clone https://github.com/"+user+"/"+repo_name+".git "+user+"/"+repo_name
                windows = ''
                os.system([linux, windows][os.name == 'nt'])
            except ValueError:
                rep = "ss"
# e download_repo_opt


# s get_jsonparsed_data
def get_jsonparsed_data(url,user):
    try:
        response = urlopen(url)
        data = response.read().decode("utf-8")
    except ValueError:
        with open(url, 'r') as json_lical_file:
            data=json_lical_file.read()
    jsondata = json.loads(data)
    rep = ''
    r = 0
    for i in jsondata:
        try:
            n = str(r+1)
            created_at=jsondata[r]["created_at"]
            repo_name=jsondata[r]["name"]
            lang_url="https://api.github.com/repos/"+user+"/"+repo_name+"/languages"
            lang_response = urlopen(lang_url)
            lang_data = lang_response.read().decode("utf-8")
            lang_jsondata = json.loads(lang_data)
            langs=""
            for key in lang_jsondata.keys():
               langs=langs+key+', '

            #rep = rep+"Repository number : "+n+"\nRepository name : "+repo_name+"\nCreated at : "+created_at+"\nlanguages : "+langs+"\n\n"
            rep = "Repository number : "+n+"\nRepository name : "+repo_name+"\nCreated at : "+created_at+"\nlanguages : "+langs+"\n\n"
            print (rep)
            #+str(r+1)+
        except ValueError:
            rep = rep
        r = r + 1
    #return rep
# e get_jsonparsed_data

# s download_list
def download_list(user,txtfile,d_type):
    a_file = open(txtfile)
    lines = a_file.readlines()
    for line in lines:
        if d_type=="split":
            x = line.split(":")
            c_dir(x[0])

            s = x[1].replace("\n", "")

            linux = "git clone https://github.com/"+x[0]+"/"+s+".git "+x[0]+"/"+s
            windows = ''
            os.system([linux, windows][os.name == 'nt'])
            #print(s)

        else:
            c_dir(user)
            s = line.replace("\n", "")
            linux = "git clone https://github.com/"+user+"/"+s+".git "+user+"/"+s
            windows = ''
            os.system([linux, windows][os.name == 'nt'])
# e download_list


# s save_list
def save_list(user,file_name):
    url = ("https://api.github.com/users/"+user+"/repos?per_page=10000")
    # check user
    request = requests.get(url)
    if request.status_code == 200:
        #print (url)
        cls()
        response = urlopen(url)
        data = response.read().decode("utf-8")
        jsondata = json.loads(data)
        rep = ''
        r = 0
        for i in jsondata:
            try:
                n = str(r+1)
                repo_name=jsondata[r]["name"]
                rep = rep+user+":"+repo_name+"\n"
                print(user+":"+repo_name)
            except ValueError:
                rep = rep
            r = r + 1
        c_dir(user)
        file = open(user+"/"+file_name, "w+") 
        file.write(rep) 
        file.close()
        print("The file '"+user+"/"+file_name+"' was created.")

    else:
        cls()
        print('User: "'+user+'" does not exist')
        sys.exit()
# e save_list

# s get_this_repo
def get_this_repo(user,repo_name):

    url="https://api.github.com/repos/"+user+"/"+repo_name
    response = urlopen(url)
    data = response.read().decode("utf-8")
    jsondata = json.loads(data)
    

    created_at=jsondata["created_at"]
    repo_name=jsondata["name"]

    lang_url="https://api.github.com/repos/"+user+"/"+repo_name+"/languages"
    lang_response = urlopen(lang_url)
    lang_data = lang_response.read().decode("utf-8")
    lang_jsondata = json.loads(lang_data)
    
    langs=""
    for key in lang_jsondata.keys():
        langs=langs+key+', '



    rep ="\nRepository name : "+repo_name+"\nCreated at : "+created_at+"\nlanguages : "+langs+"\n"

    return rep
        

# e get_this_repo


# s check argv
def check_argv(argv_n):
    try:
        sys.argv[argv_n]
    except IndexError:
        var_exists = False
    else:
        var_exists = True
    return var_exists
# e check argv


#  s check argv list
x=1
while x < 100:
    if check_argv(x) == True:
        x=x+1
    else:
        break
#  e check argv list



if check_argv(1)==True:
    argv_1=sys.argv[1]
    # help
    if argv_1=="-h" or argv_1=="-H" or argv_1=="-HELP" or argv_1=="-help":
        cls()
        print(help(sys.argv[0]))
    elif argv_1=="-a" or argv_1=="-A" or argv_1=="-ABOUT" or argv_1=="-about":
        cls()
        print(about())
    elif argv_1=="-u" or argv_1=="-U" or argv_1=="-UPDATE" or argv_1=="-update":
        cls()
        print("soon\n")
        sys.exit()
    elif argv_1=="-d" or argv_1=="-D" or argv_1=="-DOWNMOAD" or argv_1=="-download":
        cls()
        try:
            sys.argv[2]
        except IndexError:
            #download_list(user,user+".txt")
            print("\nYou did not enter a file name\n")
        else:
            user="null"
            download_list(user,sys.argv[2],"split")
    # user
    else:
        user = sys.argv[1]
        # default
        if check_argv(2)==False:
            per_page = "?per_page=100"
            url = ("https://api.github.com/users/"+user+"/repos"+per_page)
            # check user
            request = requests.get(url)
            if request.status_code == 200:
                #print (url)
                cls()
                #print(get_jsonparsed_data(url,user))
                get_jsonparsed_data(url,user)
            else:
                cls()
                print('User: "'+user+'" does not exist')
                sys.exit()
        else:
            argv_2=sys.argv[2]
            if argv_2.isdigit()==True:
                per_page = "?per_page="+argv_2
                url = ("https://api.github.com/users/"+user+"/repos"+per_page)
                cls()
                #print(get_jsonparsed_data(url,user))
                get_jsonparsed_data(url,user)
                print('Download (y/n) ! :')
                x = input()
                if x=="y" or x=="Y":
                    print('Download (all/Repository number) ! :')
                    y = input()
                    if y=="all" or y=="ALL" or y.isdigit()==True:
                        download_repo_opt(y,user,argv_2)
                    else:
                        sys.exit()
                else:
                    sys.exit()
            elif argv_2=="-l" or argv_2=="-L" or argv_2=="-LIST" or argv_2=="-list":
                cls()
                try:
                    sys.argv[3]
                except IndexError:
                    save_list(user,user+".txt")
                else:
                    save_list(user,sys.argv[3])
            elif argv_2=="-d" or argv_2=="-D" or argv_2=="-DOWNMOAD" or argv_2=="-download":
                cls()
                try:
                    sys.argv[3]
                except IndexError:
                    #download_list(user,user+".txt")
                    print("\nYou did not enter a file name\n")
                else:
                    download_list(user,sys.argv[3],"no_type")
            else:
                cls()
                print(get_this_repo(user,sys.argv[2]))
                print('Download (y/n) ! :')
                x = input()
                if x=="y" or x=="Y":
                    c_dir(user)
                    linux = "git clone https://github.com/"+user+"/"+sys.argv[2]+".git "+user+"/"+sys.argv[2]
                    windows = ''
                    os.system([linux, windows][os.name == 'nt'])
                else:
                    sys.exit()
else:
    cls()
    print("\nUsage: python "+sys.argv[0]+" {User} {Options}\n\nUse Command: 'python "+sys.argv[0]+" -help' for more information.\n")

