from .. import db

class Carrito(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    productoId=db.Column(db.Integer,db.ForeignKey('producto.id'),nullable=False)
    producto=db.relationship('Producto',back_populates='carrito',uselist=False)
    usuarioId=db.Column(db.Integer,db.ForeignKey('usuario.id'),nullable=False)
    usuario=db.relationship('Usuario',back_populates="carrito",uselist=False) 
    cantidad=db.Column(db.Integer,nullable=False)
    def __repr__(self):
        return f"{self.id}"
    
    def to_json(self):
        carrito_json={
            'id':self.id,
            'cantidad':self.cantidad,
            'producto':self.producto.to_json(),
            'usuario':self.usuario.to_json()
        }
        return carrito_json
    @staticmethod

    def from_json(carrito_json):
        id=carrito_json.get('id')
        cantidad=carrito_json.get('cantidad')
        productoId=carrito_json.get('productoId')
        usuarioId=carrito_json.get('usuarioId')

        return Carrito(
            id=id,
            cantidad=cantidad,
            productoId=productoId,
            usuarioId=usuarioId
        )


