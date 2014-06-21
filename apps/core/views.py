# -*- coding: utf-8 -*-
from core.utils import template_response


@template_response('index.html')
def index(request):
    return {}
