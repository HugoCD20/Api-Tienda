from .. import db
from werkzeug.security import generate_password_hash, check_password_hash
class Usuario(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(45), nullable=False)
    email=db.Column(db.String(60), nullable=False,unique=True,index=True)
    role=db.Column(db.String(45), nullable=False,default="cliente")
    password=db.Column(db.String(100),nullable=False )
    direccion=db.relationship('direcciones', back_populates='usuario',cascade="all,delete-orphan")
    carrito=db.relationship('Carrito', back_populates='usuario',cascade="all,delete-orphan")
    
    @property
    def plain_password(self):
        raise AttributeError('Password can\'t be read')
    
    @plain_password.setter
    def plain_password(self,password):
        self.password=generate_password_hash(password)
    
    def validate_password(self,password):
        return check_password_hash(self.password,password)


    def __repr__(self):
        return f"{self.nombre}"
    
    def to_json(self):
        Usuario_json={
            'id':self.id,
            'nombre':self.nombre,
            'email':self.email,
            'role':self.role
        }
        return Usuario_json
    @staticmethod
    def from_json(Usuario_json):
        id=Usuario_json.get('id')
        nombre=Usuario_json.get('nombre')
        email=Usuario_json.get('email')
        role=Usuario_json.get('role')
        password=Usuario_json.get('password')
        return Usuario(
            id=id,
            nombre=nombre,
            email=email,
            role=role,
            plain_password=password
        )

