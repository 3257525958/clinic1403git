from django.urls import path

from peyment_app import views


urlpatterns = [
    path('',views.OrderPageView.as_view(),name='order_page'),
    path('pay/',views.OrderPayView.as_view(),name='order'),
    path('verify/',views.VerifyPayView.as_view(),name='verify'),
    path('irandar/',views.OrderPayViewirandagaah.as_view(),name='irandargah'),
    path('irandargahcallback/',views.Verifyi.as_view(),name='irandargahverify'),
    path('zibal/',views.orderzibal,name='zibal'),
    path('verifyzibal/',views.callbackzibal, name='zibalverify'),
    path('end/',views.end, name='end')
    ]
