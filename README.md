# Album Splitter Reformat

## This script takes the output from the [album-splitter](https://github.com/crisbal/album-splitter) package and modifies it in the following ways:
* Converts from .wav to .mp3
* Removes track number from the title
* Adds metadata from command line arguments (song title, album title, artist)
* Deletes full length .wav and folder of .wavs from "splits"

## How to call from command line:
* python3 reformat.py 'Video ID' 'Album Name' 'Artist Name'
* Example with *Hounds of Love* by Kate Bush: python3 reformat.py 'cO80PF9MMAE' 'Hounds of Love' 'Kate Bush'
