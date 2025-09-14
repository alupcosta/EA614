import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import soundfile as sf

corte = 15000

# Abre a brir real do ponto 5
brir5_real = np.genfromtxt('AC1/Medições/SEC_5.csv', delimiter=',')

# Abre o áudio
audio, fs = sf.read('AC1/Áudios/Canon_Violin.wav')

# Plota a resposta ao impulso real do ponto 5
t_brir = np.arange(corte) / fs
plt.figure(figsize=(12, 5))
plt.title('BRIR Real do Ponto 5')
plt.plot(t_brir, brir5_real[:corte, 0], label='Canal Direito Real')
plt.plot(t_brir, brir5_real[:corte, 1], label='Canal Esquerdo Real')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.savefig('AC1/Saídas/Parte4_Real.png', dpi=300, bbox_inches='tight')

# Realiza a convolução (real)
right_channel = np.convolve(audio, brir5_real[:corte, 0], mode='full')
left_channel = np.convolve(audio, brir5_real[:corte, 1], mode='full')
real_stereo = np.vstack([left_channel, right_channel]).transpose()

# Salva o áudio convolucionado (real)
sf.write('AC1/Saídas/Parte4_Audio_Real.wav', real_stereo, fs)

# Plota o áudio gerado
t_audio = np.arange(len(left_channel)) / fs
plt.figure(figsize=(12, 5))
plt.plot(t_audio, left_channel, label='Canal Esquerdo (Real)')
plt.plot(t_audio, right_channel, label='Canal Direito (Real)')
plt.title('Áudio Convolucionado com BRIR Real - Parte 4')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.savefig('AC1/Saídas/Parte4_Audio.png', dpi=300, bbox_inches='tight')