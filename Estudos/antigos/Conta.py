import datetime
class Historico():
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []
    def imprime (self):
        print("data da abertura {}".format(self.data_abertura))
        print("transações")
        for c in self.transacoes:
            print("-",c)

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
class Conta:   
    def __init__ (self,numero,cliente,saldo,limite = 1000):
        print("inicializando uma conta")
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def depositar(self, valor):
           self.saldo += valor
           self.historico.transacoes.append("deposito de {}".format(valor))

    def sacar (self,valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))
            return True

    def extrato (self):
        print("numero:{}\nsaldo:{}".format(self.numero,	self.saldo))
        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))
    
    def transfere(self, conta, valor):
        retira = self.sacar(valor)
        if (retira == False):
            return False
        else:
            conta.depositar(valor)
            self.historico.transacoes.append("tranferencia para conta {} de R$ {}".format(conta.numero,valor))
            return True

