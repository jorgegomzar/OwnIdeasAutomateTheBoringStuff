import requests, json, pymsgbox

# The idea is to have it running every minute with crontab
# Requires python3-tk package and requests, pymsgbox pip3 libs

# change url for your issue of interest
ISSUE_URL = 'https://api.github.com/repos/Linux74656/SpaceEngineersLinuxPatches/issues/19/' 
FILE_PATH = '/home/jorge/Documentos/Proyectos/PYTHON/Utilidades/'

def main():
    COMMENT_URL = ISSUE_URL + 'comments?page={}'
    num = 1
    page = 1
    total = 0
    while not num == 0:
        r = requests.get(COMMENT_URL.format(str(page)))
        comments = r.json()
        num = len(comments)
        total += num
        page += 1
    print(total)
    check(total)
    save(total)

def check(total):
    try:
        with open(FILE_PATH + 'n_comments.txt', 'rt') as txt:
            num = int(txt.readline())
            if(num == total):
                print('No update')
            elif(num < total):
                print('Update')
                print('\a')
                pymsgbox.alert('New comment on issue!', 'GitHub update')
            else:
                print('A comment has been deleted')
    except IOError:
        print("File not accessible")

def save(total):
    with open(FILE_PATH + 'n_comments.txt', 'wt') as txt:
        txt.write(str(total))

main()