###
#youtube-music-ripper 
#by @peteyreplies 
#NOTE: REQUIRES YOUTUBE-DL TO WORK - http://rg3.github.io/youtube-dl/download.html
###

#import stuff
import youtube-dl


#prompt them for choice of download
print "What do you want to download? Enter 1, 2, 3, or 4 at the prompt"
print "\t 1) an individual video"
print "\t 2) a list of individual video links in a .txt file"
print "\t 3) all videos by a user/channel"
print "\t 4) all videos in a playlist"
print ""

choice = input("Enter 1, 2, 3, or 4 here:")

#validate the choice 
if 1 >= int(input) <= 4: 
	pass
else:
	print "You entered an invalid number! Why do you hate me and/or yourself?"
	break

