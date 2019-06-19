import math, random
import string
import re

class GATest():

    def __init__(self, tamanho_populacao, geracoes):
        self.populacao = []
        self.tam_populacao = tamanho_populacao
        self.geracoes = geracoes
        self.soma_coberturas = 0
        self.melhores = []
        
                                ##    1     2     3     4
        self.criterios_atingidos = [False,False,False,False]
    
    
    def inicializar_populacao(self, tam_cromossomo):
        for i in range(self.tam_populacao):
            self.populacao.append(Cromossomo(tam_cromossomo))
        for cromossomo in self.populacao:
            cromossomo.inicializar()
            
    def informar_Cobertura(self, valor):
        print("\nAvaliar Cromossomo: {}".format(valor))
        entrada = input("Critério e Cobertura atingida:").split(" ")
        
        criterios = entrada[0].split(",") ##tem que trabalhar com essa variavel
        taxa_cobertura = int(entrada[1])
        
        return taxa_cobertura
            
    def avaliar_populacao(self):##Em construção        
        for cromossomo in self.populacao:
            taxa_cobertura = self.informar_Cobertura(cromossomo.valor)
            cromossomo.set_cobertura(taxa_cobertura)
            self.soma_coberturas += cromossomo.cobertura
        
        soma_probabilidade = 0
        for cromossomo in self.populacao:
            cromossomo.avaliar_cobertura(self.soma_coberturas)
            soma_probabilidade += cromossomo.avaliacao_cobertura
            cromossomo.probabilidade_acumulada = soma_probabilidade
        
        return self.populacao

    def roleta(self):
        limite = (random.random() * self.soma_coberturas) % 1 ##Gera um limite baseado na avaliação da População sempre < 1
        self.populacao = sorted(self.populacao, key = lambda x: x.probabilidade_acumulada)
        
        
        if(limite > 0):
            i = 0
            for cromossomo in self.populacao:
                if(limite <= cromossomo.probabilidade_acumulada):
                    return i
                i += 1
        
        i = random.randint(0,(self.tam_populacao - 1))
            
        return i
            

    def nova_geracao(self, tam_filhos):
        nova_populacao = []
        for i in range(self.tam_populacao):
            pai1 = self.populacao[self.roleta()]
            pai2 = self.populacao[self.roleta()]
            filho = pai1.crossover(pai2, tam_filhos)
            filho.mutacao(.10)
            nova_populacao.append(filho)
        return nova_populacao
    
    def executar(self):
        populacoes = []
        tam_cromossomo = 1
        self.inicializar_populacao(tam_cromossomo)    
        populacoes.append(self.avaliar_populacao())
        
        tam_cromossomo = 2
        while(tam_cromossomo <= 20):
            print("\n*** Geracao {} ***".format(tam_cromossomo))
            self.populacao = self.nova_geracao(tam_cromossomo)
            populacoes.append(self.avaliar_populacao())
            '''for ind in self.populacao:
                print(ind)'''
            
            tam_cromossomo += 1     
        

        
if __name__ == "__main__":
    ga = GATest(4,5)     
    ga.executar()