from django.urls import path
from movies import views

urlpatterns = [
    path('kgf',views.kgf, name='kgf'),
    path('beast',views.beast, name='beast'),
    path('rrr',views.rrr, name='rrr'),
    path('',views.homepage, name='moviespage'),
    path('update/<id>',views.updatekgf, name='update'),
    path('save_update_data/<id>',views.save_updatedkgf, name='save_update_data'),
    path('delete/<id>',views.deletekgf , name='delete'),
    path('updatebeast/<id>', views.updatebeast,name='updatebeast'),
    path('save_update_best/<id>',views.save_updatebest, name='save_update_best'),
    path('delete_beast/<id>',views.deletebeast, name='delete_beast')
]
