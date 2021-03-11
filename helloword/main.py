import argparse
import sys
import helloword
import contohModule
# from main import contohClass


parser = argparse.ArgumentParser(
        description='Code Dasar Pyhton Untuk Dicoba Belajar')
parser.add_argument('--version', action='version',
        version='helloword ' + helloword.__version__)

def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser.parse_args(argv[1:])

    print("Hello, word")
    print(":array")
    buah = ["apel", "anggur", "mangga", "jeruk"]
    print(buah[1])

    contohModule.printNama("#makjono")    
    
    return 0
