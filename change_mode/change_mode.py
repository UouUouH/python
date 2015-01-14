import os
import optparse

def is_a_mode(m):
    if m < 0 or m > 777: 
        return False

    a = m/100
    b = (m-a*100)/10
    c = m - a*100 -b*10
    
    if a <= 7 and b <= 7 and c <=7:
        return  True
    return False

def parse_args():
    usage = '''usage: %prog [option] dir 

    this is a script can change the mode of dir and file seperatly.

    default dir is the current dir.

    run it like this:

    python change-mode.py ./ --dirmode 775 --filenode 666 --display 1

    if you have any question about it, feel free to contact me.

    nayang2011@gmail.com
    nayanng@163.com'''

    parser = optparse.OptionParser(usage)

    help = '''set the mode of dir
              default = 775'''
    parser.add_option('--dirmode', type = 'int', help = help, default = 775)

    help = '''set the mode of file
              default = 666'''
    parser.add_option('--filemode', type = 'int', help = help, default = 666)

    help = '''display the commands have been run
              1: display
              0: not display
              default = 1'''
    parser.add_option('--display', type = 'int', help = help, default = 1)

    options, args = parser.parse_args()

    for adir in args:
        if not os.path.exists(adir):
            parser.error('no such dir:%s' %adir)

    if not is_a_mode(options.dirmode):
        parser.error('the mode of dir is error')

    if not is_a_mode(options.filemode):
        parser.error('the mode of file is error')

    if options.display != 1 and options.display != 0:
        parser.error('--display should be 1 or 0')

    return args, options

def change_mode(dirs,options):

    
    if len(dirs) == 0:
        flag = True 
        parent_dirs = os.getcwd() 
        print "dir is ",parent_dirs
    else:
        flag = False
        parent_dirs = dirs
        print "dir is ",
        for adir in parent_dirs:
            print adir
        print "\n"
    filemode = options.filemode
    dirmode = options.dirmode
    display = options.display

    print "the file mode bits of dir is ",dirmode
    print "the file mode bits of file is ",filemode

    user_order = raw_input("if you want to continue, please input 'Y'.or please input others:")
    if user_order != 'Y':
        print 'nothing changed'
        return
    if flag:

        for root, children_dirs, children_files in os.walk(parent_dirs):
            for afile in children_files:
                file_command = 'chmod '+str(filemode)+' '+root+'/'+afile
                print file_command
                os.system(file_command)
            dir_command = 'chmod '+str(dirmode)+' '+root
            print dir_command
            os.system(dir_command)
            
        return

    for adir in parent_dirs:
        for root, children_dirs, children_files in os.walk(adir):
            for afile in children_files:
                file_command = 'chmod '+str(filemode)+' '+root+'/'+afile
                print file_command
                os.system(file_command)
            dir_command = 'chmod '+str(dirmode)+' '+root
            print dir_command
            os.system(dir_command)
            
def main():
    dirs, options= parse_args()
    
    change_mode(dirs,options)

if __name__ == '__main__':
    main()
