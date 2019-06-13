import math, random
import string

class Cromossomo():

    def __init__(self, tamanho):
        self.lista_modelos = self.criaListaModelos()
        self.tamanho = tamanho
        self.valor = []
        self.avaliacao_cobertura = 0

    
    def criaListaModelos(self):##Esta sendo usado
        mod1 = list(range(0,10))
        mod2 = list(string.ascii_uppercase)
        
        #modelo = [[1..9],[A..Z]]
        modelo = [mod1, mod2]
        
        return modelo
        
    def getLetraRandom(self):##Esta sendo usado
        i = random.randint(0,25)
        
        return self.lista_modelos[1][i]
    
    def set_valor(self,split_index, novo_valor):
        self.valor = novo_valor[0:split_index] + self.valor[split_index:self.tamanho]
    
    def inicializar(self):##Esta sendo usado
        novo_valor = []
        for i in range(self.tamanho):
            if random.random() < .5: ##Se valor.randômico < 0.50, adiciona um numero aleatório
                novo_valor.append(random.randint(0,9))
            else: novo_valor.append(self.getLetraRandom())
                
        self.valor = novo_valor

    def crossover(self,outro_cromossomo, tam_filho):
        novo_cromossomo = Cromossomo(tam_filho)
        novo_cromossomo.inicializar()
        
        split_index = int(random.random() * self.tamanho) ##Gera o índice onde vai ocorrer a troca de Genes
        novo_valor = []
        if random.random() > .5:##Se a probabilidade for maior que 50%
            novo_valor = self.valor[0:split_index] + outro_cromossomo.valor[split_index:len(outro_cromossomo.valor)]
        else:
            novo_valor = outro_cromossomo.valor[0:split_index] + self.valor[split_index:len(outro_cromossomo.valor)]
        
        tamanho_pai = self.tamanho
        
        novo_cromossomo.set_valor(tamanho_pai, novo_valor)
        
        return novo_cromossomo

    def mutacao(self, chance_mutacao):
        inicio, fim = [[],[]]
        for i in range(self.tamanho):
            if random.random() < chance_mutacao:
                inicio = self.valor[0:i]
                fim = self.valor[i+1:self.tamanho]
                aux = self.valor[i]
                if type(aux) == int : aux = self.getLetraRandom() ##Coloca uma letra aleatória na posição mutada
                else: aux = random.randint(0,9) ##Coloca um número, caso contrário
                self.valor = self.concatena_valores(inicio,aux,fim)
                
    def concatena_valores(self, a ,b ,c):
        resultado = []
        for i in range(len(a)):
            resultado.append(a[i])
            
        resultado.append(b)
        
        for i in range(len(c)):
            resultado.append(c[i])
        
        return resultado

    def avaliar(self):##Em construção
        print("Av. Cromossomo: {}".format(self.valor))
        cobertura = int(input("Cobertura atingida:"))
        
        self.avaliacao_cobertura = cobertura / 100
        
        return self.avaliacao_cobertura

    def __repr__(self):

        return "cromossomo:[%s] avaliacao[%.2f]" % (self.valor, self.avaliacao_cobertura)