import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import soundfile as sf

corte = 15000 

# Abre e normaliza a brir real do ponto 5
brir5_real = np.genfromtxt('AC1/Medições/SEC_5.csv', delimiter=',')
brir5_real = (brir5_real / np.ptp(brir5_real, axis=0))

# Abre o áudio
audio, fs = sf.read('AC1/Áudios/Canon_Violin.wav')

# Plota a resposta ao impulso real do ponto 5
t_brir = np.arange(corte) / fs
plt.figure(figsize=(12, 5))
plt.title('BRIR Real do Ponto 5')
plt.plot(t_brir, brir5_real[:corte, 0], label='Canal Esquerdo Real')
plt.plot(t_brir, brir5_real[:corte, 1], label='Canal Direito Real')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.savefig('AC1/Saídas/Parte4_Real.png', dpi=300, bbox_inches='tight')

# Realiza a convolução (real)
audio_real_L = np.convolve(audio, brir5_real[:corte, 0], mode='full')
audio_real_R = np.convolve(audio, brir5_real[:corte, 1], mode='full')
audio_real_stereo = np.column_stack((audio_real_L, audio_real_R))

# Salva o áudio convolucionado (real)
sf.write('AC1/Saídas/Parte4_Audio_Real.wav', audio_real_stereo, fs)

# Plota o áudio gerado
t_audio = np.arange(len(audio_real_L)) / fs
plt.figure(figsize=(12, 5))
plt.plot(t_audio, audio_real_L, label='Canal Esquerdo (Real)', color='blue')
plt.plot(t_audio, audio_real_R, label='Canal Direito (Real)', color='red')
plt.title('Áudio Convolucionado com BRIR Real - Parte 4')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.savefig('AC1/Saídas/Parte4_Audio.png', dpi=300, bbox_inches='tight')