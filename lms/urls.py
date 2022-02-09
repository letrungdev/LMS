from django.urls import path
from . import views

urlpatterns = [

#Shared URL
    path('', views.base, name='base'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register'),


#Admin URL
    path('boss/', views.boss, name='boss'),
    path('bulist', views.BUserListView.as_view(), name='bulist'),
    path('bauser', views.bauser, name='bauser'),
    path('bauser_form/', views.bauser_form, name='bauser_form'),
    path('bmuser', views.BMUserListView.as_view(), name='bmuser'),
    path('beuser/<int:pk>', views.beuser, name='beuser'),
    path('uduser/<int:pk>', views.uduser, name='uduser'),
    path('bduser/<int:pk>', views.delete_user, name='bduser'),

    path('buesearch', views.buesearch, name='buesearch'),
    path('bbesearch', views.bbesearch, name='bbesearch'),
    path('bblist/', views.BBookListView.as_view(), name='bblist'),

    path('bbslist/', views.bstatus, name='bbslist'),

    path('babook', views.babook, name='babook'),
    path('babook_form/', views.babook_form, name='babook_form'),
    path('bmbook', views.BMBookListView.as_view(), name='bmbook'),
    path('bebook/<int:pk>', views.bebook, name='bebook'),
    path('udbook/<int:pk>', views.udbook, name='udbook'),
    path('bdbook/<int:pk>', views.delete_book, name='bdbook'),
    path('bssearch/', views.bssearch, name='bssearch'),
    path('bsearch/', views.bsearch, name='bsearch'),
    path('brsearch/', views.brsearch, name='brsearch'),
    path('bbsearch/', views.bbsearch, name='bbsearch'),
    path('bhsearch/', views.bhsearch, name='bhsearch'),
    path('brlist', views.BRequestListView.as_view(), name='brlist'),
    path('baborrow/<int:pk>', views.baborrow, name='baborrow'),
    path('bdrequest/<int:pk>', views.delete_request, name='bdrequest'),

    path('bslist', views.BSListView.as_view(), name='bslist'),
    path('bdbr/<int:pk>', views.delete_borrow, name='bdbr'),
    path('bahistory/<int:pk>', views.bahistory, name='bahistory'),
    path('history', views.BHListView.as_view(), name='bhlist'),


#User URL
    path('user/', views.UBookListView.as_view(), name='user'),
    path('base/<username>', views.user, name='ubase'),
    path('ustatus/<username>', views.ustatus, name='ustatus'),

    path('urequest/<int:pk>', views.urequest, name='urequest'),

    path('urequestb/<int:pk>', views.urequestb, name='urequestb'),
    path('usearch/', views.usearch, name='usearch'),
    path('uchoose/', views.uchoose, name='uchoose'),
]