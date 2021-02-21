from django.shortcuts import redirect


def login_required(function):
    def wrap(request, *args, **kargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/user/login')
        return function(request, *args, **kargs)
    return wrap