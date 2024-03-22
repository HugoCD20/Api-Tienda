from flask_restful import Resource
from flask import request,jsonify
from .. import db
from main.models import CarritoModel
from main.auth.decorator import role_requiered
from flask_jwt_extended import get_jwt_identity
class carrito(Resource):
    @role_requiered(roles=["cliente"])
    def get(self,id):
        carrito=db.session.query(CarritoModel).get_or_404(id)
        current_user=get_jwt_identity()
        try:
            if carrito.usuarioId==current_user["usuarioId"] and current_user['role']=="cliente":
                return carrito.to_json()
            else:
                return 'Unauthorized',401
        except:
            return 'No se ha encontrado un producto',404
        
    def put(self,id):
        carrito=db.session.query(CarritoModel).get_or_404(id)
        data=request.get_json().items()
        for key,values in data:
            setattr(carrito,key,values)
        try:
            db.session.add(carrito)
            db.session.commit()
            return carrito.to_json()
        except:
            return 'request not found',404
    
    def delete(self,id):
        carrito=db.session.query(CarritoModel).get_or_404(id)
        try:
            db.session.delete(carrito)
            db.session.commit()
            return 'Eliminacion exitosa',201
        except:
            return 'not found',404
        
        
class carritos(Resource):
    @role_requiered(roles=["admin"])
    def get(self):
        page=1
        per_page=1
        carrito=db.session.query(CarritoModel)
        try:
            if request.get_json():
                filters=request.get_json().items()
                for key,value in filters:
                    if key == 'page':
                        page=int(value)
                    elif key == 'per_page':
                        per_page=int(value)
        except:
            pass
        carrito=carrito.paginate(page,per_page,True,5)
        return jsonify({
            'Carrito':[carrito.to_json() for carro in carrito.items],
            'total':carrito.total,
            'pages':carrito.pages,
            'page':page
        })
    @role_requiered(roles=["cliente"])
    def post(self):
        carrito=CarritoModel.from_json(request.get_json())
        db.session.add(carrito)
        db.session.commit()
        return carrito.to_json()