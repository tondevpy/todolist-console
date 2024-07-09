import os

def criar():
    nomeTarefa = input('Informe o nome da tarefa: ').lower()
    if nomeTarefa:
        tarefa = f'Tarefa: {nomeTarefa} - Status: \033[91mNão Concluída\033[0m'

        with open('tarefas.txt', 'a', encoding='utf-8') as tarefas:
            tarefas.writelines(tarefa + '\n')

    else:
        print('O nome da tarefa não pode ser vazio!')

def visualizar():
    
    with open('tarefas.txt', 'r', encoding='utf-8') as lerTarefas:
        LerConteudo = lerTarefas.readlines()
        for linha in LerConteudo:
            print(linha)

        if len(LerConteudo) == 0:
            print('\033[91mNenhuma tarefa encontrada...\033[0m')


def finalizar():
    print('\nLista com todas as tarefas disponíveis...\n\n')
    with open('tarefas.txt', 'r', encoding='utf-8') as lerTarefas:
        LerConteudo = lerTarefas.readlines()
        for linha in LerConteudo:
            print(linha)

        if len(LerConteudo) == 0:
            print('\033[91mNenhuma tarefa encontrada...\033[0m')

    tarefa = input('Nome da terefa que deseja finalizar: ')
    if tarefa:

        with open('tarefas.txt', 'r', encoding='utf-8') as lerTarefas:
            LerConteudo = lerTarefas.readlines()
            
        with open('tarefas.txt', 'w', encoding='utf-8') as alterarTarefa:
            for linha in LerConteudo:
                if tarefa in linha:
                    linha = linha.replace('Não Concluída', '\033[92mFinalizada\033[0m')
                    
                
                alterarTarefa.write(linha)
    else:
        print('Precisa informar o nome da tarefa!')

def excluir():
    alteracao = ''
    nomeTarefa = input('Informe o nome da tarefa que deseja excluir: ')

    with open('tarefas.txt', 'r', encoding='utf-8') as lerTarefas:
        LerConteudo = lerTarefas.readlines()
        
    with open('tarefas.txt', 'w', encoding='utf-8') as alterarTarefa:
        for linha in LerConteudo:
            if nomeTarefa in linha:
                linha = ''
                alteracao = 'Tarefa excluida com sucesso!'
            alterarTarefa.write(linha)
            
        if 'sucesso' in alteracao:
            print(alteracao)
        else:
            print(f'Tarefa informada {nomeTarefa} não encontrada!')

try:
    while True:
        print('\n\n          Bem vindo a gerenciador de tarefas - feito por TonDevpy\n\n')
        print('Escolha uma das opções desejadas:')
        print('[1] - Criar tarefa')
        print('[2] - Visualizar tarefas')
        print('[3] - Finalizar tarefa')
        print('[4] - Excluir tarefas')
        print('[5] - Encerrar programa')
        opcao = input('\n\n\033[92mQual opção desejada ?\033[0m \n')

        if opcao == '1':
            criar()
            input('\033[94mPressione Enter para prosseguir para o menu!\033[0m')
        if opcao == '2':
            visualizar()
            input('\033[94mPressione Enter para prosseguir para o menu!\033[0m')
        if opcao == '3':
            finalizar()
            input('\033[94mPressione Enter para prosseguir para o menu!\033[0m')

        if opcao == '4':
            excluir()
            input('\033[94mPressione Enter para prosseguir para o menu!\033[0m')
        if opcao == '5':
            print('\033[91mObrigado por utilizar nosso software!\n\n')
            break

        os.system('cls')
except:
    print('Ocorreu um erro!')

