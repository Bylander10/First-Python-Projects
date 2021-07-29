"""
Importe o Dataset
https://gist.github.com/KhanradCoder/35a6beea49e5b9ba62797e595a9626c0
"""

import pandas as pd  # biblioteca responsável pela manipulação do nosso arquivo csv
from sklearn.model_selection import train_test_split  # biblioteca Machine Learning responsável pela divisão dos dados
import tensorflow as tf  # biblioteca Machina Learning responsável pela criação e treino da IA

data_url = 'https://gist.github.com/KhanradCoder/35a6beea49e5b9ba62797e595a9626c0/raw/8974e055bdf3a9d7e6cacf1c1c30fcfd2ffd6de3/cancer.csv'  # arquivo csv / tabela

dataset = pd.read_csv(data_url)  # pandas vai ler o arquivo csv e disponibilizar ele pra gente em formato de tabela

x = dataset.drop(columns=['diagnosis(1=m, 0=b)'])  # x será toda a tabela menos a coluna 'diagnosis(1=m, 0=b)' (dados recebidos pela nossa IA)
y = dataset['diagnosis(1=m, 0=b)']                 # y será apenas a coluna 'diagnosis(1=m, 0=b)'              (dados reais)

"""
Divida os dados entre set de treino e set de teste
"""

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)  # 20% dos nossos dados vão estar no set de teste para dar mais resiliência a nossa IA

"""
Construa e treine a IA
"""

model = tf.keras.models.Sequential()  # modelo sequencial padrão de IA

model.add(tf.keras.layers.Dense(256, input_shape=x_train.shape, activation='sigmoid'))  # 1ª camada oculta da IA (256 neurônios, coloquei até demais)
model.add(tf.keras.layers.Dense(256, activation='sigmoid'))                             # 2ª camada oculta da IA (256 neurônios)
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))                               # camada de output       (1 neurônio)
#  ativação sigmoid é usada pra realizar uma plotagem dos números para entre 0 e 1, isso diminuirá a complexidade e deixará a IA mais precisa no nosso caso
# ƒ(x) = 1/1+e^βx (função sigmoid)
# ela tem a mesma aparência do random.random()
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  # compilação da IA focada em precisão, isso fará com que tenhamos resultados mais exatos em troca de processamento

model.fit(x_train, y_train, epochs=1000)  # IA será treinada e fará a comparação entre os valores retornados e os valores reais, para isso ela irá ler a tabela 1000 vezes

"""
Avalie a IA
"""

model.evaluate(x_test, y_test)  # comparação entre os valores retornados e os valores reais em porcentagem, eles tem uma precisão de aproximadamente 97%
