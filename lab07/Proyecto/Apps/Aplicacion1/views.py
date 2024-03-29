from django.http import HttpResponse
from django.views.generic import View
from django.template import engines, loader
from .models import render_to_pdf
import datetime

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template_engine = engines['django']
        template = template_engine.get_template('invoice.html')

        context = {
            "invoice_id": "Prueba: creando un pdf",
            "customer_name": "Jhon Cooper",
            "amount": 1399.99,
            "today": datetime.datetime.now()
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return "Not found"
