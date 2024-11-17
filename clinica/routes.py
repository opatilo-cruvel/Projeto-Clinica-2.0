from flask import  render_template, url_for, request, flash, redirect
from clinica import app, database, bcrypt
from clinica.forms import FormCriarContaPaciente, FormLoginPaciente, FormLoginMedico, FormLoginAdm
from clinica.models import Paciente, Medico, Consultas
from flask_login import login_user

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
        paciente = Paciente.query.filter_by(email=form_login.email.data).first()
        if paciente and bcrypt.check_password_hash(paciente.senha, form_login.senha.data):
            login_user(paciente, remember=form_login.lembrar_dados.data)
            flash(f'Login feito com sucesso no e-mail: {form_login.email.data}.', 'alert-success')
            # redirecionar para a homepage
            return redirect(url_for('landingpage'))
        else:
            flash(f'falha no login. E-mail ou senha Incorretos', 'alert-danger')
    
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data).decode('utf-8')
        paciente = Paciente(username=form_criarconta.username.data, idade=form_criarconta.idade.data, datanasc=form_criarconta.datanasc.data, sexo=form_criarconta.sexo.data, numero=form_criarconta.numero.data, cpf=form_criarconta.cpf.data, email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(paciente)
        database.session.commit()
        
        flash(f'Conta criada com sucesso no e-mail: {form_criarconta.email.data}.', 'alert-success')
        return redirect(url_for('landingpage'))
    return render_template('loginusuario.html', form_login=form_login, form_criarconta=form_criarconta)

@app.route('/login-medico', methods=['GET', 'POST'])
def login_medico():
    form_login_med = FormLoginMedico()
    if form_login_med.validate_on_submit() and 'botao_submit_login_med' in request.form:
        flash(f'Login feito com sucesso no e-mail: {form_login_med.email.data}', 'alert-success')
        return redirect(url_for('landingpage'))
    return render_template('loginmed.html', form_login_med=form_login_med)
 
@app.route('/login-adm', methods=['GET', 'POST'])
def login_adm():
    form_login_adm = FormLoginAdm()
    if form_login_adm.validate_on_submit() and 'botao_submit_login_adm' in request.form:
        flash(f'Login feito com sucesso no e-mail: {form_login_adm.email.data}', 'alert-success')
        return redirect(url_for('landingpage'))

    return render_template('loginadm.html', form_login_adm=form_login_adm)