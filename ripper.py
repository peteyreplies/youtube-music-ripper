###
#youtube-music-ripper 
#by @peteyreplies 
#NOTE: REQUIRES YOUTUBE-DL TO WORK - http://rg3.github.io/youtube-dl/download.html
###

#import stuff
import youtube-dl


#prompt them for choice of download
print "What do you want to download? Enter 1, 2, 3, or 4 at the prompt"
print "1) an individual video"
print "2) all videos by a user/channel"
print "3) all videos in a playlist"
print "4) a txt file of youtube links"

choice = input("Enter 1, 2, 3, or 4 here:")

#validate the choice 
if int(input) 