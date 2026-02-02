from django.views.generic import CreateView 
from django.urls import reverse_lazy
from rest_framework import permissions 
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView

from produk.forms import ProdukForm

from .serilized import ProdukSerializer
from .models import Produk

from kategori.models import Kategori
from status.models import Status

class ProdukView(CreateView) :
    template_name = "produk/home.html"
    form_class = ProdukForm 
    model = Produk
    success_url = reverse_lazy("produk")

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["produk"] = Produk.objects.filter(status_id=2)
        context["kategori"] = Kategori.objects.all()
        context["status"] = Status.objects.all()
        return context

class BaseProdukAPIView :
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
    permission_classes = [permissions.AllowAny]

class CreateProdukApi(BaseProdukAPIView,CreateAPIView) : ...
class DetailProdukApi(BaseProdukAPIView,RetrieveAPIView) : ...
class UpdateProdukApi(BaseProdukAPIView,UpdateAPIView) : ...
class DeleteProdukApi(BaseProdukAPIView,DestroyAPIView) : ...
