import math, random
import string
import re

class GATest():

    def __init__(self, tamanho_populacao, geracoes):
        self.populacao = []
        self.tam_populacao = tamanho_populacao
        self.geracoes = geracoes
        self.soma_avaliacoes = 0
        self.melhores = []
    
    
    def inicializar_populacao(self, tam_cromossomo):
        for i in range(self.tam_populacao):
            self.populacao.append(Cromossomo(tam_cromossomo))
        for cromossomo in self.populacao: cromossomo.inicializar()
            
    def avaliar_populacao(self,modelo):
        for cromossomo in self.populacao:
            self.soma_avaliacoes += cromossomo.avaliar(modelo)
        
        return sorted(self.populacao, key = lambda x: x.avaliacao, reverse=True)

    def roleta(self):
        limite = random.random() * self.soma_avaliacoes ##Gera um limite baseado na avaliação da População
        i, aux = [0, 0]
        ##random.shuffle(self.populacao) ## "Embaralha" a população aleatoriamente
        while aux < limite and i < self.tam_populacao:
            aux += self.populacao[i].avaliacao
            i += 1
        i -= 1
        return i       

    def nova_geracao(self):
        nova_populacao = []
        for i in range(self.tam_populacao):
            pai1 = self.populacao[self.roleta()]
            pai2 = self.populacao[self.roleta()]
            filho = pai1.crossover(pai2)
            filho.mutacao(.05)
            nova_populacao.append(filho)
        return nova_populacao
    
    def informaModelo(self):
        print("Digite seu modelo:")
        input_model = input()
        input_model_split = input_model.split()
        model = []
        for i in input_model_split:
            if re.match('^\d+$',i): model.append(int(i))
            else: model.append(i)
                
        return model
    
    def executar(self):
        model = self.informaModelo()
        populacoes = []
        tam_model = len(model)
        
        self.inicializar_populacao(tam_model)
        ordenado = self.avaliar_populacao(model)
        
        
        for i in range(self.geracoes):
            self.melhores.append(ordenado[0])
            populacoes.append(self.populacao)
            for top in ordenado:
                print("geração {}, Cromossomo:{}".format(i, top))
            
            self.populacao = self.nova_geracao()
            ordenado = self.avaliar_populacao(model)
        
        print("\n############## BESTS ######################\n")
        for top in sorted(self.melhores, key = lambda x: x.avaliacao, reverse = True):
            print(top)
        print("\n############## BESTS ######################\n")

ga = GATest(5,10)
ga.executar()