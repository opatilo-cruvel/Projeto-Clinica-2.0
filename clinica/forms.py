from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FileField, DateField, TimeField, SelectField, BooleanField, TextAreaField, TelField
from wtforms.validators import DataRequired, length, Email, equal_to, ValidationError, Regexp
from clinica.models import Paciente, Medico

class FormCriarContaPaciente(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(), length(1, 70)])
    idade = IntegerField('Idade',  validators=[DataRequired()])
    datanasc = DateField('Data de nascimento', validators=[DataRequired()])
    sexo = SelectField('Sexo', choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], validators=[DataRequired()])
    numero = StringField('Número',  validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email(), length(5, 255)])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 20)])
    confirmacao = PasswordField('Confirmação da senha', validators=[DataRequired(), equal_to('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_numero(self, numero):
        paciente = Paciente.query.filter_by(numero=numero.data).first()
        if paciente:
            raise ValidationError('Número de celular já cadastrado. Cadastre-se com outro número ou faça login para continuar')

    def validate_cpf(self, cpf):
        paciente = Paciente.query.filter_by(cpf=cpf.data).first()
        if paciente:
            raise ValidationError('CPF já cadastrado. Cadastre-se com outro CPF ou faça login para continuar')

    def validate_email(self, email):
        paciente = Paciente.query.filter_by(email=email.data).first()
        if paciente:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar')
        


class FormLoginPaciente(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')
 

class FormCriarContaMedico(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(), length(1, 70)])
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

    def validate_numero(self, numero):
        medico = Medico.query.filter_by(numero=numero.data).first()
        if medico:
            raise ValidationError('Número de celular já cadastrado. Cadastre-se com outro número ou faça login para continuar')

    def validate_crm(self, crm):
        medico = Medico.query.filter_by(crm=crm.data).first()
        if medico:
            raise ValidationError('CRM já cadastrado. Cadastre-se com outro CRM ou faça login para continuar')

    def validate_cpf(self, cpf):
        medico = Medico.query.filter_by(cpf=cpf.data).first()
        if medico:
            raise ValidationError('CPF já cadastrado. Cadastre-se com outro CPF ou faça login para continuar')

    def validate_email(self, email):
        medico = Medico.query.filter_by(email=email.data).first()
        if medico:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar')

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

class FormCriarContaAdm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 20)])
    confirmacao = PasswordField('Confirmação da senha', validators=[DataRequired(), equal_to('senha')])
    botao_submit_criarconta_adm = SubmitField('Fazer Login')


class FormAgendaMedico(FlaskForm):
    data = DateField('Data de disponibilidade', validators=[DataRequired()])
    hora = TimeField('Hora de disponibilidade (referente ao dia)', validators=[DataRequired()])
    id_medico = IntegerField('Seu id médico', validators=[DataRequired()])
    status = StringField('Defina o Status')
    botao_submit_agenda_med = SubmitField('Salvar')


class FormAgendamentoPaciente(FlaskForm):
    motivo = TextAreaField('Motivo da consulta:', validators=[DataRequired()])
    botao_submit_agenda_paciente = SubmitField('Marcar')

class FormFaleConosco(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), length(1,40)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    telefone = StringField('Telefone', validators=[DataRequired(), length(10, 15,) , Regexp(r'^\d+$', message="O telefone deve conter apenas números.")])
    assunto = StringField('Assunto', validators=[DataRequired(), length(1, 400)])
    botao_submit_contato = SubmitField ('Enviar')