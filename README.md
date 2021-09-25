# splitting-tracks
pydub==0.25.1
simpleaudio==1.0.4

You need to install:
######      Linux       ###########
   libav
apt-get install libav-tools libavcodec-extra
   ffmpeg
apt-get install ffmpeg libavcodec-extra

######      Windows     ###########
Install ffmpeg in Windows.
Download and extract libav from http://builds.libav.org/windows/.
Add the libav /bin folder to your PATH envvar.
pip install pydub


https://github.com/jiaaro/pydub/

The program divides the musical sounds into shorter pieces, the chosen number of minutes and saves them in the same place as you will start with the name of the track numbered from 1 to the number of parts.
You need to enter the path in which directory you want to search for files and the format, one of mp3, ogg, flv, mp4, wma, aac and the number of minutes to split the track.