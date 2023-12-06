from operacoesbd import *

"""
Para criar as tabela no SQL

create table ouvidoriajoalyson.reclamacao (
id int auto_increment,
titulo varchar(30),
usuario varchar(30),
descricao varchar(100),
situacao varchar (15),
tipo varchar (20),
primary key(id)); 

create table ouvidoriajoalyson.elogio (
id int auto_increment,
titulo varchar(30),
usuario varchar(30),
descricao varchar(100),
situacao varchar (15),
tipo varchar (20),
primary key(id)); 

create table ouvidoriajoalyson.sugestao (
id int auto_increment,
titulo varchar(30),
usuario varchar(30),
descricao varchar(100),
situacao varchar (15),
tipo varchar (20),
primary key(id)); """


#Metodos Manifestação
def addManifestacao(novaManifestacaoTitulo,novaManifestacaoUsuario,novaManifestacaoDescricao,novaManifestacaoSituacao,novaManifestacaoTipo,conexao):

    if novaManifestacaoTipo == 1:
        sqlInsercao = 'insert into reclamacao (titulo,usuario,descricao,situacao,tipo) values(%s,%s,%s,%s,%s)'
        valores = [novaManifestacaoTitulo, novaManifestacaoUsuario, novaManifestacaoDescricao,
                       novaManifestacaoSituacao,"Reclamação"]
        manifestacaoAdded = insertNoBancoDados(conexao, sqlInsercao, valores)
    elif novaManifestacaoTipo == 2:
        sqlInsercao = 'insert into elogio (titulo,usuario,descricao,situacao,tipo) values(%s,%s,%s,%s,%s)'
        valores = [novaManifestacaoTitulo, novaManifestacaoUsuario, novaManifestacaoDescricao,
                       novaManifestacaoSituacao,"Elogio"]
        manifestacaoAdded = insertNoBancoDados(conexao, sqlInsercao, valores)
    elif novaManifestacaoTipo == 3:
        sqlInsercao = 'insert into sugestao (titulo,usuario,descricao,situacao,tipo) values(%s,%s,%s,%s,%s)'
        valores = [novaManifestacaoTitulo, novaManifestacaoUsuario, novaManifestacaoDescricao,
                       novaManifestacaoSituacao,"Sugestão"]
        manifestacaoAdded = insertNoBancoDados(conexao, sqlInsercao, valores)
    else:
        manifestacaoAdded = 0

    if manifestacaoAdded == 0:
        val = "Error"
    else:
        val = manifestacaoAdded
    return val


def pesquisarManifestacao(posicaoManifestacao,conexao,tipo):
    if tipo == 1:
        consultaListagem = 'select * from reclamacao where id =' + str(posicaoManifestacao)
        manifestacaoPesquisada = listarBancoDados(conexao, consultaListagem)
    elif tipo == 2:
        consultaListagem = 'select * from elogio where id =' + str(posicaoManifestacao)
        manifestacaoPesquisada = listarBancoDados(conexao, consultaListagem)
    elif tipo == 3:
        consultaListagem = 'select * from sugestao where id =' + str(posicaoManifestacao)
        manifestacaoPesquisada = listarBancoDados(conexao, consultaListagem)
    else:
        manifestacaoPesquisada = "Error"

    if manifestacaoPesquisada==[]:
        val = "Error"
    else:
        val = manifestacaoPesquisada
    return val


def removerManifestacao(manifestacao,conexao,tipo):
    if tipo == 1:
        consultaListagem = 'delete from reclamacao where id = %s '
        dados = [manifestacao]
        manifestacaoRemovida = excluirBancoDados(conexao, consultaListagem, dados)
    elif tipo == 2:
        consultaListagem = 'delete from elogio where id = %s '
        dados = [manifestacao]
        manifestacaoRemovida = excluirBancoDados(conexao, consultaListagem, dados)
    elif tipo == 3:
        consultaListagem = 'delete from sugestao where id = %s '
        dados = [manifestacao]
        manifestacaoRemovida = excluirBancoDados(conexao, consultaListagem, dados)
    else:
        manifestacaoRemovida = 0

    if manifestacaoRemovida > 0:
        val = True
    else:
        val = False
    return val

def alterarManifestacao(posicao,manifestacao,tipo,oqueAlterar,conexao):
    global sqlAtualizar, valores
    if tipo == 1: #Alterar reclamacao
        if oqueAlterar == 1:
            sqlAtualizar = 'update reclamacao set titulo = %s  where id = %s'
            valores = [manifestacao, posicao]
        elif oqueAlterar == 2:
            sqlAtualizar = 'update reclamacao set usuario = %s  where id = %s'
            valores = [manifestacao, posicao]
        elif oqueAlterar == 3:
            sqlAtualizar = 'update reclamacao set descricao = %s  where id = %s'
            valores = [manifestacao, posicao]
        elif oqueAlterar == 4:
            sqlAtualizar = 'update reclamacao set situacao = %s  where id = %s'
            valores = ["Fechada", posicao]
        else:
            manifestacaoAlterada = 0

    elif tipo == 2: #Alterar elogio
        if oqueAlterar == 1:
            sqlAtualizar = 'update elogio set titulo = %s  where id = %s'
            valores = [manifestacao, posicao]
        elif oqueAlterar == 2:
            sqlAtualizar = 'update elogio set usuario = %s  where id = %s'
            valores = [manifestacao, posicao]
        elif oqueAlterar == 3:
            sqlAtualizar = 'update elogio set descricao = %s  where id = %s'
            valores = [manifestacao, posicao]
        elif oqueAlterar == 4:
            sqlAtualizar = 'update elogio set situacao = %s  where id = %s'
            valores = ["Fechada", posicao]
        else:
            manifestacaoAlterada = 0

    elif tipo == 3: #Alterar sugestao
        if oqueAlterar == 1:
            sqlAtualizar = 'update sugestao set titulo = %s  where id = %s'
            valores = [manifestacao, posicao]
        elif oqueAlterar == 2:
            sqlAtualizar = 'update sugestao set usuario = %s  where id = %s'
            valores = [manifestacao, posicao]
        elif oqueAlterar == 3:
            sqlAtualizar = 'update sugestao set descricao = %s  where id = %s'
            valores = [manifestacao, posicao]
        elif oqueAlterar == 4:
            sqlAtualizar = 'update sugestao set situacao = %s  where id = %s'
            valores = ["Fechada", posicao]
        else:
            manifestacaoAlterada = 0
    else:
        manifestacaoAlterada = 0

    manifestacaoAlterada = atualizarBancoDados(conexao, sqlAtualizar, valores)

    if manifestacaoAlterada > 0:
        val = True
    else:
        val = False
    return val


