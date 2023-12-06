import Implementation
from operacoesbd import *
#Abrir conexao com banco de dados
conexao = abrirBancoDados('localhost', 'root', '12345', 'ouvidoriajoalyson')

print("Bem vindo a ouvidoria da Universidade ABC 🏫, o que deseja efetuar: 👇")

opcao = 0
while opcao != 6:
    print()
    opcao = int(input(("📢 1)Listar Manifestação 2)Adicionar Manifestação 3)Pesquisar Manifestação"
          " 4)Remover Manifestação 5)Alterar Manifestação 6)Sair -> ")))

    if opcao == 1:
        #listagem
        tipoLista = int(input("Qual tipo de lista deseja exibir 1)Reclamação 2)Elogio 3)Sugestão -> "))
        if tipoLista == 1:
            consultaListagem = 'select * from reclamacao'
        elif tipoLista == 2:
            consultaListagem = 'select * from elogio'
        elif tipoLista == 3:
            consultaListagem = 'select * from sugestao'
        else:
            print("Tipo de lista inválida 😡")

        manifestacoes = listarBancoDados(conexao, consultaListagem)
        if len(manifestacoes) > 0:
            for i in manifestacoes:
                print("A manifestação -> {}, com título: {}. Do usuário:{}. Com descrição: {}, está em: {} do tipo: {}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
        else:
            print("Não há manifestações")

    elif opcao == 2:
        #Add manifestções
        novaManifestacaoTitulo = input("Digite o titulo da nova manifestação: ")
        novaManifestacaoUsuario = input("Digite o usuario da nova manifestação: ")
        novaManifestacaoDescricao = input("Digite a descrição da nova manifestação: ")
        novaManifestacaoSituacao = "Aberta" #Aberta por padrão
        novaManifestacaoTipo = int(input("Qual tipo de lista deseja adicionar 1)Reclamação 2)Elogio 3)Sugestão -> "))

        validacao = Implementation.addManifestacao(novaManifestacaoTitulo, novaManifestacaoUsuario,
                                                   novaManifestacaoDescricao, novaManifestacaoSituacao,
                                                   novaManifestacaoTipo, conexao)
        if validacao == "Error":
            print("Não foi possivel adicionar sua manifestação")
        else:
            print("A manifestação: {}-{}, foi adicionada com sucesso".format(validacao,novaManifestacaoTitulo))

    elif opcao == 3:
        # Pesquisar manifestações
        tipoLista = int(input("Qual tipo de lista deseja pesquisar 1)Reclamação 2)Elogio 3)Sugestão -> "))
        posicaoManifestacao = int(input("Digite o código da manifestação para pesquisar: "))
        manifestacaoPesquisada = Implementation.pesquisarManifestacao(posicaoManifestacao,conexao,tipoLista)

        if manifestacaoPesquisada == "Error":
            print("Essa manifestação não existe")
        else:
            for i in manifestacaoPesquisada:
                print("A manifestação que você pesquisou foi -> {}, com título: {}. Do usuário:{}. Com descrição: {}, está em: {} do tipo: {}".format(i[0], i[1], i[2], i[3], i[4], i[5]))

    elif opcao == 4:
        #Remover manifestações
        tipoLista = int(input("Qual tipo de lista deseja remover 1)Reclamação 2)Elogio 3)Sugestão -> "))
        manifestacaoRemover = int(input("Digite o código da manifestação para remover: "))

        manifestacaoRemovida = Implementation.pesquisarManifestacao(manifestacaoRemover,conexao,tipoLista)
        validacao = Implementation.removerManifestacao(manifestacaoRemover,conexao,tipoLista)
        if validacao is True:
            print("A manifestação: {}, foi removida com sucesso".format(manifestacaoRemover))
        else:
            print("Não foi possivel remover sua manifestação")

    elif opcao == 5:
        #Alterar manifestações
        tipoLista = int(input("Qual tipo de lista deseja alterar 1)Reclamação 2)Elogio 3)Sugestão -> "))
        posicaoManifestacaoAlterar = int(input("Digite o códio da manifestação para alterar: "))
        oqueAlterar = int(input("O que deseja alterar 1)Titulo 2)Usuario 3)Descrição 4)Fechar manifestação -> "))
        if oqueAlterar != 4:
            novaManifestacao = input("Digite a alteração da manifestação: ")
        else:
            novaManifestacao = "Fechada"
        manifestacaoAlterada = Implementation.pesquisarManifestacao(posicaoManifestacaoAlterar,conexao,tipoLista)
        validacao = Implementation.alterarManifestacao(posicaoManifestacaoAlterar,novaManifestacao,tipoLista,oqueAlterar,conexao)

        if validacao is True:
            print("A manifestação foi alterada para {} com sucesso".format(novaManifestacao))
        else:
            print("Não foi possivel alterar sua manifestação")

    elif opcao != 6:
        print("Opção inválida 😡")
    else:
        print("Sessão encerrada 👋")

encerrarBancoDados(conexao)