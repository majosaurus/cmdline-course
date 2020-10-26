from sys import argv, stderr
from bllipparser import RerankingParser

if __name__=="__main__":
    """
        Parse an English Gutenberg book in sentence per line format
        using bllipparser. Write string representations of parse trees
        to the output file.
    """
    if len(argv) != 3:
        print("USAGE %s inputfile outputfile" % argv[0], file=stderr)
        exit(1)

    # Initialize parser and download parser model if needed.
    rrp = RerankingParser.fetch_and_load('WSJ-PTB3', verbose=True)

    ifile = open(argv[1])
    ofile = open(argv[2],"w")
    
    # Read input sentences from ifile and print parse trees to ofile.
    for i, line in enumerate(ifile):
        if i >= 10:
            break
        print(rrp.simple_parse(line.strip('\n')), file=ofile)
