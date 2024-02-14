from flask import Flask, request, jsonify
from controller import gerarSenhaNormal,gerarSenhaPreferencial, obter_tipoAtendimento, obter_tipos_usuarios,cadastrarNaTabelaSenha, cadastrarUsuario, listarSenhas ,cadastrarAtendimento, listarAtendimento, cadastrarNaTabelaSenha, listarAtendimento, loginServidor, servidorEsquecerSenha, cadastrarServidor
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

#página cadastro-usuario

@app.route('/cadastro', methods=['POST'])
def cadastroUsuario():
    try:
        requisicao = request.get_json()

        if requisicao is None:
            return jsonify({"error": "Sem valor"}), 400

        nome = requisicao.get('nomeUsuario')
        if nome is None:
            return jsonify({"error": "Sem valor para nome"}), 400

        cpf_usuario = requisicao.get('cpf')
        if cpf_usuario is None:
            return jsonify({"error": "Sem valor para CPF"}), 400

        assunto = requisicao.get('assunto')
        if assunto is None:
            return jsonify({"error": "Sem valor para assunto"}), 400
            #comunidade    
        comunidade = requisicao.get('comunidade')
        if comunidade is None:
            return jsonify({"error": "Sem valor para comunidade"}), 400

        preferencia = requisicao.get('preferencia')
        if preferencia is None:
            return jsonify({"error": "Sem valor para preferencia"}), 400

        
        if preferencia == 'preferenciasim':
            senha = gerarSenhaPreferencial()
        else:
            senha = gerarSenhaNormal()

        cadastrarUsuario(cpf_usuario, nome, comunidade)
        cadastrarNaTabelaSenha(senha)
        cadastrarAtendimento(cpf_usuario, senha, 1)
        
        return jsonify({'senha': senha})

    except Exception as e:
        print(f"Erro: {str(e)}")
        return jsonify({'mensagem': f'Erro: {str(e)}'}), 400  





@app.route('/chamar-senha', methods =['GET'])
def chamarSenha():
    try:
        senha = listarSenhas()
        return jsonify({'Senha': senha})
    except Exception as e:    
        return jsonify({'mensagem': 'erro'})
        if senha:
            return jsonify({'Senha': senha[0]})
        else:
            return jsonify({'mensagem': 'Não há senhas disponíveis'})
    
    


@app.route('/listar-atendimentos', methods =['GET'])
def listarAtendimentos():
    try:
        atendimentos = listarAtendimento()
        return jsonify({'Atendimentos': atendimentos})
    except Exception as e:
        return jsonify({'mensagem': 'erro'})   

#referentes ao servidor:

@app.route('/cadastro-servidor', methods=['POST'])
def cadastroServidor():
    try:
        requisicao = request.get_json()
        cpf_servidor = requisicao.get('cpf_servidor')
        nome = requisicao.get('nome_servidor')
        senha_servidor = requisicao.get('senha_servidor')

        if cadastrarServidor(cpf_servidor, nome, senha_servidor):
            return jsonify ({'mensagem':'Cadastro bem-sucedido.'})
        else:
            return jsonify({'mensagem':'Erro ao tentar cadastrar. Tente novamente.'})

    except Exception as e:
        return jsonify({'mensagem': f'Erro ao processar o cadastro do servidor: {str(e)}'})

@app.route('/login-servidor', methods = ['POST'])
def login_servidor():
    try:
        requisicao = request.get_json()
        cpf_servidor = requisicao.get('cpf_servidor')
        senha_servidor = requisicao.get('senha_servidor')

        if loginServidor(cpf_servidor, senha_servidor):
            return jsonify({'mensagem': 'Login do servidor bem-sucedido'})
        else:
            return jsonify({'mensagem': 'Login do servidor falhou'})

    except Exception as e:
        return jsonify({'mensagem': f'Erro ao processar o login do servidor: {str(e)}'})



@app.route('/esqueceu-senha', methods=['PUT'])
def esqueceu_senha():
    try:
        requisicao = request.get_json()
        cpf_servidor = requisicao.get('cpf_servidor')
        senha_servidor = requisicao.get('senha_servidor')
        if servidorEsquecerSenha(cpf_servidor, senha_servidor):
            return jsonify({'mensagem': 'Sua senha foi alterada!'})
        else:
            return jsonify({'mensagem':'Erro ao tentar alterar sua senha.'})
    except Exception as e:
        return jsonify({'mensagem': f'Erro ao processar o login do servidor: {str(e)}'})



#retornando dados do banco de dados:

@app.route('/tipo-usuario', methods=['GET'])
def dropdown_usuario():
    tipos_usuarios = obter_tipos_usuarios()

    if tipos_usuarios is not None:
        return jsonify(tipos_usuarios)
    else:
        return jsonify({'error': 'Erro ao obter dados'}), 500



@app.route('/obter-atendimentos', methods=['GET'])
def rota_dados_nova_tabela():
    atendimentos = obter_tipoAtendimento()

    if atendimentos is not None:
        return jsonify(atendimentos)
    else:
        return jsonify({'error': 'Erro ao obter atendimentos'}), 500



if __name__ == "__main__":
    app.run()



