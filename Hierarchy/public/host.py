from flask import *
from flask_jwt_extended import *
import json
import os
import random
import time
import hashlib
from generate_captcha import generate_math_problem, generate_captcha

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'Z%h^J-.3d+4we+hwW#|)'
app.config['SECRET_KEY'] = '(@|ntkYC&o8>dZ(N)Tdq'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
jwt = JWTManager(app)

MAX_DEPTH = 101

salt = [random.randint(0, 1000)] * 10

tree = []
for i in range(MAX_DEPTH):
    lay = [[0, hashlib.md5(str(time.time() * salt[j]).encode()).hexdigest()] for j in range(9)] + [[1, hashlib.md5(str(time.time() * salt[-1]).encode()).hexdigest()]]
    random.shuffle(lay)
    tree.append(lay)

captchas = {}

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@jwt_required()
def index():
    current_user = get_jwt_identity()
    while os.path.exists(".lock"):
        pass
    open(".lock", "w").close()
    depth = json.load(open("database.json"))[current_user][1]
    os.remove(".lock")
    back_list = []
    if depth > 0:
        back_list = ["back"]
    if depth == MAX_DEPTH:
        return render_template("flag.html"), 200
    captchas[current_user] = generate_math_problem()
    generate_captcha(captchas[current_user][0], f"static/captchas/{current_user}.jpg")
    return render_template("index.html", links=back_list + list(map(lambda x: x[1], tree[depth])), path=f"captchas/{current_user}.jpg"), 200

@app.route('/captcha', methods=['POST'])
@jwt_required()
def captcha():
    current_user = get_jwt_identity()
    cap = int(request.form.get('captcha'))
    link = request.form.get('link')
    if captchas[current_user][1] == cap:
        return redirect(url_for('goto', href=link))
    return redirect(url_for("index"))

@app.route('/goto/<href>', methods=['GET'])
@jwt_required()
def goto(href):
    current_user = get_jwt_identity()
    while os.path.exists(".lock"):
        pass
    open(".lock", "w").close()
    depth = json.load(open("database.json"))[current_user][1]
    os.remove(".lock")
    if href == "back" and depth > 0:
        while os.path.exists(".lock"):
            pass
        open(".lock", "w").close()
        data = json.load(open("database.json"))
        data[current_user][1] -= 1
        json.dump(data, open("database.json", "w"))
        os.remove(".lock")
        return redirect(url_for('index'))
    item = list(filter(lambda x: x[1] == href, tree[depth]))
    if item and item[0][0]:
        while os.path.exists(".lock"):
            pass
        open(".lock", "w").close()
        data = json.load(open("database.json"))
        data[current_user][1] += 1
        json.dump(data, open("database.json", "w"))
        os.remove(".lock")
        if data[current_user][1] == MAX_DEPTH - 1:
            render_template("flag.html"), 200
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('registration.html')
    else:
        login = request.form.get('login')
        password = request.form.get('password')
        while os.path.exists(".lock"):
            pass
        open(".lock", "w").close()
        users = json.load(open("database.json"))
        if login not in users:
            users[login] = [password, 0]
            json.dump(users, open("database.json", "w"))
            os.remove(".lock")
            return redirect(url_for('login')), 201
        else:
            os.remove(".lock")
            flash('Пользователь уже существует', 'error')
            return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        login = request.form.get('login')
        password = request.form.get('password')
        # Check if the user exists and the password is correct
        while os.path.exists(".lock"):
            pass
        open(".lock", "w").close()
        users = json.load(open("database.json"))
        os.remove(".lock")
        if login in users and users[login][0] == password:
            access_token = create_access_token(identity=login)
            resp = redirect(url_for("index"))
            set_access_cookies(resp, access_token)  # устанавливаем токен в куках
            return resp, 200
        else:
            flash('Неправильный логин или пароль', 'error')
            return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    resp = redirect(url_for('login'))
    unset_jwt_cookies(resp)
    return resp, 200


@jwt.expired_token_loader
@jwt.invalid_token_loader
@jwt.unauthorized_loader
def unauthorized(e, *a):
    return redirect(url_for('login'))


if __name__ == "__main__":
    if os.path.exists(".lock"):
        os.remove(".lock")
    if not os.path.exists("static/captchas"):
        os.mkdir("static/captchas")
    if not os.path.exists("database.json"):
        with open("database.json", "w") as f:
            f.write("{}")
    app.run(host="0.0.0.0", port=25555)
