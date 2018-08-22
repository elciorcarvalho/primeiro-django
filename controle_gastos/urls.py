"""controle_gastos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contas.views import index, listagem, nova_transacao, update, delete

urlpatterns = [
    # URL para admin
    path('admin/', admin.site.urls),
    # URL para a listagem dos insets do banco
    path('', listagem, name='url_listagem'),
    # URL formulario de cadastro
    path('transacao', nova_transacao, name='url_transacao'),
    # URL para UPDATE no DB
    path('update/<int:pk>', update, name='url_update'),
    # URL para DELETE no DB
    path('delete/<int:pk>', delete, name='url_delete')
]
