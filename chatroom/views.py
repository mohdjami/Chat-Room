from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def room(request, room_name, username="Anonymous"):
    return render(request, 'chatroom.html', {'roomname': room_name, 'username': username})


def joinRoom(request):
    return render(request, 'join.html', {})


def redirect(request):
    if request.method == 'POST':
        username = request.POST['username']
        roomname = request.POST['roomname']
        resp = {'roomname': roomname, 'username': username}
        return room(request, roomname, username)
