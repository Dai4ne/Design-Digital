import sys
import os
import pymysql 
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

#Para o python encontrar as pastas corretamente
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

#Carrega as config do .env 
load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

app = Flask(__name__, 
            template_folder='../src/templates', 
            static_folder='../src/static')

#Função para pegar as config de conexão com o banco do .env
def conexao_db():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contatos', methods=['GET', 'POST'])
def contatos():
    if request.method == 'POST':
        #Informações que foram digitadas no form
        nome_form = request.form.get('nome')
        email_form = request.form.get('email')
        assunto_form = request.form.get('assunto')
        descricao_form = request.form.get('descricao')

        conexao = conexao_db()
        try:
            with conexao.cursor() as cursor:
                sql = '''
                    INSERT INTO contatos (nome, email, assunto, descricao) VALUES (%s, %s, %s, %s)
                '''
                cursor.execute(sql, (nome_form, email_form, assunto_form, descricao_form))

            conexao.commit() #Grava na AWS
            return redirect(url_for('contatos')) #Recarrega a página limpa
        
        except Exception as e:
            return f"Erro ao salvar as informações no banco {e}."
        finally:
            conexao.close()

    conexao = conexao_db()
    try:
        with conexao.cursor() as cursor:
            query1 = '''
                SELECT assunto, descricao FROM contatos
                ORDER BY id DESC
                LIMIT 7
            '''
            cursor.execute(query1)
            duvidas = cursor.fetchall()
    finally:
        conexao.close()

    return render_template('contatos.html', duvidas=duvidas)

@app.route('/quem')
def quem():
    return render_template('quem.html')