#!/usr/bin/python

import os
import fnmatch
import argparser
import io

# Create arguments to pass over to the command.

parser = argparse.ArgumentParser(
    description="Script to Find, Filter & copy files.",
    epilog="Please refer the above syntax for running the script correctly")

parser.add_argument("-n", "--file_name", nargs='?', help="Pass the file name to search.")
parser.add_argument("-s", "--string", nargs='?', help="Pass the string text to search in a file.")
parser.add_argument("-i", "--input_path", nargs='?', help="Path where to execute the script or where files are present")
parser.add_argument("-o", "--out_dir", nargs='?', help="Path where files need to be copied.")

args = parser.parse_args()

# Main script

# Append a directory separator if not already present
if not (args.input_path.endswith("/") or args.input_path.endswith("\\")):
    args.input_path = args.input_path + "/"

# If path does not exist, set search path to current directory
if not os.path.exists(args.input_path):
    args.input_path = "."

# Search based on string text in a file
if args.string:
    for file in os.listdir(args.input_path):
        # Read only files and ignore direcories
        if os.path.isfile(args.input_path+file):
            # Open file for reading
            # Use either encoding='latin-1' or errors='ignore'
            # Using io to avoid encoding invalid errors
            with io.open(args.input_path + file, encoding='latin-1') as fo:
                if args.string in fo.read():
                    print(file)
# Search based on file name
elif args.file_name:
    for file in os.listdir(args.input_path):
        if os.path.isfile(file):
            # match the file name based on the string text given
            if fnmatch.fnmatch(file, '*' + args.file_name + '*'):
                print(file)
