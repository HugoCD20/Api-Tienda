from .. import db

class Producto(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(100),nullable=False)
    precio=db.Column(db.Integer,nullable=False)
    imagen=db.Column(db.String(200),nullable=False)
    descripcion=db.Column(db.String(200),nullable=False)
    stock=db.Column(db.Integer,nullable=False)
    tipo=db.Column(db.String(100),nullable=False)
    carrito=db.relationship('Carrito',back_populates='producto',cascade='all,delete-orphan')

    def __repr__(self):
     return f"{self.nombre}"
    
    def to_json(self):
       
       Producto_json={
          'id':self.id,
          'nombre':self.nombre,
          'precio':self.precio,
          'imagen':self.imagen,
          'descripcion':self.descripcion,
          'stock':self.stock,
          'tipo':self.tipo
       }

       return Producto_json
    
    @staticmethod

    def from_json(Producto_json):
       
       id=Producto_json.get('id')
       nombre=Producto_json.get('nombre')
       precio=Producto_json.get('precio')
       imagen=Producto_json.get('imagen')
       descripcion=Producto_json.get('descripcion')
       stock=Producto_json.get('stock')
       tipo=Producto_json.get('tipo')

       return Producto(
          id=id,
          nombre=nombre,
          precio=precio,
          imagen=imagen,
          descripcion=descripcion,
          stock=stock,
          tipo=tipo
       )