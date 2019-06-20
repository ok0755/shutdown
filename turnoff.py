#coding=utf-8
import time
from time import sleep
import subprocess
import configparser

'''
cf = configparser.ConfigParser()
cf.read(r'd:\shutdowntm.conf')
print(cf.get('tm','attime'))
cf.set('tm','attime','cancel')
cf.write(open(r'd:\shutdowntm.conf','w'))
'''
def getime():
    cf = configparser.ConfigParser()
    cf.read(r'd:\shutdowntm.conf')
    tm = cf.get('tm','attime')
    return tm

def wr_time(st):
    cf = configparser.ConfigParser()
    cf.read(r'd:\shutdowntm.conf')
    cf.set('tm','attime',st)
    cf.write(open(r'd:\shutdowntm.conf','w'))
    return

def cancel():
    exc = subprocess.Popen('shutdown.exe -a',shell=True)
    sleep(1)
    exc.kill()

def shutdown(tm):
    h1 = int(tm[:2])
    m1 = int(tm[2:])
    mytime=time.strftime('%H:%M')
    h2=int(mytime[0:2])
    m2=int(mytime[3:5])
    s1=(h1-h2)*3600+(m1-m2)*60
    exe = subprocess.Popen('shutdown.exe -s -t {}'.format(s1),shell=True)
    sleep(1)
    exe.kill()

if __name__=='__main__':
    tm = getime()
    if tm != 'cancel':
        shutdown(tm)
        sleep(2)
        wr_time('cancel')
    else:
        cancel()
        wr_time('1630')



    ##shutdown()