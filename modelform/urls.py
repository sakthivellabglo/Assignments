from django.urls import path 
from modelform import views
urlpatterns = [ path('add/',views.add,name = 'add'),
		path('login',views.user_login,name='login'),
		path('view',views.list_table,name = 'view' ),
		path('delete/<int:id>',views.delete_data,name='delete'),
		path('mark_student/<int:id>',views.update_student,name = 'mark_update'),
		path('mark/<int:id>',views.detail_view,name='detail'),
		path('mark_add',views.mark_add,name = 'mark_add'),
		path('mark_delete/<int:id>',views.delete_mark,name = 'mark_delete'),
		path('mark_update/<int:id>',views.update_mark,name = 'mark_update'),
		path('jsonfile',views.jsondisplay,name = 'json')
		path('mark_delete/<int:id>',views.delete_mark,name = 'mark_add'),
		path('mark_update/<int:id>',views.update_mark,name = 'mark_update')
		]
