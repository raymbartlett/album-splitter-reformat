"""Reformat output from album_splitter to mp3 files with custom metadata."""
import sys
import os
import shutil
import eyed3
from pydub import AudioSegment


# How to call from command line: python3 reformat.py 'video ID' 'album title' 'artist'
# Video ID is the same as the new dir created in the 'splits' folder
def main():
    """Convert wav files to mp3 with metadata from command line args."""
    new_dir = sys.argv[1]
    album_name = sys.argv[2]
    album_artist = sys.argv[3]
    album_splitter_path = os.getcwd()

    input_dir = album_splitter_path + '/splits/' + new_dir
    output_dir = album_splitter_path + '/albums/' + album_name
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.mkdir(output_dir)

    # iterate over .wav files
    for filename in os.listdir(input_dir):
        file = os.path.join(input_dir, filename)
        if os.path.isfile(file):
            track_num = filename.split(' ', 1)[0]
            track_name = filename.split(' ', 1)[1].split('.wav')[0]
            song = AudioSegment.from_wav(file)
            song.export(output_dir + '/' + track_name + ".mp3", format="mp3")

            audiofile = eyed3.load(output_dir + '/' + track_name + ".mp3")
            audiofile.tag.track_num = track_num
            audiofile.tag.title = track_name
            audiofile.tag.album = album_name
            audiofile.tag.artist = album_artist
            audiofile.tag.album_artist = album_artist

            audiofile.tag.save()

    # delete original audio and .wav files
    shutil.rmtree(input_dir)
    os.remove(new_dir + '.wav')


if __name__ == '__main__':
    main()
