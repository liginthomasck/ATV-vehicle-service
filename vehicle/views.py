from django.shortcuts import render
from django.shortcuts import render,redirect,render_to_response,HttpResponseRedirect
from django.http import HttpResponse
from django.db import connection
from vechicle.forms import vForm
from vechicle.models import vitem

from  datetime import date 
from datetime import datetime
today=date.today()
import datetime
today_date = datetime.date.today()
new_today_date = today_date.strftime("%Y-%m-%d")

def  login(request):
	return  render(request ,'index.html')
def logout(request):
	try:
		del request.session['uid']
		del request.session['utype']
	except:
		pass
	return HttpResponse("<script>alert('you are loged out');window.location='/home/';</script>")
def searchlogin(request):
	cursor=connection.cursor()
	p=request.GET['t1']
	q=request.GET['t2']
	sql2="select * from login where uname='%s' and upass='%s'  " %(p,q)
	cursor.execute(sql2)
	result=cursor.fetchall()
	if 	(cursor.rowcount) > 0:
		sql3 = "select * from login  where uname='%s' and upass='%s' " % (p, q)
		cursor.execute(sql3)
		result1 = cursor.fetchall()
		for row1 in result1:
			request.session['uid'] = row1[0]
			request.session['username'] = row1[1]
			request.session['upass'] = row1[2]
			request.session['utype'] =row1[3]
		if(request.session['utype']=='admin'):
			return render(request ,'adminhome.html') 
		elif(request.session['utype']=='user'):
			return render(request ,'userhome.html')
		elif(request.session['utype']=='mechanics'):
			return render(request ,'mechanicshome.html') 
	else:
		html="<script>alert('invalid password and username ');window.location='/login/';</script>"
		return HttpResponse(html)
def userinsert(request): 
	cursor=connection.cursor()
	n=request.GET["t1"];
	m=request.GET["t2"];
	e=request.GET["t3"];
	p=request.GET["t4"];
	cp=request.GET["t5"];
	
	sql="insert into user(name,ph,email,rdate) values('%s','%s','%s','%s')"%(n,m,e,today)
	cursor.execute(sql)
	sqlemp="select max(user_id) from user"
	cursor.execute(sqlemp)
	result=cursor.fetchall()
	for row in result: 
		id=int(row[0])
	sql="insert into login(uid,uname,upass,utype)values('%s','%s','%s','%s')"%(id,e,p,'user')
	cursor.execute(sql)
	html="<script>alert('sucessfully executed');window.location='/register/';</script>"
	return HttpResponse(html)
def serviceadviser(request): 
	return  render(request ,'serviceadviser.html')
def admin(request): 
	return  render(request ,'admin/admin.html')
def feedback(request):
	return render(request,'feedback.html')
def servicing(request):
	cursor=connection.cursor()
	sql="select *from  category"
	cursor.execute(sql)
	results=cursor.fetchall()
	list=[]
	for row in results:
		w={'catcode':row[0],
			'catname':row[1],
		}
		list.append(w)
	sql2="select *from  service"
	cursor.execute(sql2)
	results2=cursor.fetchall()
	list2=[]
	for row2 in results2:
		w1={'sid':row2[0],
			'catid':row2[1],
			'stype':row2[2],
			'desp':row2[3],
			'amt':row2[4],
			}
		list2.append(w1)
	return render(request,'servicing.html',{'list':list,'list2':list2})
def category(request):
	cursor=connection.cursor()
	sql="select *from  category"
	cursor.execute(sql)
	results=cursor.fetchall()
	list=[]
	for row in results:
		w={'catcode':row[0],
			'catname':row[1],
		}
		list.append(w)
	return render(request,'category.html',{'list':list})
def catdelete(request):
	cursor=connection.cursor()
	sql="delete from  category where catcode='%s'"%(request.GET['id'])
	cursor.execute(sql)
	html="<script>alert('sucessfully deleted');window.location='/category/';</script>"
	return HttpResponse(html)
def booking(request):
	sid=request.GET['id']
	return render(request,'booking.html',{'sid':sid})
def bookingaction(request):
	return render(request,'bookingaction.html')

def serviceadviserinsert(request): 
	cursor=connection.cursor()
	name=request.GET['t1'] 
	ph=request.GET['t2']
	em=request.GET['t3']
	adr=request.GET['t4']	
	do=request.GET['t5']
	ps=request.GET['t6']
	qu=request.GET['t7']	
	sql="insert into mechanics(mname,phno,email,addr,doj,qua)values('%s','%s','%s','%s','%s','%s')"%(name,ph,em,adr,do,qu)
	cursor.execute(sql)
	sqlemp="select max(mid) from mechanics"
	cursor.execute(sqlemp)
	result=cursor.fetchall()
	for row in result: 
		id=int(row[0])
	sql="insert into login(uid,uname,upass,utype)values('%s','%s','%s','%s')"%(id,em,ps,'mechanics')
	cursor.execute(sql)
	html="<script>alert('sucessfully executed');window.location='/mechanic/';</script>"
	return HttpResponse(html)
def assigninsert(request): 
	cursor=connection.cursor()
	sid=request.GET['sid'] 
	mid=request.GET['me']
	sql="insert into assign(sid,mid,status)values('%s','%s','%s')"%(sid,mid,'pending')
	cursor.execute(sql)
	sql="update service set status='Assigned'   where sid='%s'"%(sid)
	cursor.execute(sql)
	html="<script>alert('sucessfully executed');window.location='/vservices/';</script>"
	return HttpResponse(html)
def mech(request): 
	cursor=connection.cursor()
	sql2="select *from  mechanics"
	cursor.execute(sql2)
	results2=cursor.fetchall()
	list2=[]
	for row2 in results2:
		w1={'mid':row2[0],
			'mname':row2[1],
			'phno':row2[2],
			'email':row2[3],
			'addr':row2[4],
			'doj':row2[5],
			'qua':row2[6],
			}
		list2.append(w1)
	return list2
def vmech(request): 
	cursor=connection.cursor()
	sql2="select *from  mechanics"
	cursor.execute(sql2)
	results2=cursor.fetchall()
	list2=[]
	for row2 in results2:
		w1={'mid':row2[0],
			'mname':row2[1],
			'phno':row2[2],
			'email':row2[3],
			'addr':row2[4],
			'doj':row2[5],
			'qua':row2[6],
			}
		list2.append(w1)
	return render(request,'managemechanics.html',{'list2':list2})
def vuser(request): 
	cursor=connection.cursor()
	sql2="select *from  user"
	cursor.execute(sql2)
	results2=cursor.fetchall()
	list2=[]
	for row2 in results2:
		w1={'user_id':row2[0],
			'name':row2[1],
			'email':row2[2],
			'ph':row2[3],
			'rdate':row2[4],
			}
		list2.append(w1)
	return render(request,'users.html',{'list':list2})
def delmech(request):
	cursor=connection.cursor()
	sql="delete from  mechanics where mid='%s'"%(request.GET['id'])
	cursor.execute(sql)
	html="<script>alert('sucessfully deleted');window.location='/vmech/';</script>"
	return HttpResponse(html)
def deluser(request):
	cursor=connection.cursor()
	sql="delete from  user where user_id='%s'"%(request.GET['id'])
	cursor.execute(sql)
	html="<script>alert('sucessfully deleted');window.location='/vuser/';</script>"
	return HttpResponse(html)
def vehaction(request):
	saved = False
	if request.method == "POST":
		MyItemForm = vForm(request.POST, request.FILES)
		if MyItemForm.is_valid():
				item = vitem()
				item.mno =MyItemForm.cleaned_data['mno']
				item.mname =request.POST['t2']
				item.color =request.POST['t3']
				item.scap =request.POST['t4']
				item.fea =request.POST['t5']
				item.mil =request.POST['t6']
				item.amt =request.POST['t9']
				item.img =MyItemForm.cleaned_data['img']
				item.status ='available'
				item.save()
				html = "<script>alert('successfully added! ');window.location='/vehicle/';</script>"
	else:
			MyItemForm = vForm()
	return HttpResponse(html)	
def vvehicles(request): 
	cursor=connection.cursor()
	if request.method == 'GET' and 'id' in request.GET:
		sql2="select * from vehicle where vehid='%s'" %(request.GET['id'])
	else:
		sql2="select *from  vehicle"
	cursor.execute(sql2)
	results2=cursor.fetchall()
	list2=[]
	for row2 in results2:
		w1={'vehid':row2[0],
			'mno':row2[1],
			'mname':row2[2],
			'color':row2[3],
			'scap':row2[4],
			'fea':row2[5],
			'mil':row2[6],
			'amt':row2[7],
			'img':row2[8],
			'status':row2[9],
			}
		list2.append(w1)
	if request.method == 'GET' and 'id' in request.GET:
		return render(request,'details.html',{'list':list2})	
	else:
		if(request.session['utype']=='admin'):
				return render(request,'viewvehicles.html',{'list':list2})	
		elif(request.session['utype']=='user'):
				return render(request,'viewvehicleuser.html',{'list':list2})	
	
def vservices(request): 
	cur=connection.cursor()
	if(request.session['utype']=='admin'):
			sql1="select * from service inner join user on user.user_id=service.vid"
	elif(request.session['utype']=='user'):
			sql1="select * from service inner join user on user.user_id=service.vid  where service.vid='%s'"%(request.session['uid'])
	cur.execute(sql1)
	#return HttpResponse(sql1)
	results2=cur.fetchall()
	list2=[]
	for row2 in results2:
		mname="Null"
		sql12="select mechanics.mname from assign  inner join mechanics on mechanics.mid=assign.mid where assign.sid='%s'"%(row2[0])
		cur.execute(sql12)
		#return HttpResponse(sql12)
		results22=cur.fetchall()
		for row22 in results22:
			mname=row22[0]
		w1={'sid':row2[0],
			'vid':row2[1],
			'cat':row2[2],
			'vname':row2[3],
			'vmodel':row2[4],
			'vbrand':row2[5],
			'vno':row2[6],
			'sdate':row2[7],
			'stime':row2[8],
			'dtype':row2[9],
			'stype':row2[10],
			'stype2':row2[11],
			'sdate2':row2[12],
			'stype3':row2[13],
			'sdate3':row2[14],
			'status':row2[15],
			'user_id':row2[16],
			'name':row2[17],
			'ph':row2[18],
			'email':row2[19],
			'mname':mname
			}
		list2.append(w1)
		
	mec=mech(request)
	if(request.session['utype']=='admin'):
			return render(request,'viewservices.html',{'list':list2,'mec':mec})	
	elif(request.session['utype']=='user'):
		return render(request,'viewservicesuser.html',{'list':list2,'mec':mec})	
def vservices1(request): 
	cur=connection.cursor()
	sql1="select * from service inner join user on user.user_id=service.vid inner join  assign on assign.sid=service.sid    inner join mechanics on mechanics.mid=assign.mid   where assign.mid='%s'"%(request.session['uid'])
	cur.execute(sql1)
	#return HttpResponse(sql1)
	results2=cur.fetchall()
	list2=[]
	for row2 in results2:
		w1={'sid':row2[0],
			'vid':row2[1],
			'cat':row2[2],
			'vname':row2[3],
			'vmodel':row2[4],
			'vbrand':row2[5],
			'vno':row2[6],
			'sdate':row2[7],
			'stime':row2[8],
			'dtype':row2[9],
			'stype':row2[10],
			'stype2':row2[11],
			'sdate2':row2[12],
			'stype3':row2[13],
			'sdate3':row2[14],
			'status':row2[15],
			'user_id':row2[16],
			'name':row2[17],
			'ph':row2[18],
			'email':row2[19],
			
			}
		list2.append(w1)
		
	return render(request,'viewserviceass.html',{'list':list2})	
def vservicesuser(request): 
	cur=connection.cursor()
	
	sql1="select * from service inner join servicedone on service.sid=servicedone.vid  where service.vid='%s'"%(request.session['uid'])
	cur.execute(sql1)
	results2=cur.fetchall()
	list2=[]
	for row2 in results2:
		w1={'sid':row2[0],
			'vid':row2[1],
			'cat':row2[2],
			'vname':row2[3],
			'vmodel':row2[4],
			'vbrand':row2[5],
			'vno':row2[6],
			'sdate':row2[7],
			'stime':row2[8],
			'dtype':row2[9],
			'stype':row2[10],
			'stype2':row2[11],
			'sdate2':row2[12],
			'stype3':row2[13],
			'sdate3':row2[14],
			'status':row2[15],
			'amt':row2[22],
			'sstaus':row2[23],
			
			}
		list2.append(w1)
	return render(request,'viewservicesuser.html',{'list':list2})	
def servicedone(request): 
	cur=connection.cursor()
	sql1="select * from service inner join user on user.user_id=service.vid  where service.sid='%s'"%(request.GET['id'])
	cur.execute(sql1)
	results2=cur.fetchall()
	list2=[]
	for row2 in results2:
		w1={'sid':row2[0],
			'vid':row2[1],
			'cat':row2[2],
			'vname':row2[3],
			'vmodel':row2[4],
			'vbrand':row2[5],
			'vno':row2[6],
			'sdate':row2[7],
			'stime':row2[8],
			'dtype':row2[9],
			'stype':row2[10],
			'stype2':row2[11],
			'sdate2':row2[12],
			'stype3':row2[13],
			'sdate3':row2[14],
			'status':row2[15],
			'user_id':row2[16],
			'name':row2[17],
			'ph':row2[18],
			'email':row2[19],
			}
		list2.append(w1)
	return render(request,'servicedone.html',{'list':list2})
def aservice(request):
	cursor=connection.cursor()
	sql="update service set status='Approve' where sid='%s'"%(request.GET['id'])
	cursor.execute(sql)
	html="<script>alert('sucessfully deleted');window.location='/vservices/';</script>"
	return HttpResponse(html)	
def rservice(request):
	cursor=connection.cursor()
	sql="update service set status='Reject' where sid='%s'"%(request.GET['id'])
	cursor.execute(sql)
	html="<script>alert('sucessfully deleted');window.location='/vservices/';</script>"
	return HttpResponse(html)
def vehdelete(request):
	cursor=connection.cursor()
	sql="delete from  vehicle where vehid='%s'"%(request.GET['id'])
	cursor.execute(sql)
	html="<script>alert('sucessfully deleted');window.location='/vvehicles/';</script>"
	return HttpResponse(html)
def servicedoneaction(request): 
	cursor=connection.cursor()
	id=request.GET['t0'];
	sid=request.GET['sid'];
	fn=request.GET['t1'];
	vt=request.GET['t4'];
	vno=request.GET['t5'];
	sd=request.GET['t6'];
	amt=request.GET['t7'];
	status=request.GET['t8'];
	stype=request.GET['t9'];
	
	sql="insert into servicedone(vid,fname,vtype,vno,sd,amt,sstatus,stype)values('%s','%s','%s','%s','%s','%s','%s','%s')"%(id,fn,vt,vno,sd,amt,status,stype)
	cursor.execute(sql)
	if status=='Completed':
		sql1="update service  set status='%s' where sid='%s'"%(status,sid)
		cursor.execute(sql1)
	html="<script>alert('sucessfully updated');window.location='/adminhome/';</script>"
	return HttpResponse(html)
def serviceaction(request): 
	cursor=connection.cursor()
	val=request.session['uid'];
	cat=request.GET['t1'];
	vname=request.GET['t2'];
	vmodel=request.GET['t3'];
	vbrand=request.GET['t4'];
	vno=request.GET['t5'];
	sdate=request.GET['t7'];
	stime=request.GET['t8'];
	dtype=request.GET['t9'];
	stype=request.GET['t10'];
	qty=request.GET['t4'];
	
	sql="insert into service(vid,cat,vname,vmodel,vbrand,vno,sdate,stime,dtype,stype,status)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(val,cat,vname,vmodel,vbrand,vno,sdate,stime,dtype,stype,'pending')
	cursor.execute(sql)
	html="<script>alert('sucessfully requested');window.location='/services/';</script>"
	return HttpResponse(html)
def vservicedoneadmin(request): 
	cur=connection.cursor()
	if(request.session['utype']=='admin'):
			sql1="select * from servicedone"
	elif(request.session['utype']=='user'):
		sql1="select * from servicedone where vid='%s'"%(request.session['uid'])
	cur.execute(sql1)
	results2=cur.fetchall()
	list2=[]
	for row2 in results2:
		w1={'sdid':row2[0],
			'vid':row2[1],
			'fname':row2[2],
			'vtype':row2[3],
			'vno':row2[4],
			'sd':row2[5],
			'amt':row2[6],
			'sstatus':row2[7],
			'stype':row2[8],
			
			}
		list2.append(w1)
	if(request.session['utype']=='admin'):
			return render(request,'viewservicedoneadmin.html',{'list':list2})
	elif(request.session['utype']=='user'):
		return render(request,'viewservicedone.html',{'list':list2})
def pay(request):
	cursor=connection.cursor()
	sql="select amt from servicedone where sdid='%s'"%(request.GET['id'])
	cursor.execute(sql)
	results=cursor.fetchall()
	list=[]
	for row in results:
		amt=row[0]
	return render(request,'pay.html',{'amt':amt,'sdid':request.GET['id'],'date':new_today_date})	
def payaction(request): 
	cursor=connection.cursor()
	val=request.session['uid'];
	cat=request.GET['t2'];
	sql="insert into pay(sid,advamt,sdate,status)values('%s','%s','%s','%s')"%(val,cat,today,'Paid')
	cursor.execute(sql)
	html="<script>alert('sucessfully payed');window.location='/userhome/';</script>"
	return HttpResponse(html)	
	

def booking(request): 
	cursor=connection.cursor()
	sql2="select *from  vehicle where vehid='%s'"%(request.GET['id'])
	cursor.execute(sql2)
	results2=cursor.fetchall()
	list2=[]
	for row2 in results2:
		w1={'vehid':row2[0],
			'mno':row2[1],
			'mname':row2[2],
			'color':row2[3],
			'scap':row2[4],
			'fea':row2[5],
			'mil':row2[6],
			'amt':row2[7],
			'img':row2[8],
			'status':row2[9],
			}
		list2.append(w1)
	return render(request,'booking.html',{'list':list2})
def bookaction(request):
	cur=connection.cursor()
	uid=request.session['uid'] 
	vid=request.GET['t0'] 
	qty=request.GET['t4'] 
	sql="insert into bookings(uid,vid,qty,adamt,bdate,status) values('%s','%s','%s','%s','%s','%s')"%(uid,vid,qty,0,today,'pending')
	cur.execute(sql)
	sql1="select max(bid) from bookings"
	cur.execute(sql1)
	results=cur.fetchall()
	list=[]
	for row in results:
		bid=row[0]
	html="<script>window.location='/payment?id=%s';</script>"%(bid)
	return HttpResponse(html)
def payment(request):
	cursor=connection.cursor()
	return render(request,'payment.html',{'bid':request.GET['id']})
def paymentaction(request):
	cursor=connection.cursor()
	sql="update bookings set adamt='%s' ,status='Book' where bid='%s'"%(request.GET['t1'],request.GET['t0'])
	cursor.execute(sql)
	html="<script>alert(' bookedsucessfully ');window.location='/userhome/';</script>"
	return HttpResponse(html)	
def viewvehbookings(request): 
	cur=connection.cursor()
	sql1="select * from bookings inner join user on user.user_id=bookings.uid inner join vehicle on bookings.vid=vehicle.vehid where bookings.uid='%s' and  bookings.status='book'" %(request.session['uid'])
	cur.execute(sql1)
	results2=cur.fetchall()
	list2=[]
	for row2 in results2:
		w1={'bid':row2[0],
			'uid':row2[1],
			'vid':row2[2],
			'qty':row2[3],
			'adamt':row2[4],
			'bdate':row2[5],
			'status':row2[6],
			'user_id':row2[7],
			'name':row2[8],
			'email':row2[9],
			'ph':row2[10],
			'rdate':row2[11],
			'vehid':row2[12],
			'mno':row2[13],
			'mname':row2[14],
			'color':row2[15],
			'scap':row2[16],
			'fea':row2[17],
			'mil':row2[18],
			'amt':row2[19],
			'img':row2[20],
			'status':row2[21],
			}
		list2.append(w1)
	return render(request,'viewvehiclebooking.html',{'list':list2})