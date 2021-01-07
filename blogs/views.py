from django.shortcuts import render,HttpResponse
from .models import Blog
from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO
# Create your views here.

def index(request):
    context = {}
    blogs = Blog.objects.all()
    context['blogs'] = blogs
    return render(request,'index.html',context)

def get_PDF_page(request):
    data = {}
    blogs = Blog.objects.all()
    data['blogs'] = blogs
    template = get_template('pdf_page.html')
    data_p = template.render(data)
    response = BytesIO()

    pdfPage = pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")), response)
    if not pdfPage.err:
        return HttpResponse(response.getvalue(), content_type="application/pdf")
    else:
        return HttpResponse("Error Generating PDF")

