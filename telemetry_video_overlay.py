#!/usr/bin/python
import os
import sys
import gpxpy
import ffmpeg

#---------clean up - delete srt file
srt_file = "srt_file.srt"
exists = os.path.isfile(srt_file)
if exists:
    os.remove(srt_file) 


#---------getting data from user
vidinput = (sys.argv[1])
vidoutput = (sys.argv[2])
gpxinput = (sys.argv[3])
telsync = (sys.argv[4]) 
vidsync = (sys.argv[5])
tellen = (sys.argv[6])


#---------reading gpx file and cauclating speed and writing .srt file
gpx_file = open(gpxinput, 'r')
gpx = gpxpy.parse(gpx_file)

line = 0
time_second = 0
time_minute = 0
time_dif_second = 0
first_time = True

for track in gpx.tracks:
    for segment in track.segments:
        for point_no, point in enumerate(segment.points):
            if point_no > 0:
                speed = (point.speed_between(segment.points[point_no - 1]))
                kph_speed = round(speed * 3.6, 1)
                kph_speed = str(kph_speed)
 
                #pulling time and making line numbers 

                
                if first_time == False:
                    time_dif_second = (point.time.second - time_second) 
                    print(time_dif_second) 
                
                time_second = (point.time.second)   
                
                if first_time == True:
                    init_offset = time_second
                    first_time = False                 
                
                if time_dif_second < 0: #means if it's a negtaive number
                    time_dif_second = time_dif_second + 60

                final_output_seconds = (time_second - init_offset - time_dif_second)

                print(final_output_seconds)
                                         
                
                if final_output_seconds < 0:
                    final_output_seconds = final_output_seconds + 59
                   
                    
                 
                line = line + 1  
            
                if first_time == False:
                    file=open(srt_file,"a")
                    file.write (str(line))
                    file.write("\n")
                    file.write ("00:")
                    file.write (str(time_minute))
                    file.write (":")
                    file.write (str(final_output_seconds))
                    file.write (",")
                    file.write ("000")
                    file.write(" --> ")
                    file.write ("00:")
                    file.write (str(time_minute))
                    file.write (":")
                    file.write (str(final_output_seconds + time_dif_second))
                    file.write (",")
                    file.write ("000")
                    file.write("\n")
                    file.write(kph_speed + " kp/h")
                    file.write("\n")
                    file.close() 
                



# generate the video using the subtitles file 
#os.system("ffmpeg -i input.mp4 -vf subtitles=srt_file.srt output.mp4 -y")










