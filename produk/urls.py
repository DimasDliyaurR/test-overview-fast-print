from django.urls import path

from produk.views import CreateProdukApi, DeleteProdukApi, DetailProdukApi, ProdukView, UpdateProdukApi

urlpatterns = [
    path("",ProdukView.as_view(),name="produk"),
    path("",CreateProdukApi.as_view(),name="produk.create"),
    path("<int:pk>/",UpdateProdukApi.as_view(),name="produk.update"),
    path("detail/<int:pk>/",DetailProdukApi.as_view(),name="produk.detail"),
    path("delete/<int:pk>/",DeleteProdukApi.as_view(),name="produk.delete")
]
