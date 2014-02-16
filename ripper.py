###
#youtube-music-ripper 
#by @peteyreplies 
#NOTE: REQUIRES YOUTUBE-DL TO WORK - http://rg3.github.io/youtube-dl/download.html
#youtube-dl -citw ytuser:LaBelleChannel --extract-audio --audio-format mp3
###

#prompt them for choice of download
print "What do you want to download? Enter 1, 2, or 3 at the prompt"
print "1) an individual video"
print "2) all videos by a user/channel"
print "3) all videos in a playlist"

choice = input("Enter 1, 2, or 3 here:")

#validate the choice 
if int(input) 