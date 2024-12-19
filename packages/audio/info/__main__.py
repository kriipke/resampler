from pedalboard.io import AudioFile

def main(args):
  with AudioFile("murmur.wav") as f:
    print(f.duration) # => 30.0
    print(f.samplerate) # => 44100
    print(f.num_channels) # => 2
    print(f.read(f.samplerate * 10))
    # => returns a NumPy array of shape (2, 441_000):
    #    [[ 0.  0.  0. ... -0. -0. -0.]
    #     [ 0.  0.  0. ... -0. -0. -0.]]
