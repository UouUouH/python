import optparse, os, getpass


def parse_args():
    usage = '''usage: %prog [option] dir

    This is a script can delete the empty folder in the dir.

    Run it like this:

      python delete_empty_folder.py <dir> 

    If you want to delete all of the empty folder in the dir 'e:\',
    you can run it like this:

        python delete_empty_folder.py e:\

    if you have more than one dir,
    you can run it like this:
        python delete_empty_folder.py e:\ c:\ --dodelete 0

    if you have any question about it ,feel free to email me.
    nayang2011@gmail.com
    nayanng@163.com'''

    parser = optparse.OptionParser(usage)

    help = '''if delete the empty folder ,or just display the dir.
              1: delete
              0: not delete
              default = 0'''
    parser.add_option('--dodelete', type = 'int', help = help, default = 0)

    options, args = parser.parse_args()

    if options.dodelete != 0 and options.dodelete != 1:
        parser.error('option error: --dodelete should be 0 or 1')

    if len(args) == 0:
        parser.error('no dir')

    for adir in args:
        if not os.path.exists(adir):
            parser.error('no such dir: %s' % adir)

    return options.dodelete, args

def delete_empty_folder(dirs, flag):
    i = 1
    j = 1
    for dir1 in dirs:
        for root, adir, files in os.walk(dir1):
            print i,'-',
            i += 1
            if len(os.listdir(root)) == 0:
                print j, ' empty floder:',
                j += 1
                if flag == 1:
                    os.rmdir(root)
        
            print root
    return

def main():
    flag, dirs = parse_args()

    print dirs
    print flag
    
    delete_empty_folder(dirs, flag)



if __name__ == '__main__':
    main()

