# Imports
import argparse
import csv
from datetime import date

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    #pass
    # Create the parser
    #my_parser = argparse.ArgumentParser(prog='myls', usage='heloo hello',
    #                                description='List the content of a folder')
    
    my_parser = argparse.ArgumentParser()
    
    my_parser.add_argument("-p", "--print", type=str)
    my_parser.add_argument("-c","--count", type = int)
    
    args = my_parser.parse_args()
    
    print(f"Hello {args.print}")
    print(str(args.count))
    #print('aaacd')


if __name__ == "__main__":
    main()
