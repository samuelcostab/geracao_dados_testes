import math, random
import string
import re

class GATest():

    def __init__(self, tamanho_populacao, geracoes):
        self.populacao = []
        self.tam_populacao = tamanho_populacao
        self.geracoes = geracoes
        self.soma_avaliacoes = 0
    
    
    def inicializar_populacao(self, tam_cromossomo):
        for i in range(self.tam_populacao):
            self.populacao.append(Cromossomo(tam_cromossomo))
        for cromossomo in self.populacao: cromossomo.inicializar()
            
    def avaliar_populacao(self,modelo):
        for cromossomo in self.populacao:
            self.soma_avaliacoes += cromossomo.avaliar(modelo)
            print(cromossomo.valor, cromossomo.avaliacao)
    
    def executar(self):
        print("Digite seu modelo:")
        input_model = input()
        input_model_split = input_model.split()
        model = []
        for i in input_model_split:
            if re.match('^\d+$',i): model.append(int(i))
            else: model.append(i)
        
        tam_model = len(model)
        self.inicializar_populacao(tam_model)
        self.avaliar_populacao(model)

ga = GATest(4,5)
ga.executar()