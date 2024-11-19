from clinica import database, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_paciente(id_paciente):
    return Paciente.query.get(int(id_paciente))




class Adm(database.Model, UserMixin):
    __tablename__ = 'adm'

    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(255), nullable=False)
    senha = database.Column(database.String(20), nullable=False)



class Paciente(database.Model, UserMixin):
    __tablename__ = 'paciente'

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(70), nullable=False)
    idade = database.Column(database.Integer, nullable=False)
    datanasc = database.Column(database.Date, nullable=False)
    sexo = database.Column(database.String(10), nullable=False)
    numero = database.Column(database.String(11), nullable=False, unique=True)
    cpf = database.Column(database.String(11), nullable=False, unique=True)
    ## historico =
    email = database.Column(database.String(150), nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    consultas = database.relationship('Consultas', backref='paciente', lazy=True)



class Medico(database.Model, UserMixin):
    __tablename__ = 'medico'

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(70), nullable=False)
    idade = database.Column(database.Integer, nullable=False)
    datanasc = database.Column(database.Date, nullable=False)
    sexo = database.Column(database.String(10), nullable=False)
    numero = database.Column(database.String(11), nullable=False)
    cpf = database.Column(database.String(11), nullable=False)
    crm = database.Column(database.String(13), nullable=False)
    especialidade = database.Column(database.String(), nullable=False)
    email = database.Column(database.String(255), nullable=False)
    senha = database.Column(database.String(20), nullable=False)
    consultas = database.relationship('Consultas', backref='medico', lazy=True)



class Consultas(database.Model):
    __tablename__ = 'concultas'

    id = database.Column(database.Integer, primary_key=True)
    data = database.Column(database.Date, nullable=False)
    hora = database.Column(database.Time, nullable=False)
    id_medico = database.Column(database.Integer, database.ForeignKey('medico.id'), nullable=False)
    status = database.Column(database.String(10), nullable=False, default='Livre')
    id_paciente = database.Column(database.Integer, database.ForeignKey('paciente.id'))
    motivo = database.Column(database.Text)
    
class Contato(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False)
    telefone = database.Column(database.String, nullable=False)
    assunto = database.Column(database.Text)
