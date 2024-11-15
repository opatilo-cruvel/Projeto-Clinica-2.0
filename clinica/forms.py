from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FileField, DateField, TimeField, SelectField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, length, Email, equal_to

class FormCriarContaPaciente(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(), length(1, 70)])
    idade = IntegerField('Idade',  validators=[DataRequired()])
    datanasc = DateField('Data de nascimento', validators=[DataRequired()])
    sexo = SelectField('Sexo', choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], validators=[DataRequired()])
    numero = StringField('Número',  validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired()])
    historico = FileField('Histórico médico (opcional)')
    email = StringField('E-mail', validators=[DataRequired(), Email(), length(5, 255)])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 20)])
    confirmacao = PasswordField('Confirmação da senha', validators=[DataRequired(), equal_to('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

class FormLoginPaciente(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')
 
class FormCriarContaMedico(FlaskForm):
    username = StringField('Nome de Usuário', validator=[DataRequired(), length(1, 70)])
    idade = IntegerField('Idade', validators=[DataRequired()])
    datanasc = DateField('Data de nascimento', validators=[DataRequired()])
    sexo = SelectField('Sexo', choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], validators=[DataRequired()])
    numero = StringField('Número', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired()])
    crm = StringField('CRM', validators=[DataRequired()]) # CRM + UF + 6 digitos
    especialidade = StringField('Especialidade', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 20)])
    confirmacao = PasswordField('Confirmação da senha', validators=[DataRequired(), equal_to('senha')])
    botao_submit_criar_med = SubmitField('Criar Conta')

class FormLoginMedico(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login_med = SubmitField('Fazer Login')

class FormLoginAdm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login_adm = SubmitField('Fazer Login')

class FormAgendaMedico(FlaskForm):
    data = DateField('Data de disponibilidade', validators=[DataRequired()])
    hora = TimeField('Hora de disponibilidade (referente ao dia)', validators=[DataRequired()])
    id_medico = IntegerField('Seu id médico', validators=[DataRequired()])
    status = StringField('Defina o Status')
    botao_submit_agenda_med = SubmitField('Salvar')

class FormAgendamentoPaciente(FlaskForm):
    motivo = TextAreaField('Motivo da consulta:', validators=[DataRequired()])
    botao_submit_agenda_paciente = SubmitField('Marcar')
