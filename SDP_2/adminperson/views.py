from django.shortcuts import render
from pharmacy.models import MedicineOrder, Pharmacy
from doctor.models import Consult, Doctor
from customer.models import Patient, Appointment

# Create your views here.
def AdminHomePage(request):
    medor=MedicineOrder.objects.all()
    data1=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in medor:
        my_mon = i.date.strftime("%m")
        p=int(my_mon)
        data1[p-1]+=1
    data2=[0,0,0,0,0,0,0,0,0,0,0,0]
    con=Consult.objects.all()
    for i in con:
        my_mon = i.date.strftime("%m")
        p=int(my_mon)
        data2[p-1]+=1

    labels = ['Patients','Doctors','Pharmacist']
    data = []

    c=0
    pat=Patient.objects.all()
    for i in pat:
        c=c+1
    data.append(c)
    c=0
    doc=Doctor.objects.filter(assign=True)
    for d in doc:
        c+=1
    data.append(c)
    c=0
    pha=Pharmacy.objects.filter(assign=True)
    for p in pha:
        c+=1
    data.append(c)

    flabels = ['Patients','Doctors','Pharmacist']
    fdata = []
    c=0
    pat=Patient.objects.all()
    for i in pat:
        c=c+1
    fdata.append(c)
    c=0
    doc=Doctor.objects.filter(assign=True)
    for d in doc:
        c+=1
    fdata.append(c)
    c=0
    pha=Pharmacy.objects.filter(assign=True)
    for p in pha:
        c+=1
    fdata.append(c)
    
    return render(request,'adminhome.html',{'data1':data1,'data2':data2,'labels': labels,'data3': data,'order_count':sum(data1),'con_count':sum(data2),'flabel':flabels,'fdata':fdata})

def pie_chart(request):
    labels = ['Patients','Doctors','Pharmacist']
    data = []
    c=0
    pat=Patient.objects.all()
    for i in pat:
        c=c+1
    data.append(c)
    c=0
    doc=Doctor.objects.filter(assign=True)
    for d in doc:
        c+=1
    data.append(c)
    c=0
    pha=Pharmacy.objects.filter(assign=True)
    for p in pha:
        c+=1
    data.append(c)
    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })