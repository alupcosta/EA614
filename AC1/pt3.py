import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import soundfile as sf

corte = 15000 
largura = 3.0
altura = 3.0
ponto5_x = 2.2
ponto5_y = 0.7

# Abre e normaliza as brir's
brir1 = np.genfromtxt('AC1/Medições/SEC_1.csv', delimiter=',') 
brir1 = (brir1 / np.ptp(brir1, axis=0))
brir2 = np.genfromtxt('AC1/Medições/SEC_2.csv', delimiter=',')  
brir2 = (brir2 / np.ptp(brir2, axis=0))
brir3 = np.genfromtxt('AC1/Medições/SEC_3.csv', delimiter=',')
brir3 = (brir3 / np.ptp(brir3, axis=0))
brir4 = np.genfromtxt('AC1/Medições/SEC_4.csv', delimiter=',')
brir4 = (brir4 / np.ptp(brir4, axis=0))

# Abre o áudio
audio, fs = sf.read('AC1/Áudios/Canon_Violin.wav')

# Calcula os fatores de interpolação
tx = ponto5_x / largura
ty = ponto5_y / altura

# Interpola na borda inferior (entre P4 e P1)
i1 = brir4 * (1 - tx) + brir1 * tx

# Interpola na borda superior (entre P3 e P2)
i2 = brir3 * (1 - tx) + brir2 * tx

# Interpola entre os dois resultados intermediários
brir5_interpolada = i1 * (1 - ty) + i2 * ty

# Plota a resposta ao impulso estimada para o ponto 5
t = np.arange(0, len(brir5_interpolada[:corte, 0])) / fs
plt.figure(figsize=(12, 5))
plt.plot(t, brir5_interpolada[:corte, 0], label='Canal Esquerdo')
plt.plot(t, brir5_interpolada[:corte, 1], label='Canal Direito')
plt.title('Formato da Resposta ao Impulso Estimada')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.savefig('AC1/Saídas/Parte3_Interpolacao.png', dpi=300, bbox_inches='tight')

# Realiza convolução
final_left = np.convolve(audio, brir5_interpolada[:corte, 0], mode='full')
final_right = np.convolve(audio, brir5_interpolada[:corte, 1], mode='full')
final_stereo = np.column_stack((final_left, final_right))

# Transforma em áudio
sf.write('AC1/Saídas/Parte3_Interpolacao.wav', final_stereo, fs)