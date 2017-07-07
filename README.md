# findsubsound

If you have a slice of audio taken from a larger parent file, this script
finds the onset time where the slice of audio was taken from.


# dependencies

- numpy
- scipy

## usage

```
$ python fss.py parent.wav child.wav
```

Currently the script expects wav files as input. You can turn an mp3 into a wav using ffmpeg
and force the sampling rate of both parent and child files to match (still working on this)


