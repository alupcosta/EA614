import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import soundfile as sf

corte = 15000 

# Abre e normaliza brir da Fonte 1
brir1 = np.genfromtxt('AC1/Medições/SEC_1.csv', delimiter=',')
brir1 = (brir1 / np.ptp(brir1, axis=0))

# Abre e normaliza brir da Fonte 2
brir2 = np.genfromtxt('AC1/Medições/SEC_2.csv', delimiter=',') # Use um arquivo de medição oposto
brir2 = (brir2 / np.ptp(brir2, axis=0))

# Abre os áudios
audio1, fs = sf.read('AC1/Áudios/Aria_Violin1.wav')
audio2, fs = sf.read('AC1/Áudios/Aria_Violin2.wav')

# Realiza convolução da fonte 1
left1 = np.convolve(audio1, brir1[:corte, 0], mode='full')
right1 = np.convolve(audio1, brir1[:corte, 1], mode='full')

# Realiza convolução da fonte 2
left2 = np.convolve(audio2, brir2[:corte, 0], mode='full')
right2 = np.convolve(audio2, brir2[:corte, 1], mode='full')

# Combina os canais esquerdo e direito de ambas as fontes (propriedade linear da convolução)
final_left = left1 + left2
final_right = right1 + right2

# Une os canais
final_stereo = np.column_stack((final_left, final_right))

# Transforma em áudio
sf.write('AC1/Saídas/Parte2_Duas_Fontes.wav', final_stereo, fs)