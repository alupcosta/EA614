import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import soundfile as sf

corte = 15000 

# Abre e normaliza brir
brir = np.genfromtxt('AC1/Medições/SEC_1.csv', delimiter=',')
brir = (brir / np.ptp(brir, axis=0))

# Abre áudio
inst1, fs = sf.read('AC1/Áudios/Canon_Violin.wav') 

# Realiza convolução
left_channel = np.convolve(inst1, brir[:corte, 0], mode='full')
right_channel = np.convolve(inst1, brir[:corte, 1], mode='full')

# Une os canais
stereo_audio = np.column_stack((left_channel, right_channel))

# Transforma em audio
sf.write('AC1/Saídas/Canon_Violin_SEC1_Left.wav', left_channel, fs)
sf.write('AC1/Saídas/Canon_Violin_SEC1_Right.wav', right_channel, fs)
sf.write('AC1/Saídas/Canon_Violin_SEC1_Stereo.wav', stereo_audio, fs)