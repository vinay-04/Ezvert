import sys
import ffmpeg


try:
    args = sys.argv
    if '-h' in args or '--help' in args or len(args) != 2:
        print('Usage:  -f <input file>\n\t-o <output file>')
    else:
        file = args.index('-f')+1
        output = args.index('-o')+1
        ffmpeg.input(args[file]).output(args[output]).run()



except:
    sys.exit('Error: Invalid arguments\nUsage:  -f <input file>\n\t-o <output file>')
