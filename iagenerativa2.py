import ollama as ola


# Inicialize o cliente Olhama
# client = ollama(api_key='aacb1008-4be8-4b1e-8649-3f292a796a31')

# Função que gera a resposta com o Olhama
def gerar_resposta(prompt):
    response = ola.generate(model='llama3', prompt=prompt)
    return response['response']  # Ajuste conforme o formato de resposta do Ollama

# Função do menu
def menu():
    print("Escolha uma opção:")
    print("1 - Completar uma história")
    print("2 - Responder uma pergunta técnica")
    print("3 - Gerar descrição de um produto")
    opcao = int(input("Digite o número da sua opção: "))
    return opcao

def switch_case(opcao):
    switcher = {
            1: 'Explique o conceito central do "Quarto Chinês" de John Searle em termos simples, como se estivesse explicando para um iniciante. Inclua um exemplo prático para ilustrar o argumento.',
            2: 'Descreva como o "Quarto Chinês" de Searle argumenta contra a inteligência artificial forte. Use dois exemplos práticos para apoiar sua explicação.',
            3: 'Compare o "Quarto Chinês" com o funcionalismo de Jerry Fodor, utilizando um exemplo prático para destacar as principais diferenças. Responda em dois parágrafos.',
            4: 'Liste três críticas ao "Quarto Chinês" e, em seguida, explique como Searle responde a cada uma. Estruture a resposta em tópicos.',
            5: 'Como o "Quarto Chinês" questiona a ideia de que computadores podem realmente entender o significado (semântica)? Explique em dois parágrafos com um exemplo prático.',
            6: 'Qual é a diferença entre "entendimento" e "simulação" no contexto do "Quarto Chinês"? Responda em um parágrafo curto.',
            7: 'Dê um exemplo prático que demonstre o experimento mental do "Quarto Chinês" e explique como ele refuta a noção de compreensão em máquinas.',
            8: 'Explique uma implicação prática do "Quarto Chinês" para o desenvolvimento atual de inteligência artificial. Dê um exemplo aplicado.',
            9: 'Explique por que Searle acredita que o "Quarto Chinês" refuta a noção de consciência em máquinas, e dê um exemplo de como isso se aplica em tecnologias de IA modernas.',
            10: 'Compare o "Quarto Chinês" com a hipótese do cérebro de Turing, focando em como cada um trata a questão da consciência nas máquinas. Dê um exemplo de como esses argumentos diferem.',
            11: 'O "Quarto Chinês" é uma crítica válida às atuais tecnologias de IA? Explique com exemplos e responda em dois parágrafos curtos.',
            12: 'Como o "Quarto Chinês" pode ser relacionado ao debate sobre a diferença entre mente e máquina? Dê um exemplo de como isso afeta as discussões sobre IA.'
        }
    # Retorna o prompt correspondente ou uma mensagem padrão para opção inválida
    return switcher.get(opcao, "Opção inválida!")

# Função principal
def main():
    opcao = menu()
    prompt = switch_case(opcao)
    
    if prompt == "Opção inválida!":
        print(prompt)
    else:
        print(f"Prompt selecionado: {prompt}")

    print("\nResposta da IA:")
    print(gerar_resposta(prompt))

main()