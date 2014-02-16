###
#youtube-music-ripper 
#by @peteyreplies 
#NOTE: must install youtube-dl and ffmpeg to work reliably! 
#youtube-dl: http://rg3.github.io/youtube-dl/download.html
#ffmpeg: https://trac.ffmpeg.org/wiki/MacOSXCompilationGuide
###

#import stuff
import youtube-dl
import subprocess

#prompt them for choice of download
print "What do you want to download? Enter 1, 2, 3, or 4 at the prompt!"
print "\t 1: an individual video"
print "\t 2: a list of individual video links in a .txt file"
print "\t 3: all videos by a user/channel"
print "\t 4: all videos in a playlist"
print ""

choice = input("Enter 1, 2, 3, or 4 here:")

if choice == 1: 
	print "Paste a link to the video in the prompt:"
	link = input()
	subprocess.call("youtube-dl " + link + " -itw --extract-audio --audioformat mp3")
	print "Ripped!"

if choice not in range 1,4: 
	print "You entered an invalid number! Why do you hate me and/or yourself?"


