from django.urls import path


from megaboss_app.views import *

urlpatterns =[
    path('', index, name="index"),
    path('import-excel', import_excel,name="import_excel"),

    path('api/v1/excel-list', GetList.as_view(), name="api-excel-list"),
    path('api/v1/excel-import', Import_Excel.as_view(), name="api-excel-import"),
    path('api/v1/excel-save', Save_Excel.as_view(), name="api-excel-save"),
    path('api/v1/get-collum',  GetCollum.as_view(), name="api-get-collum"),

    path('api/v1/set-collum', SetCollum.as_view(), name="api-set-collum"),


]