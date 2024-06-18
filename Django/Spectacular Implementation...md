
Using `drf-spectacular` is another excellent choice for API documentation in Django REST Framework projects. `drf-spectacular` is a library that provides OpenAPI 3.0 schema generation and is often favored for its more complete and feature-rich support 

Here's a step-by-step guide on how to use `drf-spectacular` to document your API:

### Step 1: Install `drf-spectacular`

First, install the `drf-spectacular` library:

```bash
pip install drf-spectacular
```

### Step 2: Configure `drf-spectacular` in Your Project

1. **Update `settings.py`:**

   Add `'drf_spectacular'` to your `INSTALLED_APPS` and configure the REST framework to use `drf-spectacular`:

   ```python
   INSTALLED_APPS = [
       ...
       'rest_framework',
       'drf_spectacular',
       'menu',
       'reservations',
       'orders',  # Ensure this app exists
   ]

   REST_FRAMEWORK = {
       'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
   }
   ```

2. **Update `urls.py`:**

   Add the Spectacular schema view and the Swagger UI view to your `urls.py` file in the main project directory (`restaurant/urls.py`):

   ```python
   from django.contrib import admin
   from django.urls import path, include
   from menu.views import MenuItemViewSet
   from reservations.views import ReservationViewSet
   from orders.views import OrderViewSet
   from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('home.urls')),  # Home app
       path('menu/', include('menu.urls')),  # Menu app (if needed for non-API views)
       path('reservations/', include('reservations.urls')),  # Reservations app (if needed for non-API views)
       path('orders/', include('orders.urls')),  # Orders app (if needed for non-API views)
       path('api/', include(router.urls)),  # API endpoints
       path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
       path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
       path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
   ]
   ```

   This configuration adds three new routes:
   - `/api/schema/` for the raw OpenAPI schema.
   - `/api/schema/swagger-ui/` for the Swagger UI documentation.
   - `/api/schema/redoc/` for the ReDoc documentation.

### Step 3: Add Docstrings to Your Viewsets

To enhance the documentation, add docstrings to your viewsets. These docstrings will be displayed in the Swagger UI.

#### `menu/views.py`

```python
from rest_framework import viewsets
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing the menu items.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
```

#### `reservations/views.py`

```python
from rest_framework import viewsets
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing reservations.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
```

#### `orders/views.py`

```python
from rest_framework import viewsets
from .models import Order  # Ensure Order model is defined
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing orders.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
```

### Step 4: Run the Server and Access Swagger UI

1. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

2. **Access Swagger UI:**

   Open your browser and navigate to `http://127.0.0.1:8000/api/schema/swagger-ui/` to see the Swagger UI with the documentation of your API.

3. **Access ReDoc:**

   Alternatively, you can navigate to `http://127.0.0.1:8000/api/schema/redoc/` to see the ReDoc documentation.
