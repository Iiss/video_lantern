'''
Just look in playlist directory and play loof of first compartible video from it

'''
import os

print '=================================='
print ' Welcome to the video lantern!'
print '=================================='
ext = tuple(['.avi', '.mpeg', '.mkv', '.mp4'])
app_dir = os.path.dirname(os.path.realpath(__file__))
playlist_dir = os.path.join(app_dir,'playlist')

playlist = []

for f in os.listdir(playlist_dir):
	if f.endswith(ext):
		playlist.append(f)

if len(playlist) > 0:
	vid = os.path.join(playlist_dir,playlist[0])
	print "Let's watch %s" % vid 
	os.system('omxplayer %s -b --loop --no-osd') % vid
else:
	print 'No videos found. Sorry...'

