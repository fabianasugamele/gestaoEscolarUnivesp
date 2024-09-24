
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gestao_escolar.views import HomeView,ExcluirAnexoView
from gestao_escolar.views import AlunosListView, AlunoInfoView, AlunoCreateView, AlunoUpdateView, AlunoAnexosView
from gestao_escolar.views import ProfessoresListView, ProfessorCreateView, ProfessorInfoView, ProfessorUpdateView, ProfessorAnexosView
from gestao_escolar.views import EquipeListView, EquipeCreateView, EquipeInfoView, EquipeUpdateView, EquipeAnexosView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),  # Usando .as_view() para a CBV
    path('alunos/', AlunosListView.as_view(), name="alunos_list"),  # Usando .as_view() para a CBV
    path("alunos/info/<int:pk>/", AlunoInfoView.as_view(), name="aluno_info"),
    path("alunos/create/", AlunoCreateView.as_view(), name="aluno_create"),
    path("alunos/update/<int:pk>/", AlunoUpdateView.as_view(), name="aluno_update"),
    path("alunos/upload_anexos/<int:pk>/", AlunoAnexosView.as_view(), name="aluno_upload_anexos"),
    path("professores/", ProfessoresListView.as_view(), name="professores_list"),
    path("professores/create/", ProfessorCreateView.as_view(), name="professor_create"),
    path("professores/info/<int:pk>/", ProfessorInfoView.as_view(), name="professor_info"),
    path("professores/update/<int:pk>/", ProfessorUpdateView.as_view(), name="professor_update"),
    path("professores/upload_anexos/<int:pk>/", ProfessorAnexosView.as_view(), name="professor_upload_anexos"),
    path('anexos/excluir/<int:pk>/', ExcluirAnexoView.as_view(), name='excluir_anexo'),
    path('anexos/excluir/<int:pk>/', ExcluirAnexoView.as_view(), name='excluir_anexo'),
    path('equipe/', EquipeListView.as_view(), name="equipe_list"),
    path('equipe/create/', EquipeCreateView.as_view(), name="equipe_create"),
    path('equipe/info/<int:pk>/', EquipeInfoView.as_view(), name="equipe_info"),
    path('equipe/update/<int:pk>/', EquipeUpdateView.as_view(), name="equipe_update"),
    path('equipe/upload_anexos/<int:pk>/', EquipeAnexosView.as_view(), name="equipe_upload_anexos"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # para servir arquivos de mídia durante o desenvolvimento



