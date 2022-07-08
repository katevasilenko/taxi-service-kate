from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
    DriverListView,
    DriverDetailView,
    DriverCreateView,
    DriverDeleteView,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
    car_assign_driver,
    car_delete_driver,
    DriverLicenseUpdateView

)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list"
    ),
    path(
        "manufacturer/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create"
    ),
    path(
        "manufacturer/<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update"
    ),
    path(
        "manufacturer/<int:pk>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete"
    ),

    path("cars/", CarListView.as_view(), name="car-list"),
    path(
        "cars/<int:pk>/",
        CarDetailView.as_view(),
        name="car-detail"
    ),
    path(
        "cars/create/",
        CarCreateView.as_view(),
        name="car-create"
    ),
    path(
        "cars/<int:pk>/update/",
        CarUpdateView.as_view(),
        name="car-update"
    ),
    path(
        "cars/<int:pk>/delete/",
        CarDeleteView.as_view(),
        name="car-delete"
    ),
    path(
        "cars/driver/<int:pk>/assign/",
        car_assign_driver,
        name="car-assign-driver"
    ),
    path(
        "cars/driver/<int:pk>/delete/",
        car_delete_driver,
        name="car-delete-driver"
    ),

    path(
        "drivers/",
        DriverListView.as_view(),
        name="driver-list"
    ),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
    path(
        "drivers/create/",
        DriverCreateView.as_view(),
        name="driver-create"
    ),
    path(
        "drivers/license/update/<int:pk>/",
        DriverLicenseUpdateView.as_view(),
        name="driver-license-update"
    ),
    path(
        "drivers/<int:pk>/delete/",
        DriverDeleteView.as_view(),
        name="driver-delete"
    )
]

app_name = "taxi"
