from django.urls import path
from . import views

app_name = 'indexurl'
urlpatterns = [
	path('', views.myindex, name='index'),
	path('contact/',  views.mycontact ,name='contact'),
	path('about/',  views.myabout ,name='about'),
	path('service/',  views.myse ,name='service'),
	path('our-advantages/',  views.myadvan ,name='advan'),
	path('platform/',  views.myplat ,name='plat'),
	path('policies/',  views.mypoli ,name='poli'),
	path('trading-assets/',  views.mytrade ,name='trade'),
	path('withdrawal-method/',  views.mywith ,name='with'),
	path('reffer/',  views.myref ,name='ref'),
	path('funding', views.myfunding, name='fund'),
	path('app', views.myapp, name='app'),


    ]

