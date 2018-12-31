#!/usr/bin/python

import sys
#import mlt
import gpxpy
import ffmpeg

vidinput = (sys.argv[1])
vidoutput = (sys.argv[2])
gpxinput = (sys.argv[3])
telsync = (sys.argv[4]) 
vidsync = (sys.argv[5])



print (vidinput)
print (vidoutput)
print (gpxinput)
print (telsync)
print (vidsync)

gpx_file = open('example.gpx', 'r')
gpx = gpxpy.parse(gpx_file)

for track in gpx.tracks:
    for segment in track.segments:
        for point_no, point in enumerate(segment.points):
            if point.speed != None:
                print("speed="), point.speed
            elif point_no > 0:
                speed = (point.speed_between(segment.points[point_no - 1]))
                kph_speed = speed * 3.6
                print kph_speed





from moviepy.editor import *
video = VideoFileClip('test_vid.avi')

txt_clip = ( TextClip("My TEXT TEX TEX")
        .set_position('center')
        .set_duration('10')            
            )

result = CompositeVideoClip([video, txt_clip])
result.write_videofile("output.mov")


          


