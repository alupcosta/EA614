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
print("Arquivos carregados com sucesso.")

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
audio_real = np.column_stack((audio_real_L, audio_real_R))

# Tranforma em áudio (real)
sf.write('AC1/Saídas/Parte4_Real.wav', audio_real, fs)