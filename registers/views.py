from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin
from django.forms import widgets
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . models import Register

#some importations to use with reportlab in generate pdf file in django
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter,C7,C11
########


class RegisterListView(LoginRequiredMixin, ListView):
    model = Register
    template_name = "registers/register_list.html"
    context = Register.objects.all()


class RegisterCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Register
    fields = "__all__"
    success_message = "New record successfully added."

    def get_form(self):
        """add date picker in forms"""
        form = super(RegisterCreateView, self).get_form()
        form.fields["date"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        return form


class RegisterUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Register
    fields = "__all__"
    success_message = "Record successfully updated."

    def get_form(self):
        """add date and text picker in forms"""
        form = super(RegisterUpdateView, self).get_form()
        form.fields["date"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        return form
        


class RegisterDetailView(LoginRequiredMixin, DetailView):
    model = Register
    template_name = "registers/register_detail.html"

    def get_context_data(self, **kwargs):
        context = super(RegisterDetailView, self).get_context_data(**kwargs)
        return context

    

class RegisterDeleteView(LoginRequiredMixin, DeleteView):
    model = Register
    success_url = reverse_lazy("register-list")



def pdffile(request):
    buffer = io.BytesIO()

    c = canvas.Canvas(buffer, pagesize=letter)

    DocumentTitle = 'New invoice generator'

    c.setTitle(DocumentTitle)

    c.translate(inch,inch)
    # define a large font
    c.setFont("Helvetica", 14)
    # choose some colors
    c.setStrokeColorRGB(0.1,0.8,0.1)
    c.setFillColorRGB(0,0,1) # font colour
    #c.drawImage('C:\Users\new_user\Pictures\Screenshots\Capture d’écran (1).png',-0.8*inch,9.3*inch)
    c.drawString(0, 9*inch, "City Name : ")
    c.drawString(0, 8.7*inch, "Address : ")
    c.setFillColorRGB(0,0,0) # font colour
    #c.line(0,8.6*inch,6.8*inch,8.6*inch)
    c.drawString(4.9*inch,9.5*inch,'Invoice No :# 854')
    from  datetime import date
    dt = date.today().strftime('%d-%b-%Y')
    c.drawString(5.6*inch,9.3*inch,dt)
    c.setFont("Helvetica", 18)
    c.drawString(3*inch,9.6*inch,'Register List')
    c.setFillColorRGB(1,0,0) # font colour
    c.setFont("Times-Bold", 30)
    c.drawString(4.3*inch,8.7*inch,'Invoice')
    c.rotate(45) # rotate by 45 degree 
    c.setFillColorCMYK(0,0,0,0.08) # font colour CYAN, MAGENTA, YELLOW and BLACK
    c.setFont("Helvetica", 80) # font style and size
    c.drawString(1.8*inch, 0.4*inch, "SAUVEGARDE") # String written 
    c.rotate(-45) # restore the rotation #good to know
    c.setFillColorRGB(0,0,0) # font colour
    c.setFont("Times-Roman", 22)
    c.drawString(0, 8.3*inch,'Name')
    c.drawString(2*inch, 8.3*inch, 'Rent type')
    c.drawString(3.7*inch,8.3*inch,'Email')
    c.drawString(5.1*inch,8.3*inch,'Phone')
    c.drawString(6.2*inch,8.3*inch,'Start date')
    registers = Register.objects.all()
    #line_y = 7.9
    for register in registers:
        c.setFont("Helvetica", 9)
        c.drawString(0, 8*inch, f'{register.full_name}')
        c.drawString(2*inch, 8*inch, f'{register.rent_type}')
        c.drawString(3.6*inch, 8*inch, f'{register.email}')
        c.drawString(5.1*inch, 8*inch, f'{register.phone}')
        c.drawString(6.2*inch, 8*inch, f'{register.date}')




    c.setStrokeColorCMYK(0,0,0,1) # vertical line colour
    c.line(1.6*inch,8.3*inch,1.6*inch,0*inch)# first vertical line
    c.line(3.5*inch,8.3*inch,3.5*inch,0*inch)# second vertical line
    c.line(4.9*inch,8.3*inch,4.9*inch,0*inch)# third vertical line
    c.line(6.1*inch,8.3*inch,6.1*inch,0*inch)# fourth vertical line
    c.line(0.01*inch,0*inch,8*inch,0*inch)# horizontal line total
    c.setFont("Helvetica", 8) # font size
    c.setFillColorRGB(1,0,0) # font colour
    c.drawString(0, -0.1*inch, u"\u00A9"+" Light_35") 
        
    c.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='register.pdf')

        #create a file like buffer to receive PDF data
        #buffer = io.BytesIO()

        #create the PDF object, using the buffer as its "file"
        #p = canvas.Canvas(buffer, pagesize=letter, bottomup=0)

        #Draw things on the PDF. here's where the pdf generation happens.
        #see the reportlab documentation for the full list of functionnality.
        
    

        #Create a text object
        #textob = p.beginText()
        #textob.setTextOrigin(inch, inch)
        #textob.setFont("Helvetica", 14)

        #Designate the model
        #registers = Register.objects.all()
        #lines = []
        #for register in registers:
            #lines.append(f'{register.full_name}')
            #lines.append(f'{register.rent_type}')
            #lines.append(f'{register.email}')
            #lines.append(f'{register.phone}')
            #lines.append(f'{register.address}')
            #lines.append(f'{register.date}')
            #lines.append(f'{register.amount}')
            #lines.append('=================================') """

        #Loop
        #for line in lines:
            #textob.textLine(line)

        #Finish up
        #p.setTitle("Register's pdf")
        #p.drawCentredString(270, 30, "REGISTRATION RECORD")
        #p.drawText(textob)


        #close the pdf object cleanly, and we're done
        #p.showPage()
        #p.save()

        #FileResponse sets the content-Disposition header so that browsers present the option to save the files.
        #buffer.seek(0)
        #return FileResponse(buffer, as_attachment=True, filename='register.pdf') """