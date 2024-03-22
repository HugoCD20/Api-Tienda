from flask_restful import Resource
from flask import request,jsonify
from .. import db
from main.models import direccionesModel
from main.auth.decorator import role_requiered
from flask_jwt_extended import get_jwt_identity
class direccion(Resource):
    @role_requiered(roles=["admin","cliente"])
    def get(self,id):
        direccion=db.session.query(direccionesModel).get_or_404(id)
        current_user=get_jwt_identity()
        if current_user['usuarioId']==direccion.usuarioId or current_user["role"]=="admin":
            try:
                return direccion.to_json()
            except:
                return 'direccion no encontrada', 404
        else:
            return 'Unauthorized',401
        
    @role_requiered(roles=["admin","cliente"])
    def delete(self,id):
        direccion=db.session.query(direccionesModel).get_or_404(id)
        current_user=get_jwt_identity()
        if current_user['usuarioId']==direccion.usuarioId or current_user['role']=="admin":
            try:
                db.session.delete(direccion)
                db.session.commit()
                return "Eliminación exitosa",201
            except:
                return "Ha ocurrido un error",401
        else:
            return 'Unauthorized',401
    
    @role_requiered(roles=["admin","cliente"])
    def put(self,id):
        direccion=db.session.query(direccionesModel).get_or_404(id)
        current_user=get_jwt_identity()
        if current_user['usuarioId']==direccion.usuarioId or current_user['role']=="admin":
            data=request.get_json().items()
            for key,value in data:
                setattr(direccion,key,value)
            try:
                db.session.add(direccion)
                db.session.commit()
                return direccion.to_json(), 201
            except:
                return "Ha sucedido un error",401
        else:
            return 'Unauthorized',401

        
class direcciones(Resource):
    
    @role_requiered(roles=["admin"])
    def get(self):
        page=1
        per_page=5
        direcciones=db.session.query(direccionesModel)
        try:
            if request.get_json():
                filters=request.get_json().items()
                for key,value in filters:
                    if key == 'page':
                        page=int(value)
                    elif key =='per_page':
                        per_page=int(value)
        except:
            pass
        direcciones=direcciones.paginate(page,per_page,True,5)
        return jsonify({
            "direcciones":[direccion.to_json() for direccion in direcciones.items],
            "total":direcciones.total,
            "pages":direcciones.pages,
            "page":page
        })
    @role_requiered(roles=["admin","cliente"])
    def post(self):
        direccion=direccionesModel.from_json(request.get_json())
        db.session.add(direccion)
        db.session.commit()

        return direccion.to_json(),201