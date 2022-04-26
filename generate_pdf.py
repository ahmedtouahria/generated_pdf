 from xhtml2pdf import pisa
 from django.http import HttpResponse
 from django.template.loader import get_template
 from django.template import Context 
 from rest_framework.views import APIView
 from .models import Model
from django.template.loader import render_to_string

def generate_pdf(request):
    report = Brand.objects.all()
    template_path = 'profile_brand_report.html'

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Report.pdf"'

    html = render_to_string(template_path, {'report': report})
    print (html)

    pisaStatus = pisa.CreatePDF(html, dest=response)

    return response
