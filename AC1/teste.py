import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# Carrega a BRIR do Ponto 1 (lado direito do diagrama, mas esquerdo para o ouvinte)
brir_ponto1 = np.genfromtxt('AC1/Medições/SEC_5.csv', delimiter=',')
brir_ponto1 = (brir_ponto1 / np.ptp(brir_ponto1, axis=0)) # Normaliza

fs = 44100
corte = 5000 
time_vector = np.arange(corte) / fs

plt.figure(figsize=(12, 6))
plt.title('Verificação Definitiva da BRIR do Ponto 1', fontsize=16)

# Nossa suposição original: Coluna 0 é o canal Esquerdo
plt.plot(time_vector, brir_ponto1[:corte, 0], label='Canal Esquerdo (Coluna 0)', color='blue', linewidth=2)

# Nossa suposição original: Coluna 1 é o canal Direito
plt.plot(time_vector, brir_ponto1[:corte, 1], label='Canal Direito (Coluna 1)', color='red', linestyle='--')

plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True, alpha=0.5)
plt.legend()
plt.show()