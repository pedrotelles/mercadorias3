# encoding: utf-8

from mercadorias3 import db
class ProcessoSeletivo(db.Model):
    __tablename__ = 'ProcessoSeletivo'
    idPS = db.Column(db.Integer, primary_key=True)
    codMer = db.Column(db.Integer, nullable=False)
    tipoMer = db.Column(db.String(100), nullable=False)
    nomeMer = db.Column(db.String(100), nullable = False)
    qtdMer = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    tNegocio = db.Column(db.Integer, nullable=False, server_default=str("'0'"))

    def toJSON(self):
        return {"Mercadoria": {'codMer': self.codMer,
                         'tipoMer': self.tipoMer,
                         'nomeMer': self.nomeMer,
                         'qtdMer': self.qtdMer,
                         'preco': '{0:.2f}'.format(self.preco).replace('.',','),
                         'tNegocio': self.tNegocio}}