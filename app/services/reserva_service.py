from app.models.reserva import Reserva
from database.db import db
from datetime import datetime

class ReservaService:
    @staticmethod
    def get_all_reservas():
        return Reserva.query.all()

    @staticmethod
    def get_reserva_by_id(id):
        return Reserva.query.get_or_404(id)

    @staticmethod
    def create_reserva(data):
        nueva_reserva = Reserva(
            id_propietario=data['id_propietario'],
            id_area=data['id_area'],
            fecha_reserva=datetime.strptime(data['fecha_reserva'], '%Y-%m-%d').date(),
            hora_inicio=datetime.strptime(data['hora_inicio'], '%H:%M').time(),
            hora_fin=datetime.strptime(data['hora_fin'], '%H:%M').time(),
            estado=data['estado']
        )
        db.session.add(nueva_reserva)
        db.session.commit()
        return nueva_reserva

    @staticmethod
    def update_reserva(reserva, data):
        reserva.id_propietario = data.get('id_propietario', reserva.id_propietario)
        reserva.id_area = data.get('id_area', reserva.id_area)
        reserva.fecha_reserva = datetime.strptime(data.get('fecha_reserva', reserva.fecha_reserva.isoformat()), '%Y-%m-%d').date()
        reserva.hora_inicio = datetime.strptime(data.get('hora_inicio', reserva.hora_inicio.isoformat()), '%H:%M').time()
        reserva.hora_fin = datetime.strptime(data.get('hora_fin', reserva.hora_fin.isoformat()), '%H:%M').time()
        reserva.estado = data.get('estado', reserva.estado)
        db.session.commit()
        return reserva

    @staticmethod
    def delete_reserva(reserva):
        db.session.delete(reserva)
        db.session.commit()