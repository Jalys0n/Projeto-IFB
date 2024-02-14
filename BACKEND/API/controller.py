import random
import string
from conexao import conexao


# FUNÇÕES PARA GERAR SENHAS:

def gerarSenhaNormal():
    letras = string.ascii_uppercase
    letras = ''.join(random.choice(letras) for _ in range(3))
    numeros = ''.join(random.choice(string.digits) for _ in range(3)) 
    senha = letras + numeros   

    return senha


def gerarSenhaPreferencial():
   letras = 'PREF'
   numeros = ''.join(random.choice(string.digits) for i in range(3))
   senha = letras + numeros
   return senha





#table usuario
def cadastrarUsuario(cpf_usuario, nome, fk_tipo_usuario):
    cursor = conexao.cursor()
    sql = 'INSERT INTO usuarios (cpf_usuario, nome, fk_tipo_usuario) VALUES (%s,%s,%s)'
    cursor.execute(sql, (cpf_usuario, nome, fk_tipo_usuario))
    conexao.commit()
    cursor.close()


#atendimentos 

#para cadastrar o atendimento assim que a pessoa fizer o cadastro

def cadastrarAtendimento(fk_cpf_usuario, fk_idSenha, fk_tipo_atendimento):
   cursor = conexao.cursor()
   sql = 'INSERT INTO atendimentos (fk_cpf_usuario, fk_idSenha, fk_tipo_atendimento) values (%s,%s,%s)'
   cursor.execute(sql,(fk_cpf_usuario, fk_idSenha, fk_tipo_atendimento))
   conexao.commit()
   cursor.close()      

def listarAtendimento():
   sql = 'SELECT * FROM atendimentos'
   cursor = conexao.cursor()
   cursor.execute(sql)
   resultado = cursor.fetchall()
   cursor.close()
   return resultado


#função pra ser chamada quando terminar o atendimento


def incluirTerminoAtendimento(idSenha):
    sql = 'UPDATE atendimentos SET finalAtendimento = CURRENT_TIMESTAMP WHERE fk_idSenha = ?'
    cursor = conexao.cursor()
    cursor.execute(sql, (idSenha,))
    conexao.commit()
    cursor.close()



#senhas

def listarSenhas():
    sql = 'SELECT idSenha FROM senhas WHERE fk_Status_senha = 1 ORDER BY idSenha ASC LIMIT 1'
    cursor = conexao.cursor()
    cursor.execute(sql)
    senha = cursor.fetchone()
    print(type(senha))
    cursor.close()
    return senha

               #cadastrar na tabela senha assim que a pessoa fizer o cadastro
def cadastrarNaTabelaSenha(idSenha):
    sql = 'INSERT INTO senhas (idSenha, fk_status_senha) VALUES (%s, 1)'
    cursor = conexao.cursor()
    cursor.execute(sql, (idSenha,))
    conexao.commit()
    cursor.close()


                #chamou a senha? ai a gente precisa alterar o status da senha, e claro PRECISA existir uma função que altera de novo se a pessoa desistir

def alterarStatus(idSenha, novoStatus):
    sql = 'UPDATE senhas SET fk_status_senha = ? WHERE idSenha = ?'
    cursor = conexao.cursor()
    cursor.execute(sql, (novoStatus, idSenha))
    conexao.commit()
    cursor.close()


def obter_tipos_usuarios():
    try:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM tipo_usuarios')
        data = cursor.fetchall()
        cursor.close()
        tipos_usuarios = [{'value': row[0], 'label': row[1]} for row in data]
        return tipos_usuarios
    except Exception as e:
        print(f"Erro ao obter dados: {str(e)}")
        return None



def obter_tipoAtendimento():
    try:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM tipo_atendimento')
        data = cursor.fetchall()
        cursor.close()
        dados = [{'value': row[0], 'label': row[1]} for row in data]
        return dados

    except Exception as e:
        print(f"Erro ao obter dados da nova tabela: {str(e)}")
        return None



#servidor:


def loginServidor(cpf_servidor, senha_servidor):
    sql = 'Select * from servidores where cpf_servidor = %s and senha = %s' 
    cursor = conexao.cursor()
    cursor.execute(sql, (cpf_servidor, senha_servidor))
    servidor = cursor.fetchone()
    cursor.close()
    if servidor:
        return True
    else:
       return False

    
def servidorEsquecerSenha(cpf_servidor, nova_senha_servidor):
    try:
        sql = 'UPDATE servidores SET senha = %s WHERE cpf_servidor = %s'
        cursor = conexao.cursor()
        cursor.execute(sql, (nova_senha_servidor, cpf_servidor))
        conexao.commit()
        cursor.close()
        return True
    except Exception as e:
        print(f'Erro ao esquecer senha do servidor: {str(e)}')
        conexao.rollback() 
        return False



def cadastrarServidor(cpf_servidor, nome, senha):
    try:
        sql = 'INSERT INTO servidores (cpf_servidor, nome, senha) VALUES (%s, %s, %s)'
        cursor = conexao.cursor()
        cursor.execute(sql, (cpf_servidor, nome, senha))
        conexao.commit()
        cursor.close()
        return True  
    except Exception as e:
        print(f'Erro ao cadastrar servidor: {str(e)}')
        conexao.rollback()  
        return False  


#tabelas existentes no banco de dados: atendimento, senhas, servidores, tipo_atendimento, usuarios. ai eu acho q vai ter duas novas
