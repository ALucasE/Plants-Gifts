from celery import shared_task
from django.core.mail import send_mail

from .models import Order


@shared_task
def order_created(order_id):
    """
    Tarea para enviar una notificación por correo electrónico cuando se crea correctamente un pedido.
    """
    order = Order.objects.get(id=order_id)
    subject = f"Orden nr. {order.id}"
    message = f"""Estimado/a {order.first_name},
    
    Has realizado un pedido con éxito. Su ID de pedido es {order.id}.
    
    Para realizar el pago realiza una transferencia de: ${order.get_total_cost()} a la sigueinte cuenta:
    CBU: 2850 1145 4008 5594 677 678
    Alias:jacaranda.plants.gifts
    Numero de cuenta:41140 95584 07761
    En la referencia de la tranferencia agregue el numero de orden: {order.id}
    """
    mail_sent = send_mail(subject, message, "admin@myshop.com", [order.email])
    return mail_sent
