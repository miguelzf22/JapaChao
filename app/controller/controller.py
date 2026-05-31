from flask import Blueprint, render_template, url_for, request, redirect
from app.model.post import Post
from app.model.reply import Reply
from werkzeug.utils import secure_filename
import os


controller = Blueprint('lmao', __name__)

@controller.route('/')
def index():
    return render_template('index.html', lista=sorted(Post.consultar(), reverse=True), respostas=sorted(Reply.consultar()))

@controller.route('/enviar', methods=['POST', 'GET'])
def enviar():
    if request.method == 'POST':
        titulo = request.form.get('title')
        msg = request.form.get('msg')
        foto = request.files.get('foto')
        caminho_disco = os.path.join('app','static', 'uploads')
        if foto:
            filename = secure_filename(foto.filename)
            caminho = os.path.join(caminho_disco, filename)
            foto.save(caminho)
            Post.cadastrar(titulo, msg, f'uploads/{filename}')
        else:
            Post.cadastrar(titulo, msg, None)
        return redirect(url_for('lmao.index'))
    else:
        return redirect(url_for('lmao.index'))
    
@controller.route('/responder', methods=['POST', 'GET'])
def responder():
    if request.method == 'POST':
        postid = request.form.get('id-post')
        titulo = request.form.get('title')
        msg = request.form.get('msg')
        foto = request.files.get('foto')
        caminho_disco = os.path.join('app','static', 'uploads')
        if foto:
            filename = secure_filename(foto.filename)
            caminho = os.path.join(caminho_disco, filename)
            foto.save(caminho)
            Reply.cadastrar(postid, titulo, msg, f'uploads/{filename}')
        else:
            Reply.cadastrar(postid, titulo, msg, None)
        return redirect(url_for('lmao.index'))
    else:
        return render_template('reply.html')