from sys import argv, stderr

START = "*** START OF THIS PROJECT GUTENBERG EBOOK"
STOP  = "*** END OF THIS PROJECT GUTENBERG EBOOK"

if __name__=="__main__":
    if len(argv) != 3:
        print("USAGE: %s input_file output_file" % argv[0], file=stderr)
        exit(1)

    ifile = open(argv[1])
    ofile = open(argv[2],"w")
    printing = 0
    for line in ifile:
        if STOP in line:
            break
        if printing: 
            print(line,end="",file=ofile)
        if START in line:
            printing = 1
