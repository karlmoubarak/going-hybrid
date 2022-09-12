import os
from tracemalloc import start
import srt
import pydub


AUDIO_EXT   = '.mp4'
CAPTION_EXT = '.srt'
AUDIO_DIR   = '../../audio/'

def mkdir_if_none( dirname ):
  if not os.path.exists( dirname ):
    os.mkdir( dirname )

def chop( src_path, dest_path, start_time, end_time ):
  sound = pydub.AudioSegment.from_file( src_path )
  sound_clip = sound[ start_time:end_time ]
  sound_clip.export( dest_path, format='mp3' )



files = os.listdir( AUDIO_DIR )
print(files)



for file in files :
  if file.endswith( AUDIO_EXT ):
    audio_file   = file
    caption_file = file.replace( AUDIO_EXT, CAPTION_EXT )
    track_name   = file.replace( AUDIO_EXT, '' )

    if os.path.isfile( AUDIO_DIR + caption_file ):
      print( caption_file, 'exists; proceeding to chop.' )
      caption_file = open( AUDIO_DIR + caption_file, 'r' )
      captions = caption_file.read()
      caption_file.close()
      subs = srt.parse( captions )
      mkdir_if_none( AUDIO_DIR + track_name )

      for sub in subs :
        src_path = AUDIO_DIR + audio_file
        dest_path = AUDIO_DIR + track_name + '/' + sub.content + '.mp3'
        start_time = sub.start.total_seconds() * 1000
        end_time = sub.end.total_seconds() * 1000

        chop( src_path, dest_path, start_time, end_time )
