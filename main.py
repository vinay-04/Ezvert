from sys import argv
from os import makedirs
import ffmpeg
import threading
from math import ceil
import moviepy.editor as mp


def splitFile(file, d, format):
        ffmpeg.input(file, ss=d*60, t=60).output(f'out/{d}.{format}').run()
        # ffmpeg.input(args[file]).output(args[output]).run()

def outFile(file, format):
    makedirs('out', exist_ok=True)
    duration = float(ffmpeg.probe(file)['format']['duration'])
    if duration < 180:
        split = 1
    else:
        split = (duration/60)%60
    threads = []
    for d in range(0, int(ceil(split))):
        thread = threading.Thread(target=splitFile, args=(file, d, format))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == '__main__':

    try:
        if '-h' in argv or '--help' in argv:
            print('Usage:  -f <input file>\n\t-o <output file>')
        else:
            file = argv.index('-f')+1
            output = argv.index('-o')+1
            format = argv[output].split('.')[-1]
            outFile(argv[file], format)
            files = [f'out/{d}.{format}' for d in range(0, int(ceil((float(ffmpeg.probe(argv[file])['format']['duration'])/60)%60)))]
            mp.concatenate_videoclips([mp.VideoFileClip(file) for file in files]).write_videofile(argv[output])


    except:
        exit('Error: Invalid arguments\nUsage:  -f <input file>\n\t-o <output file>')
