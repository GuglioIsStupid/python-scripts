import moviepy.editor as mp
import sys, os
# max length is 2:20
maxVideoLength = 140

# check if video is too long
def checkVideoLength(video):
    clip = mp.VideoFileClip(video)
    duration = clip.duration
    if duration > maxVideoLength:
        return False
    else:
        return True
    
def determinePartAmount(video):
    clip = mp.VideoFileClip(video)
    duration = clip.duration
    if duration > maxVideoLength:
        parts = int(duration // maxVideoLength) + 1
        return parts
    else:
        return 1
    
# if video is too long, cut it
# should export 2 videos, part0 and part1 (or more if needed)

vid = sys.argv[1]
if checkVideoLength(vid) == False:
    clip = mp.VideoFileClip(vid)
    duration = clip.duration
    # cut the video into parts
    partAmount = determinePartAmount(vid)
    for i in range(partAmount):
        start = i * maxVideoLength
        end = (i + 1) * maxVideoLength
        part = clip.subclip(start, end)
        part.write_videofile("part" + str(i) + ".mp4")
        

