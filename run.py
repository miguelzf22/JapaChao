from app import createApp
from app.model.post import Post
from app.model.reply import Reply

app = createApp()

if __name__ == '__main__':
    Post.criartabela()
    Reply.criartabela()
    app.run(debug=True, host='0.0.0.0')