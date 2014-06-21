# -*- coding: utf-8 -*-


def current_user(request):
    """
    return current login user
    """
    u = request.session.get('user', None)
    return {"current_user": u}
