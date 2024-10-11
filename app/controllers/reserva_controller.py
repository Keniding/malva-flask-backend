from flask import jsonify, request
from app.services.reserva_service import ReservaService

class ReservaController:
    @staticmethod
    def get_reservas():
        reservas = ReservaService.get_all_reservas()
        return jsonify([reserva.to_dict() for reserva in reservas])

    @staticmethod
    def get_reserva(id):
        reserva = ReservaService.get_reserva_by_id(id)
        return jsonify(reserva.to_dict())

    @staticmethod
    def create_reserva():
        data = request.json
        nueva_reserva = ReservaService.create_reserva(data)
        return jsonify(nueva_reserva.to_dict()), 201

    @staticmethod
    def update_reserva(id):
        reserva = ReservaService.get_reserva_by_id(id)
        data = request.json
        reserva_actualizada = ReservaService.update_reserva(reserva, data)
        return jsonify(reserva_actualizada.to_dict())

    @staticmethod
    def delete_reserva(id):
        reserva = ReservaService.get_reserva_by_id(id)
        ReservaService.delete_reserva(reserva)
        return jsonify({'mensaje': 'Reserva eliminada exitosamente'})