from django.urls import path
from . import views

urlpatterns = [
    path("listagents/", views.list_agents),
    path("byclient/<client>/", views.by_client),
    path("bysite/<client>/<site>/", views.by_site),
    path("overdueaction/", views.overdue_action),
    path("sendrawcmd/", views.send_raw_cmd),
    path("<pk>/agentdetail/", views.agent_detail),
    path("<pk>/meshtabs/", views.meshcentral_tabs),
    path("<pk>/takecontrol/", views.take_control),
    path("poweraction/", views.power_action),
    path("uninstallagent/", views.uninstall_agent),
    path("editagent/", views.edit_agent),
    path("<pk>/geteventlog/<logtype>/<days>/", views.get_event_log),
    path("<pk>/updateagent/", views.update_agent),
]