from django.urls import path
from .views import (AddProductView, GetCategoriesView,
                    GetBrandsView, GetStoresView, ProductsView, AddOrderView, GetOrderView, DeleteOrderView)


urlpatterns = [
    path('add-products', AddProductView.as_view(), name="AddProduct"),
    path('', ProductsView.as_view(), name="Get_all_products"),
    path('get-categories', GetCategoriesView.as_view(), name="Get_categories"),
    path('get-brands', GetBrandsView.as_view(), name="Get_brands"),
    path('get-order', GetOrderView.as_view(), name="Get_order"),
    path('get-stores', GetStoresView.as_view(), name="Get_stores"),
    path('add-order', AddOrderView.as_view(), name="Add_order"),
    path('delete-order/<int:id>', DeleteOrderView, name="Delete_order"),
]
