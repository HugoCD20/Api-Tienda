from .. import db

class direcciones(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    calle=db.Column(db.String(200),nullable=False)
    colonia=db.Column(db.String(200),nullable=False)
    codigoPostal=db.Column(db.Integer,nullable=False)
    estado=db.Column(db.String(200),nullable=False)
    numeroExterior=db.Column(db.Integer,nullable=False)
    numeroTelefonico=db.Column(db.String(10),nullable=False)
    usuarioId=db.Column(db.Integer,db.ForeignKey('usuario.id'),nullable=False)
    usuario=db.relationship('Usuario',back_populates="direccion",uselist=False) 

    def __repr__(self):
            return f"{self.usuarioId}"
     
    def to_json(self):
      direccion_json = {
            'id': self.id,
            'calle': self.calle,
            'colonia':self.colonia,
            'codigoPostal':self.codigoPostal,
            'estado':self.estado,
            'numeroExterior':self.numeroExterior,
            'numeroTelefonico':self.numeroTelefonico,
            'usuario': self.usuario.to_json()
      }

      return direccion_json

    
    @staticmethod
    def from_json(direccion_json):
          id=direccion_json.get('id')
          calle=direccion_json.get('calle')
          colonia=direccion_json.get('colonia')
          codigoPostal=direccion_json.get('codigoPostal')
          estado=direccion_json.get('estado')
          numeroExterior=direccion_json.get('numeroExterior')
          numeroTelefonico=direccion_json.get('numeroTelefonico')
          usuarioId=direccion_json.get('usuarioId')
          return direcciones(
                id=id,
                calle=calle,
                colonia=colonia,
                codigoPostal=codigoPostal,
                estado=estado,
                numeroExterior=numeroExterior,
                numeroTelefonico=numeroTelefonico,
                usuarioId=usuarioId
          )