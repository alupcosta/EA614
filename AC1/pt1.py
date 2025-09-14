import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import soundfile as sf

corte = 15000 

# Abre a brir
brir = np.genfromtxt('AC1/Medições/SEC_1.csv', delimiter=',')

# Abre áudio
inst1, fs = sf.read('AC1/Áudios/Canon_Violin.wav') 

# Realiza convolução
right_channel = np.convolve(inst1, brir[:corte, 0], mode='full')
left_channel = np.convolve(inst1, brir[:corte, 1], mode='full')

# Une os canais
stereo_audio = np.vstack([left_channel, right_channel]).transpose()

# Transforma em áudio
sf.write('AC1/Saídas/Parte1_Esquerdo.wav', left_channel, fs)
sf.write('AC1/Saídas/Parte1_Direito.wav', right_channel, fs)
sf.write('AC1/Saídas/Parte1_Estereo.wav', stereo_audio, fs)

# Plota o áudio gerado
t_audio = np.arange(len(left_channel)) / fs
plt.figure(figsize=(12, 5))
plt.plot(t_audio, left_channel, label='Canal Esquerdo')
plt.plot(t_audio, right_channel, label='Canal Direito')
plt.title('Áudio Convolucionado - Parte 1')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.savefig('AC1/Saídas/Parte1_Audio.png', dpi=300, bbox_inches='tight')