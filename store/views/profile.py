# from django.http import HttpResponse
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth.hashers import check_password
# from store.models.customer import Customer
# from django.views import View
# from store.models import customer
# from store.models.product import Products
from store.views import profile
from store.models.customer import Customer
from store.middlewares.auth import auth_middleware

class ProfileView(View):
    # def get(self, request):
    #     return HttpResponse('profile')
    def get(self,request):
        if request.session.has_key('customer'):
            user_email=request.session['customer']
            myUser=Customer.objects.get(id=user_email)
            # myUser=Customer.objects.all()
            return render(template_name="profile.html",
            request=request,context={"profile":myUser})
        else:
            return redirect("/")