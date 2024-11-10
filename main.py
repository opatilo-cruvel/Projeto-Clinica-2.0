from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormCriarContaPaciente, FormLoginPaciente


app = Flask(__name__)

app.config['SECRET_KEY'] = 'e130616980c3ea8d297d37ca384b9260'


@app.route('/')
def landingpage():
    return render_template('landingpage.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/sobre-nos')
def sobrenos():
    return render_template('sobre.html')

@app.route('/login-usuario', methods=['GET', 'POST'])
def login_usuario():
    form_login = FormLoginPaciente()
    form_criarconta = FormCriarContaPaciente()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        # Exibir msg de login bem sucedido
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}.', 'alert-success')
        # redirecionar para a homepage
        return redirect(url_for('landingpage'))
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        # Criou conta com sucesso
        flash(f'Conta criada com sucesso no e-mail: {form_criarconta.email.data}.', 'alert-success')
        return redirect(url_for('landingpage'))
    return render_template('loginusuario.html', form_login=form_login, form_criarconta=form_criarconta)

@app.route('/login-medico', methods=['GET', 'POST'])
def login_medico():
    return render_template('loginmed.html')



if __name__ == ('__main__'):
    app.run(debug=True)
 
