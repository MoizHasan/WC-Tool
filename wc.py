import argparse, sys, os
parser = argparse.ArgumentParser(description='WC tool')
# need to specify nargs to allow for stdin
parser.add_argument('filename', help='the file to analyze', nargs='?')
parser.add_argument('-c', '--bytes', action='store_true', help='sum the bytes')
parser.add_argument('-w', '--words', action='store_true', help='sum the words')
parser.add_argument('-l', '--lines', action='store_true', help='sum the lines')
parser.add_argument('-m', '--chars', action='store_true', help='sum the chars')

args = parser.parse_args()
line_count = 0
word_count = 0
bytes = 0
chars = 0
output = ''
file_path = ''
# this will give an err if we don't specify encoding
if args.filename:
    file_path = args.filename
    bytes = os.stat(file_path).st_size
    text = open(file_path, encoding="utf8")
else:
    text = sys.stdin
Lines = text.readlines()
for line in Lines:
    line_count += 1
    chars += len(line)
    if args.filename is None:
        bytes += len(line.encode('utf-8'))
    # no arg bundles whitespace
    word_count += len(line.split())
# loop over args and check for keys
if args.bytes:
    output += ' ' + str(bytes) + ' '
if args.lines:
    output += ' ' + str(line_count) + ' '
if args.words:
    output += ' ' + str(word_count) + ' '
if args.chars: 
    output += ' ' + str(chars) + ' '
if args.bytes is False and args.lines is False and args.words is False and args.chars is False:
    output += ' ' + str(line_count) + ' '
    output += ' ' + str(word_count) + ' '
    output += ' ' + str(bytes) + ' '
print(output + file_path)
if args.filename:
    text.close()
