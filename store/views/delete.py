from django.shortcuts import render,redirect
from django.views import View
from store.models.customer import Customer



class DeleteView(View):
  def post(self,request):
    ddata=Customer.objects.get(id=id)
    ddata.delete()
    return redirect('signup')


# from msilib.schema import Class


# Class DeleteView(View):
# def post(self,request)
#   ddata=Customer.objects.get(id=id)
#   ddata.delete()
#   return redirect('signup')