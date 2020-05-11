from django.shortcuts import render
from django.views.generic import View
from . import models


class ListView(View):
    def get(self, request):
        kind = request.GET.get("kind")
        print(kind)

        return render(request, "example/list.html")

class AllView(View):
    def get(self, request):
        pass