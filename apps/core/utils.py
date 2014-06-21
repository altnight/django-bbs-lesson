# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext


def template_response(template=None):
    def render(func):
        def wrapper(request, *args, **kwargs):
            dst = func(request, *args, **kwargs)
            if not isinstance(dst, dict):
                return dst
            tmpl = dst.pop('template', template)
            return render_to_response(
                tmpl, dst, context_instance=RequestContext(request),
            )
        return wrapper
    return render
