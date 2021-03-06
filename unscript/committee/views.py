from django.db import connections
from django.shortcuts import render

# Create your views here.
from committee.dbOperations import events


def viewEvents(request):
    id = request.session.get('cmid_fk', "")
    event_stud = events()
    return render(request, 'myapp/ViewEvent.html', {'events': event_stud.getCreatedEvents(id)})


def addEvent(request):
    conn = connections['default']
    if request.method == 'POST':
        cmid_fk = request.session.get('cmid_fk', "1")
        ename = request.POST.get('Ename', "Unscript2k18")
        description = request.POST.get('Edescription', 'Hackathod')
        sdate = request.POST.get('sDate', '2018-03-07')
        from_hr = request.POST.get('sTime', '11')
        to_hr = request.POST.get('etime', '1')
        room_id = request.POST.get('location', '511')
        branch = request.POST.get('branch', 'Computer')
        target_aud = request.POST.get('year', 'BE')
        amount = request.POST.get('amount', '5000')
        author = request.POST.get('Authors', 'TCss')
        print(cmid_fk, ename, description, sdate, from_hr, to_hr, room_id, branch, target_aud, amount, author)
        query = "insert into events (cmid_fk,ename,description,date,from_hr,to_hr,room_id,branch,target_aud,amount,author) values(" + cmid_fk + ",'" + ename + "','" + description + "','" + sdate + "'," + from_hr + "," + to_hr + "," + room_id + ",'" + branch + "','" + target_aud + "'," + amount + ",'" + author + "')"
        print("Query=>" + query)
        cursor = conn.cursor()
        cursor.execute(query)
        msg = {"message": "Your Event sent to  Admin for Approval "}
        return render(request, "myapp/AddEvent2.html", msg)
    return render(request, "myapp/AddEvent2.html", {})


def EditEvent(request):
    conn = connections['default']
    if request.method == 'POST':
        cmid_fk = request.session.get('cmid_fk', "1")
        ename = request.POST.get('Ename', "Unscript2k18")
        description = request.POST.get('Edescription', 'Hackathod')
        sdate = request.POST.get('sDate', '2018-03-07')
        from_hr = request.POST.get('sTime', '11')
        to_hr = request.POST.get('etime', '1')
        room_id = request.POST.get('location', '511')
        branch = request.POST.get('branch', 'Computer')
        target_aud = request.POST.get('year', 'BE')
        amount = request.POST.get('amount', '5000')
        author = request.POST.get('Authors', 'TCss')
        id = request.POST.get('ID', 1)
        print(cmid_fk, ename, description, sdate, from_hr, to_hr, room_id, branch, target_aud, amount, author)
        query = "update events set cmid_fk=" + cmid_fk + ", ename='" + ename + "', description='" + description + "' ,date='" + sdate + "', from_hr=" + from_hr + ",to_hr=" + to_hr + "," \
                                                                                                                                                                                      "room_id=" + room_id + ", branch='" + branch + "',target_aud='" + target_aud + "',amount=" + amount + ",author='" + author + "'" \
                                                                                                                                                                                                                                                                                                                   " where eid=" + str(
            id)
        print("Query=>" + query)
        cursor = conn.cursor()
        cursor.execute(query)
        msg = {"message": "Your Event is Updated "}
        return render(request, "myapp/AddEvent2.html", msg)
    return render(request, "myapp/AddEvent2.html", {})


def deleteEvent(request):
    conn = connections['default']
    id = request.POST.get('hidden', '')

    query = "delete from event_student where eid_fk=" + str(id)
    cursor = conn.cursor()
    cursor.execute(query)

    query = "delete from events where eid=" + str(id)
    cursor.execute(query)
    return viewEvents(request)


def editEvent(request):
    conn = connections['default']
    id = request.POST.get('hidden', '')
    query = "select ename, description, date, room_id, from_hr,to_hr, amount, author,eid from events where eid=" + str(
        id)
    cursor = conn.cursor()
    cursor.execute(query)
    rs = cursor.fetchone()
    return render(request, "myapp/AddEvent2.html", {'data': rs})


def rescheduleEvent(request):
    conn = connections['default']
    id = request.POST.get('hidden', '')
    query = "select ename, description, date, room_id, from_hr,to_hr, amount, author,eid from events where eid=" + str(
        id)
    cursor = conn.cursor()
    cursor.execute(query)
    rs = cursor.fetchone()
    return render(request, "myapp/reEdit.html", {'data': rs})


def reschdule(request):
    conn = connections['default']
    if request.method == 'POST':
        cmid_fk = request.session.get('cmid_fk', "1")
        ename = request.POST.get('Ename', "Unscript2k18")
        description = request.POST.get('Edescription', 'Hackathod')
        sdate = request.POST.get('sDate', '2018-03-07')
        from_hr = request.POST.get('sTime', '11')
        to_hr = request.POST.get('etime', '1')
        room_id = request.POST.get('location', '511')
        branch = request.POST.get('branch', 'Computer')
        target_aud = request.POST.get('year', 'BE')
        amount = request.POST.get('amount', '5000')
        author = request.POST.get('Authors', 'TCss')
        id = request.POST.get('ID', 1)
        print(cmid_fk, ename, description, sdate, from_hr, to_hr, room_id, branch, target_aud, amount, author)
        query = "update events set cmid_fk=" + cmid_fk + ", ename='" + ename + "', description='" + description + "' ,date='" + sdate + "', from_hr=" + from_hr + ",to_hr=" + to_hr + "," \
                                                                                                                                                                                      "room_id=" + room_id + ", branch='" + branch + "',target_aud='" + target_aud + "',amount=" + amount + ",author='" + author + "'" \
                                                                                                                                                                                                                                                                                                                   " approve_status=0 where eid=" + str(
            id)
        print("Query=>" + query)
        cursor = conn.cursor()
        cursor.execute(query)
        msg = {"message": "Your Event is Updated "}
        return render(request, "myapp/reEdit.html", msg)
    return render(request, "myapp/reEdit.html", {})


def Desk(request):
    title = []
    desc = []
    td = {}
    query = "select title,description from notice"
    conn = connections['default']
    cursor = conn.cursor()
    cursor.execute(query)
    for t in cursor.fetchall():
        td[t[0]] = t[1]
        print("print")
        print(td[t[0]])
        print(t[0])
    return render(request, 'myapp/Committee.html', {'title': td})
