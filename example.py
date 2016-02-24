import os.path as op
from pyasr.features import mfcc
from pyasr.features import logfbank
import scipy.io.wavfile as wav

timit_base = "/home/leo/work/neural/timit/TIMIT"
wav_file = op.join(timit_base, "TRAIN/DR1/FCJF0/SI1027.WAV")

print wav_file

(rate,sig) = wav.read(wav_file)
mfcc_feat = mfcc(sig,rate)
fbank_feat = logfbank(sig,rate)

print(fbank_feat[1:3,:])
