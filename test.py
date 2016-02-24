#!/usr/bin/python3

import os.path as op
from pyasr.features import mfcc
from pyasr.features import logfbank
from pyasr.io_func import kaldi_io
import scipy.io.wavfile as wav

if __name__ == '__main__':
    ark = kaldi_io.KaldiArkRead()
    ark.open('../eesen/asr_egs/tedlium/v1/tv/cmvn.ark')
    X = ark.read(key='AJJacobs_2007P')
    print(X)
    ark.open('../eesen/asr_egs/tedlium/v1/tv/cmvn_txt.ark')
    X = ark.read(key='AJJacobs_2007P')
    print(X)
    ark.open('../eesen/asr_egs/tedlium/v1/tv/feat.ark')
    X = ark.read(key='AJJacobs_2007P-0001605-0003029')
    print(X)
    ark.open('../eesen/asr_egs/tedlium/v1/tv/feat_bin.ark')
    X = ark.read(key='AJJacobs_2007P-0001605-0003029')
    print(X)
