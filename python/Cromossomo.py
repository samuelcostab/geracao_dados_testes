import math, random
import string

class Cromossomo():

    def __init__(self, tamanho):
        self.lista_modelos = self.criaListaModelos()
        self.tamanho = tamanho
        self.valor = []
        self.avaliacao = 0

    
    def criaListaModelos(self):##Esta sendo usado
        mod1 = list(range(0,10))
        mod2 = list(string.ascii_uppercase)
        
        #modelo = [[1..9],[A..Z]]
        modelo = [mod1, mod2]
        
        return modelo
        
    def getLetraRandom(self):##Esta sendo usado
        i = random.randint(0,25)
        
        return self.lista_modelos[1][i]
    
    def set_valor(self, novo_valor):##Esta sendo usado
        self.valor = novo_valor
    
    def inicializar(self):##Esta sendo usado
        novo_valor = []
        for i in range(self.tamanho):
            if random.random() < .5: ##Se valor.randômico < 0.50, adiciona um numero aleatório
                novo_valor.append(random.randint(0,9))
            else: novo_valor.append(self.getLetraRandom())
                
        self.set_valor(novo_valor)

    def crossover(self, outro_cromossomo):
        split_index = int(random.random() * self.tamanho) ##Gera o índice onde vai ocorrer a troca de Genes
        novo_valor = []
        if random.random() > .5:##Se a probabilidade for maior que 50%
            novo_valor = self.valor[0:split_index] + outro_cromossomo.valor[split_index:len(outro_cromossomo.valor)]
        else:
            novo_valor = outro_cromossomo.valor[0:split_index] + self.valor[split_index:len(outro_cromossomo.valor)]
        novo_cromossomo = Cromossomo(self.tamanho)
        novo_cromossomo.set_valor(novo_valor)
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
            

    def valor_real(self, inf = 0, sup = 100):
        return inf + (sup - inf)/(2**self.tamanho - 1)*int(self.valor, 2)

    def avaliar(self, modelo):##Esta sendo usado
        for i in range(len(modelo)):
            if type(self.valor[i]) == type(modelo[i]):
                self.avaliacao += 1

        return self.avaliacao

    def __repr__(self):

        return "cromossomo:[%s] avaliacao[%.2f]" % (self.valor, self.avaliacao)