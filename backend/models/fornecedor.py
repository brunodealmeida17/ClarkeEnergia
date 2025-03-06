from models import db

class FornecedorModel(db.Model):
    __tablename__ = "fornecedores"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    logo = db.Column(db.String(255))
    estado = db.Column(db.String(2), nullable=False)
    custo_por_kwh = db.Column(db.Float, nullable=False)
    limite_minimo_kwh = db.Column(db.Integer, nullable=False)
    num_clientes = db.Column(db.Integer, nullable=False)
    avaliacao_media = db.Column(db.Float, nullable=False)