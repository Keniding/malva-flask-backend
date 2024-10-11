from flask import Blueprint
from app.controllers.reserva_controller import ReservaController

reserva_bp = Blueprint('reserva', __name__)

reserva_bp.route('/', methods=['GET'])(ReservaController.get_reservas)
reserva_bp.route('/<int:id>', methods=['GET'])(ReservaController.get_reserva)
reserva_bp.route('/', methods=['POST'])(ReservaController.create_reserva)
reserva_bp.route('/<int:id>', methods=['PUT'])(ReservaController.update_reserva)
reserva_bp.route('/<int:id>', methods=['DELETE'])(ReservaController.delete_reserva)