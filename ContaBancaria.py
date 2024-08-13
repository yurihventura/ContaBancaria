class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
    def depositar (self, valor):
        self.saldo += valor
        print (f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")
        
    def sacar(self, valor):
        if valor <= self.saldo: 
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}")
        else: 
            print("Saldo insuficiente. Operação não realizada.")
    
    def transferir(self, destinatario, valor):
        if valor > 0: 
            if valor <= self.saldo:
                self.saldo -= valor 
                destinatario.depositar (valor)
                print(f"Transferencia de R$(valor) realizada. Novo saldo: R${self.saldo}")
        else: 
            print("Valor inválido para transferência. Transfêrencia não realizada.")
            
def obter_valor_input (mensagem):
        while True: 
            try: 
                valor = float(input (mensagem))
                return valor 
            except ValueError: 
                print("Por favor, insira um valor numérico válido")  
                
                
conta1_saldo_inicial = obter_valor_input("Informe o saldo inicial da conta 1: R$")
conta2_saldo_inicial = obter_valor_input("Informe o saldo inicial da conta 2: R$")            

conta1 = ContaBancaria(conta1_saldo_inicial)
conta2 = ContaBancaria(conta2_saldo_inicial)

while True:
    print("\nOpções:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Transferir")
    print("4. Sair")
    
    escolha = input("Escolha uma opção ( 1-4): ")
    
    if escolha == "1":
        valor_deposito = obter_valor_input("Informe o valor a ser depositado na Conta 1: R$")
        conta1.depositar(valor_deposito)
    elif escolha == "2": 
        valor_saque = obter_valor_input("Informe o valor a ser sacado na Conta 1: R$")
        conta1.sacar(valor_saque)
    elif escolha == "3":
        valor_transferencia = obter_valor_input("Informe o valor a ser transferido da Conta 1 para a Conta 2: R$")
        conta1.transferir(conta2, valor_transferencia)
    elif escolha == "4":
        break
        
print("\nSaldos Finais:")
print(f"Conta 1: R$ {conta1.saldo}")
print(f"Conta 2: R$ {conta2.saldo}")