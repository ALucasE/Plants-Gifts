from celery import shared_task
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

from io import BytesIO
import weasyprint

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


@shared_task
def order_completed(order_id):
    """
    Tarea para enviar una notificación por correo electrónico cuando un pedido se
    haya pagado correctamente.
    """
    order = Order.objects.get(id=order_id)
    # create invoice e-mail
    subject = f'Jacaranda Plant & Gifts - Factura n. {order.id}'
    message = 'Adjunto encuentrara la factura de su compra.'
    email = EmailMessage(subject, message, 'admin@myshop.com', [order.email])
    # generate PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    # attach PDF file
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')
    # send e-mail
    email.send()