from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import mysql.connector as sql
import random
import string
import json


# Create your views here.
def index(request):
    return render(request,'index.html')

def admit(request):
    cnx=sql.connect(host='127.0.0.1',user='root',password='Elango@7666',database='RI')
    cur=cnx.cursor()
    id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    s=str(datetime.now())
    s=s[:19]
    if request.method == 'GET':
        return render(request, 'patientad.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        ph = request.POST.get('ph')
        address = request.POST.get('address')
        cause = request.POST.get('cause')
        q=f"insert into patientadmit(id,name,age,ph,address,cause,date,amount)values('{str(id)}','{name}','{age}','{ph}','{address}','{cause}','{s}','{str(200)}');"
        cur.execute(q)
        q=f"insert into doctor(id,name)values('{str(id)}','{name}');"
        cur.execute(q)
        q=f"UPDATE doctor SET dname = '[]' WHERE id = '{str(id)}' AND dname IS NULL;"
        cur.execute(q)
        cnx.commit()
        
        cur.close()
        cnx.close()
        return HttpResponse(f"<center><h1>Patient admitted successfully</h1><br><h2>Patient ID : '{id}'</h2><br></center>")
def discharge(request):
    cnx=sql.connect(host='127.0.0.1',user='root',password='Elango@7666',database='RI')
    cur=cnx.cursor()
    if(request.method=='GET'):
        return render(request,'patientdischarge.html')
    if(request.method=='POST'):
        s=str(datetime.now())
        s=s[:19]
        id1=request.POST.get('id1')
        name1 = request.POST.get('name1')
        q= f"select * from patientadmit where id='{id1}' and name='{name1}';"
        cur.execute(q)
        l=[]
        for i in cur:
            l.append(i)
        if(l!=[]):
            q=f"insert into patientdischarge(id,name,age,ph,address,cause,admitdate,amount,dischargedate)values('{l[0][0]}','{l[0][1]}','{l[0][2]}','{l[0][3]}','{l[0][4]}','{l[0][5]}','{l[0][6]}','{l[0][7]}','{s}');"
            cur.execute(q)
            q=f"delete from patientadmit where id='{id1}' and name='{name1}';"
            cur.execute(q)
            q=f"delete from doctor where id='{id1}';"
            cur.execute(q)
            cnx.commit()
            cur.close()
            cur.close()
            return HttpResponse("<center><h1> Patient Discharged Successfully !!!</h1></center>")
        else:
            return HttpResponse("<center><h1> Invalid Details </h1></center>")
def bill(request):
    cnx=sql.connect(host='127.0.0.1',user='root',password='Elango@7666',database='RI')
    cur=cnx.cursor()
    if(request.method=='GET'):
        return render(request,'billing.html')
    if(request.method=='POST'):
        id2=request.POST.get('id2')
        name2=request.POST.get('name2')
        am2=request.POST.get('am2')
        
        q=f"select amount from patientadmit where id='{id2}' and name='{name2}';"
        cur.execute(q)
        l=[]
        for i in cur:
            l.append(i)
        if(l!=[]):
            print(l)
            t=str(int(l[0][0])+int(am2))
            q=f"update patientadmit set amount='{t}' where id='{id2}' and name='{name2}';"
            cur.execute(q)
            cnx.commit()
            cur.close()
            cnx.close()
            return HttpResponse("<center><h1> Bills Added Successfully !!!</h1></center>")
        else:
            return HttpResponse("<center><h1> Invalid Details</h1></center>")

def visit(request):
    cnx=sql.connect(host='127.0.0.1',user='root',password='Elango@7666',database='RI')
    cur=cnx.cursor()
    if(request.method=='GET'):
        return render(request,'doctor.html')
    if(request.method=='POST'):
        id3=request.POST.get('id3')
        name3=request.POST.get('name3')
        d3=request.POST.get('d3')
        am3=request.POST.get('am3')
        q=f"select * from doctor where id='{id3}';"
        cur.execute(q)
        l1=[]
        for i in cur:
            l1.append(i)
        if(l1!=[]):
            
            q = f"UPDATE doctor SET dname = JSON_ARRAY_APPEND(dname, '$', '{d3}') WHERE id = '{id3}';"
            cur.execute(q)
            cur.fetchall()
            q=f"select amount from patientadmit where id='{id3}' and name='{name3}';"
            cur.execute(q)
            l=[]
            for i in cur:
                l.append(i)
            t=str(int(l[0][0])+int(am3))
            q=f"update patientadmit set amount='{t}' where id='{id3}';"
            cur.execute(q)
            cnx.commit()
            cur.close()
            cnx.close()
            return HttpResponse("<center><h1> Successful Doctor Entry !!!</h1></center>")
        else:
            return HttpResponse("<center><h1> Invalid details</h1></center>")
    
def lss(request):
    if(request.method=='POST'):
        name0=request.POST.get('name0')
        print(name0)
        cnx=sql.connect(host='127.0.0.1',user='root',password='Elango@7666',db='ri')
        cur=cnx.cursor()
        q=f"select * from patientadmit where name='{name0}' or id='{name0}';"
        cur.execute(q)
        l=[]
        for i in cur:
            l.append(i)
        if(l!=[]):
            res={
                'rr':l,
            }
            return render(request,'lss.html',res)
        return HttpResponse("<center><h1>No Patients are available</h1></center>")
def lss1(request):
    cnx=sql.connect(host='127.0.0.1',user='root',password='Elango@7666',db='ri')
    cur=cnx.cursor()
    q=f"select * from patientadmit;"
    cur.execute(q)
    l=[]
    for i in cur:
        l.append(i)
    res={
        'rr':l,
    }
    return render(request,'lss1.html',res)
def lss3(request):
    cnx=sql.connect(host='127.0.0.1',user='root',password='Elango@7666',db='ri')
    cur=cnx.cursor()
    q=f"select * from patientdischarge;"
    cur.execute(q)
    l=[]
    for i in cur:
        l.append(i)
    res={
        'rr':l,
    }
    return render(request,'lss3.html',res)
def lss2(request):
    cnx=sql.connect(host='127.0.0.1',user='root',password='Elango@7666',db='ri')
    cur=cnx.cursor()
    q=f"select * from doctor;"
    cur.execute(q)
    l=[]
    for i in cur:
        l.append(i)
    res={
        'rr':l,
    }
    return render(request,'lss2.html',res)
    