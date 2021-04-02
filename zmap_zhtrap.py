import os
from datetime import datetime

now = datetime.now()

def zmap_scan():
    cmd = ""
    cmd += "sudo zmap "
    # cmd += "-M udp "
    ## ZHTRAP honeypot listen to these belo ports.
    # cmd += "-p 80, 8080, 8081, 8083, 37215, 5500, 60001, 52869, 8089, 8000, 81, 82, 83, 84, 85, 8888, 8181, 8443, 5555, 443, 22, 2323"
    cmd += "-p 2323 "
    cmd += "-r 5000 "
    cmd += "--whitelist-file=../data/srciplist.csv "
    # cmd += "--max-targets=10000000 "
    cmd += "-o ../result/zmap_zhtrap_take_" + now.strftime("%b-%d-%y-%H:%M:%S") + ".csv"

    os.system(cmd)

if __name__ == '__main__':
    zmap_scan()
