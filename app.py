from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id': 0,
     'nome': 'Cleiton', 
     'habilidades': ['python', 'csharp']
     },
    {'id': 1,
     'nome': 'Vagner',
     'habilidades': ['java', 'cobol']
    }
]
# devolve um desenvolvedor pelo ID
@app.route('/dev/<int:id>', methods=['GET'])
def get_desenvolvedor(id):
    if request.method =='GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe.'
            response = {'status': 'ERRO', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'ERRO', 'mensagem': mensagem}
        return jsonify(response)
    
# altera um desenvolvedor pelo ID
@app.route('/dev/<int:id>', methods=['PUT'])
def put_altera_desenvolvedor(id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

# deleta um desenvolvedor pelo ID
@app.route('/dev/<int:id>', methods=['DELETE'])
def delete_desenvolvedor(id):
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído'})
    
# insere um desenvolvedor pelo ID
@app.route('/dev/', methods=['POST'])
def post_desenvoledor():
    dados = json.loads(request.data)
    dados['id'] = len(desenvolvedores)
    desenvolvedores.append(dados)
    return jsonify({'status': 'sucesso', 'mensagem': f'Registro incluído id = {len(desenvolvedores) - 1}'})

# lista todos os desenvolvedores
@app.route('/dev/', methods=['GET'])
def listar_desenvolvedores():
    return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)