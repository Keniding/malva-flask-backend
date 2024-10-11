from database.db import db
from datetime import datetime

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id_reserva = db.Column(db.Integer, primary_key=True)
    id_propietario = db.Column(db.Integer)
    id_area = db.Column(db.Integer)
    fecha_reserva = db.Column(db.Date)
    hora_inicio = db.Column(db.Time)
    hora_fin = db.Column(db.Time)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.String(50))

    def to_dict(self):
        return {
            'id_reserva': self.id_reserva,
            'id_propietario': self.id_propietario,
            'id_area': self.id_area,
            'fecha_reserva': self.fecha_reserva.isoformat(),
            'hora_inicio': self.hora_inicio.isoformat(),
            'hora_fin': self.hora_fin.isoformat(),
            'fecha_creacion': self.fecha_creacion.isoformat(),
            'estado': self.estado
        }