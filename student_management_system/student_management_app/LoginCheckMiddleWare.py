from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.http import HttpResponseRedirect

class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):
        modilename = view_func.__module__
        user = request.user
        if user.is_authenticated:
            if modulename == "student_management_app.HodViews":
                pass
            elif modulename == "student_management_app.views":
                pass
            else:
                return HttpResponseRedirect(reverse("show_login"))
        else:
            if request.path == reverse("show_login" or request.path == reverse("do_login")):
                pass
            else:
                return HttpResponseRedirect(reverse("show_login"))