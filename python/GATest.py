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
        for cromossomo in self.populacao:
            cromossomo.inicializar()
            print(cromossomo)
            
    def avaliar_populacao(self):##Em construção
        for cromossomo in self.populacao:
            self.soma_avaliacoes += cromossomo.avaliar()
        
        return self.populacao

    def roleta(self):
        limite = random.random() * self.soma_avaliacoes ##Gera um limite baseado na avaliação da População
        i, aux = [0, 0]
        random.shuffle(self.populacao) ## "Embaralha" a população aleatoriamente
        while aux <= limite and i < self.tam_populacao:
            aux += self.populacao[i].avaliacao_cobertura
            i += 1
        i -= 1
        return i       

    def nova_geracao(self, tam_filhos):
        nova_populacao = []
        for i in range(self.tam_populacao):
            pai1 = self.populacao[self.roleta()]
            pai2 = self.populacao[self.roleta()]
            filho = pai1.crossover(pai2, tam_filhos)
            filho.mutacao(.05)
            nova_populacao.append(filho)
        return nova_populacao
    
    def executar(self):
        populacoes = []
        tam_cromossomo = 1
        self.inicializar_populacao(tam_cromossomo)    
        populacoes.append(self.avaliar_populacao())
        
        tam_cromossomo = 2
        while(tam_cromossomo <= 10):
            print("\n*** Geracao {} ***".format(tam_cromossomo))
            self.populacao = self.nova_geracao(tam_cromossomo)
            populacoes.append(self.avaliar_populacao())
            for ind in self.populacao:
                print(ind)
            
            tam_cromossomo += 1
        
        ##for tam_cromossomo in range(8):
            
        
        
        
        

        

        


        
if __name__ == "__main__":
    ga = GATest(4,5)     
    ga.executar()