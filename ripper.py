###
#youtube-music-ripper 
#by @peteyreplies 
#NOTE: must install youtube-dl and ffmpeg to work reliably! 
#youtube-dl: http://rg3.github.io/youtube-dl/download.html
#ffmpeg: https://trac.ffmpeg.org/wiki/MacOSXCompilationGuide
#generic disclaimer: use legally, etc, etc 
###

#import 
import subprocess

#prompt them for choice of download
print ""
print "What do you want to rip? Enter 1, 2, 3, or 4 at the prompt!"
print "\t 1: audio from an individual video"
print "\t 2: audio from a list of video links in a .txt file in this folder"
print "\t 3: audio from all videos by a user/channel"
print "\t 4: audio from all videos in a playlist"
print ""

choice = input("Enter 1, 2, 3, or 4 here: ")

if choice == 1: 
	print "Paste the link to the video in the prompt: "
	link = raw_input()
	subprocess.call("youtube-dl " + link + " -itw --extract-audio --audio-format mp3", shell=True)
	print "Ripped!"

if choice == 2: 
	print "Enter the name of the text file (e.g. links.txt): "
	links = raw_input()
	subprocess.call("youtube-dl -itw --extract-audio --audio-format mp3 -a, --batch-file " + links, shell=True)
	print "Ripped!"

if choice == 3: 
	print "Paste *only* the user/channel name into the prompt: "
	user = raw_input()
	subprocess.call("youtube-dl -itw ytuser:" + user + " --extract-audio --audio-format mp3", shell=True)
	print "Ripped!"

if choice == 4: 
	print "Paste a link to the playlist (it should have the word '''playlist''' in the URL) into the prompt: " 
	playlist = raw_input()
	subprocess.call("youtube-dl " + playlist + " -itw --extract-audio --audio-format mp3", shell=True)
	print "Ripped!"

if choice not in range (1,4): 
	print "You entered an invalid option! Why do you hate me and/or yourself? Try that again..."


