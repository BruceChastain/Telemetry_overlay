#!/usr/bin/python
import os
import subprocess
import sys
import gpxpy
import ffmpeg
from moviepy.editor import *
import moviepy

srt_file = "srt_file.srt"

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




   

#---------reading gpx file and cauclating speed and writing .srt file
gpx_file = open(gpxinput, 'r')
gpx = gpxpy.parse(gpx_file)
gpxtime = ""
line = 0
for track in gpx.tracks:
    for segment in track.segments:
        for point_no, point in enumerate(segment.points):
            if point.speed != None:
                print("speed="), point.speed
            elif point_no > 0:
                speed = (point.speed_between(segment.points[point_no - 1]))
                kph_speed = speed * 3.6
                kph_speed = str(kph_speed)
                print(kph_speed) 
                #making line numbers                
                line = line + 1
                line = str(line)  
                print(line)     
                #making time stamps
                old_cut_time=(gpxtime[11:18])
                print(old_cut_time)
                current_time = str(point.time)              
                current_cut_time=(current_time[11:19])  
                print(current_cut_time)            
                  

                #writing file (only takes strings)
                file=open(srt_file,"a")
                file.write(line)
                file.write("\n")
                file.write(old_cut_time)
                file.write(" --> ")
                file.write(current_cut_time)
                file.write("\n")
                file.write(kph_speed)
                file.write("\n")
                file.close() 
                line = int(line)







# generate the video using the subtitles file 
#os.system("ffmpeg -i input.mp4 -vf subtitles=srt_file.srt output.mp4")


#clean up - delete srt file
#os.remove("srt_file.srt") 






