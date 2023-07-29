#!/usr/bin/env python

import sys

command=[]

def list_command_line_arguments():
    startrec = False
    if len(sys.argv) > 1:
        print("Command-line arguments:")
        for index, arg in enumerate(sys.argv[1:], start=1):
            print(f"{index}. {arg}")
            if arg == '--flash_mode':
                startrec = True
            if startrec:
                command.append(arg)

    else:
        print("No command-line arguments provided.")

if __name__ == "__main__":
    list_command_line_arguments()

    with open('flash_args', 'w') as f:
        f.write(' '.join(command))

    print('Using command %s' % ' '.join(command))

