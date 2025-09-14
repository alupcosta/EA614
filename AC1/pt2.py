import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import soundfile as sf

corte = 15000 

# Abre as brir's
brir1 = np.genfromtxt('AC1/Medições/SEC_1.csv', delimiter=',')
brir2 = np.genfromtxt('AC1/Medições/SEC_3.csv', delimiter=',')

# Abre os áudios
audio1, fs = sf.read('AC1/Áudios/Aria_Violin1.wav')
audio2, fs = sf.read('AC1/Áudios/Aria_Cello.wav')

# Realiza convolução da fonte 1
right1 = np.convolve(audio1, brir1[:corte, 0], mode='full')
left1 = np.convolve(audio1, brir1[:corte, 1], mode='full')

# Realiza convolução da fonte 2
right2 = np.convolve(audio2, brir2[:corte, 0], mode='full')
left2 = np.convolve(audio2, brir2[:corte, 1], mode='full')

# Combina os canais esquerdo e direito de ambas as fontes (propriedade linear da convolução)
final_left = left1 + left2
final_right = right1 + right2

# Une os canais
final_stereo = np.vstack([final_left, final_right]).transpose()

# Salva o áudio final
sf.write('AC1/Saídas/Parte2_Estereo.wav', final_stereo, fs)

# Plota o áudio gerado
t_audio = np.arange(len(final_left)) / fs
plt.figure(figsize=(12, 5))
plt.plot(t_audio, final_left, label='Canal Esquerdo')
plt.plot(t_audio, final_right, label='Canal Direito')
plt.title('Áudio Combinado - Parte 2')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.savefig('AC1/Saídas/Parte2_Audio.png', dpi=300, bbox_inches='tight')