class Calculadora:
    def __init__(self):
        self.historico = []

    def somar(self, a, b):
        result = a + b
        self.historico.append(f"{a} + {b} = {result}")
        return result

    def subtr(self, a, b):
        result = a - b
        self.historico.append(f"{a} - {b} = {result}")
        return result

    def multipl(self, a, b):
        resultado = a * b
        self.historico.append(f"{a} * {b} = {resultado}")
        return resultado

    def dividir(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero!"
        resultado = a / b
        self.historico.append(f"{a} / {b} = {resultado}")
        return resultado

    def mostrar_historico(self):
        if not self.historico:
            print("Nenhuma operação realizada ainda.")
        else:
            print("Histórico de operações:")
            for operacao in self.historico:
                print(operacao)


calculadora = Calculadora()

try:
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
except ValueError:
    print("Por favor, digite números válidos.")
else:
    print(f"Soma: {calculadora.somar(num1, num2)}")
    print(f"Subtração: {calculadora.subtr(num1, num2)}")
    print(f"Multiplicação: {calculadora.multipl(num1, num2)}")
    print(f"Divisão: {calculadora.dividir(num1, num2)}")

    calculadora.mostrar_historico()