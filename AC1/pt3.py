import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import soundfile as sf

corte = 15000 
largura = 3.0
altura = 3.0
ponto5_x = 2.2
ponto5_y = 0.7

# Abre as brir's
brir1 = np.genfromtxt('AC1/Medições/SEC_1.csv', delimiter=',') 
brir2 = np.genfromtxt('AC1/Medições/SEC_2.csv', delimiter=',')  
brir3 = np.genfromtxt('AC1/Medições/SEC_3.csv', delimiter=',')
brir4 = np.genfromtxt('AC1/Medições/SEC_4.csv', delimiter=',')
brir5 = np.genfromtxt('AC1/Medições/SEC_5.csv', delimiter=',')

# Abre o áudio
audio, fs = sf.read('AC1/Áudios/Canon_Violin.wav')

# Realiza interpolação bilinear para estimar a BRIR no ponto 5
tx = ponto5_x / largura
ty = ponto5_y / altura
i1 = brir4 * (1 - tx) + brir1 * tx
i2 = brir3 * (1 - tx) + brir2 * tx
brir5_interpolada = i1 * (1 - ty) + i2 * ty

# Plota a resposta ao impulso estimada para o ponto 5
t = np.arange(0, len(brir5_interpolada[corte:, 0])) / fs
plt.figure(figsize=(12, 5))
plt.plot(t, brir5_interpolada[corte:, 0], label='Canal Direito (Interpolado)')
plt.plot(t, brir5_interpolada[corte:, 1], label='Canal Esquerdo (Interpolado)')
plt.title('BRIR Interpolada para o Ponto 5')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.savefig('AC1/Saídas/Parte3_BRIR_Interpolada.png', dpi=300, bbox_inches='tight')

# Realiza a convolução com a BRIR interpolada
right_channel = np.convolve(audio, brir5_interpolada[:corte, 0], mode='full')
left_channel = np.convolve(audio, brir5_interpolada[:corte, 1], mode='full')
interpolated_stereo = np.vstack([left_channel, right_channel]).transpose()

# Salva o áudio convolucionado
sf.write('AC1/Saídas/Parte3_Audio_Interpolado.wav', interpolated_stereo, fs)

# Plota o áudio gerado
t_audio = np.arange(len(left_channel)) / fs
plt.figure(figsize=(12, 5))
plt.plot(t_audio, left_channel, label='Canal Esquerdo (Interpolado)')
plt.plot(t_audio, right_channel, label='Canal Direito (Interpolado)')
plt.title('Áudio Convolucionado com BRIR Interpolada - Parte 3')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.savefig('AC1/Saídas/Parte3_Audio.png', dpi=300, bbox_inches='tight')