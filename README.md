# Generate PDF using python with Dajngo
# Technical requirements 
Using xhtml2pdf library to create and hundel pdf 
```python
 from xhtml2pdf import pisa
```
Then we use the response with content type 'application/pdf'
```python
  response = HttpResponse(content_type='application/pdf')
  response['Content-Disposition'] = 'attachment; filename="Report.pdf"'
```
and render this in html 
```python
    html = render_to_string(template_path, {'report': report})
    print (html)
    pisaStatus = pisa.CreatePDF(html, dest=response)
```
