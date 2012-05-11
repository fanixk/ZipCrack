from itertools import product
import string
import sys
import zipfile

zfile = zipfile.ZipFile('test_zip.zip')
name = zfile.namelist()
        
def crack():
    str_pass = ''
    for len in range(1,10):
        for possible_pass in product(string.ascii_lowercase, repeat = len):
            str_pass = str_pass.join(possible_pass)
            try:
                file = zfile.read(name[0], str_pass)
                return str_pass
            except:
                str_pass = ''
    return "not found"
                
if __name__ == '__main__':
    from timeit import Timer
    t = Timer("print crack()", "from __main__ import crack")
    print(("Min(s): %.2f" %(t.timeit(1) /60)))
    #print "Password: ", crack()
