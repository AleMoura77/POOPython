
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def titular(self):
        return self.__titular
    @property
    def saldo(self):
        return self.__saldo
    @property
    def limite(self):
        return self.__limite
    
    @staticmethod
    def codigo_banco():
        return "001"
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    @saldo.setter    
    def saldo(self, saldo):
        self.__saldo = saldo
    @limite.setter    
    def limite(self, limite):
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))
        
    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        valor_disponivel = self.saldo + self.limite
        return valor <= valor_disponivel 
        
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else: 
            print("O valor {} passou o limite".format(valor)) 
        
    def transfera(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        
                