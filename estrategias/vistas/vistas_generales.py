from xhtml2pdf import pisa
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404, redirect
from estrategias.models import Estrategia
from io import BytesIO
from django.http import HttpResponse
from django.contrib import messages

def estrategia_pdf(request, estra_id):
    if request.user.is_authenticated:
        estrategia = get_object_or_404(Estrategia, id=estra_id)

        # Renderizar HTML
        html = render_to_string("estrategia_pdf.html", {'estrategia': estrategia})

        # Generar PDF desde HTML
        buffer = BytesIO()
        pisa_status = pisa.CreatePDF(html, dest=buffer)
        buffer.seek(0)

        if pisa_status.err:
            return HttpResponse("Error al generar el PDF", status=500)

        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{estrategia.nombre}_{estrategia.id}.pdf"'
        return response
    else:
        messages.error(request, "No estás autenticado.")
        return redirect("login")
