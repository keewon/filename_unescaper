import sys
import os
import os.path
import urllib

def log_error(str):
    sys.stderr.write(str)

def modify(filename):
    i = 0
    f1 = urllib.unquote(filename)
    t = f1
    try:
        t = f1.decode('utf-8')
    except UnicodeDecodeError:
        t = f1.decode('cp949')
    
    return t

def main(fullpath):
    if not os.path.isfile(fullpath):
        log_error("Not a file\n")
        return -101

    (prefix, base) = os.path.split(fullpath)

    prefix = prefix.decode('utf-8')

    modified = modify(base)

    if modified == base:
        log_error("No need to change filename\n")
        return -102

    dst = os.path.join(prefix, modified)
    os.rename(fullpath, dst)

    log_error("rename to %s\n" % dst)

    return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: %s FILENAME' % os.path.basename(sys.argv[0])
    else:
        main(sys.argv[1])
