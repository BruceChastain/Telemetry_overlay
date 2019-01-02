#!/usr/bin/python
import sys
import gpxpy
import ffmpeg
from moviepy.editor import *

#---------getting data from user
vidinput = (sys.argv[1])
vidoutput = (sys.argv[2])
gpxinput = (sys.argv[3])
telsync = (sys.argv[4]) 
vidsync = (sys.argv[5])
tellen = (sys.argv[6])



print (vidinput)
print (vidoutput)
print (gpxinput)
print (telsync)
print (vidsync)
print (tellen)



#find the FPS !!!
clip = VideoFileClip(vidinput)
print(clip.fps)
print(clip.duration)
print(clip.is_playing(2))






#---------reading gpx file and cauclating speed
gpx_file = open(gpxinput, 'r')
gpx = gpxpy.parse(gpx_file)

for track in gpx.tracks:
    for segment in track.segments:
        for point_no, point in enumerate(segment.points):
            if point.speed != None:
                print("speed="), point.speed
            elif point_no > 0:
                speed = (point.speed_between(segment.points[point_no - 1]))
                kph_speed = speed * 3.6
                #print kph_speed



#--------applying overlay and rendering video

dur = 10

video = VideoFileClip(vidinput)




txt_clip = (TextClip(str(kph_speed), fontsize=90,color='white')
            .set_position('center')
            .set_duration(dur)            
)

result = CompositeVideoClip([video, txt_clip])
result.write_videofile(vidoutput)



