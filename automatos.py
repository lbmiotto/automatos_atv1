# Esse código em Python define uma classe Automato que representa um autômato finito determinístico, ou AFD,
# e permite simular o processamento de cadeias de entrada nesse autômato.

class Automato:

    # A função "INIT" é o contrutor da classe "Automato", e ele é responsável por receber todas as informações que vão ser necessárias
    # para definir o automato, sendo essas informações as seguintes: Estados, Alfabeto, Transições, Estado Inicial e Estado de aceitação.

    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_aceitacao):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_aceitacao = estados_aceitacao

    # A função "simular" é o método responsável pela simulação (processamento) da cadeia de entrada do automato, ou seja, ele faz uma
    # verificação de aceitação ou negação pelo automato, e retorna uma mensagem de acordo com o caso

    def simular(self, entrada):
        estado_atual = self.estado_inicial
        caminho = [(estado_atual, "")]

        for simbolo in entrada:
            if simbolo not in self.alfabeto:
                return "Erro: símbolo não está no alfabeto"

            if (estado_atual, simbolo) in self.transicoes:
                estado_atual = self.transicoes[(estado_atual, simbolo)]
                caminho.append((estado_atual, simbolo))
            else:
                return "Erro: não foi possível aplicar uma transição"

        if estado_atual in self.estados_aceitacao:
            caminho_str = " -> ".join(f"({estado}, {simbolo})" for estado, simbolo in caminho)
            return f"A sua cadeia foi aceita! Caminho: {caminho_str}"
        else:
            return "A sua cadeia foi rejeitada!"

# A função "main" é a função principal do código, pois ela é responsável pelas seguintes etapas:
#
# 1- Pedir pro usuário o nome do arquivo txt que tem a definição do automato.
# 2- Lê as linhas do arquivo para extrair as informações (As informações são as que foi citado anteriormente no construtor da classe Automato).
# 3- Começa um loop onde o usuário pode colocar as cadeias de entrada para fazer a simulação.
# 4- Mostra uma opção de saída pro usuário, sendo a opção de escrever "exit"
# 5- Caso tudo da forma correta, a cadeia de entrada é passada pela o método simular e mostra o resultado.

def main():
    nome_arquivo = input("Informe o nome ou o caminho do arquivo: ")

    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    estados = set(linhas[0].strip().split())
    alfabeto = set(linhas[1].strip().split())
    estado_inicial = linhas[2].strip()
    estados_aceitacao = set(linhas[3].strip().split())

    transicoes = {}
    for linha in linhas[4:]:
        partes = linha.strip().split()
        transicoes[(partes[0], partes[1])] = partes[2]

    automato = Automato(estados, alfabeto, transicoes, estado_inicial, estados_aceitacao)

    # Loop de interação infinita
    while True:
        entrada = input("Digite uma cadeia de entrada (ou 'exit' para sair): ")
        if entrada.lower() == 'exit':
            break
        resultado = automato.simular(entrada)
        print(resultado)

# Esse bloco, garante que o código seja executado apenas se o arquivo for executado diretamente.
if __name__ == "__main__":
    main()
