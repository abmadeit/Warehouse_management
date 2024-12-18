from django.urls import path
# from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from inventory.views import OrderViewSet, OrderProductViewSet, Inventory_MovementViewSet

urlpatterns = [
    # path('', include(router.urls)), 
    path('create/user/', create_user, name='create_user'),
    path('create/warehouse/', create_warehouse, name='create_warehouse'),
    path('create/category/', create_category, name='create_category'),
    path('users/', get_users, name='get_users'),
    path('warehouses/', get_warehouses, name='get_warehouses'),
    path('categories/', get_categories, name='get_categorys'),
    path('user/<int:pk>/update/', update_user, name='update_user'),
    path('warehouse/<int:pk>/update/', update_warehouse, name='update_warehouse'),
    path('category/<int:pk>/update/', update_category, name='update_category'),
    path('user/<int:pk>/delete/', delete_user, name='delete_user'),
    path('warehouse/<int:pk>/delete/', delete_warehouse, name='delete_warehouse'),
    path('category/<int:pk>/delete/', delete_category, name='delete_category'),
    path('warehouse/<int:pk>/', get_warehouse, name='get_warehouse'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Initialize DefaultRouter
# router = DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'roles', RoleViewSet)
# router.register(r'warehouses', WarehouseViewSet)
# router.register(r'products', ProductViewSet)
# router.register(r'stocks', StockViewSet)
# router.register(r'suppliers', SupplierViewSet)
# router.register(r'shipments', ShipmentViewSet)
# router.register(r'orders', OrderViewSet)
# router.register(r'orderproducts', OrderProductViewSet)
# router.register(r'inventorymovement', Inventory_MovementViewSet)