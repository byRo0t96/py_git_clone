#!/usr/bin/env python
import json
import sys
import requests
import os
import pathlib

#import git
#sudo apt install git-all


try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

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
    -h | -H | -help | -Help  : Open help paragraph.
    a Number [1-->infinity]  : The number of Repositories that are displayed.
    Repository Name          : Repository View information.
"""
    return help
#e help

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
            #repo_lang=jsondata[r]["clone_url"]
            

            lang_url="https://api.github.com/repos/"+user+"/"+repo_name+"/languages"
            lang_response = urlopen(lang_url)
            lang_data = lang_response.read().decode("utf-8")
            lang_jsondata = json.loads(lang_data)
            
            langs=""
            for key in lang_jsondata.keys():
               langs=langs+key+', '

            rep = rep+"Repository number : "+n+"\nRepository name : "+repo_name+"\nCreated at : "+created_at+"\nlanguages : "+langs+"\n\n"
            #+str(r+1)+
        except ValueError:
            rep = rep
        r = r + 1
    return rep
# e get_jsonparsed_data

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
    if argv_1=="-h" or argv_1=="-H" or argv_1=="-Help" or argv_1=="-help":
        cls()
        print(help(sys.argv[0]))
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
                print(get_jsonparsed_data(url,user))
            else:
                cls()
                print('User: "'+user+'" does not exist')
                sys.exit()
        else:
            if sys.argv[2].isdigit()==True:
                per_page = "?per_page="+sys.argv[2]
                url = ("https://api.github.com/users/"+user+"/repos"+per_page)
                cls()
                print(get_jsonparsed_data(url,user))
            else:
                cls()
                print(get_this_repo(user,sys.argv[2]))
                print('Download (y/n) ! :')
                c_dir(user)
                #os.system("git clone https://github.com/"+user+"/"+sys.argv[2]+".git "+user+"/"+sys.argv[2])
                #git.Git(user+"/").clone("git://github.com/"+user+"/"+sys.argv[2]+".git")
                #x = input(vv)
                #if vv=="y" or vv=="Y":
                #    print('soon')
                #else:
                #    print('hahah')
else:
    cls()
    print("\nUsage: python "+sys.argv[0]+" {User} {Options}\n\nUse Command: 'python "+sys.argv[0]+" -help' for more information.\n")































