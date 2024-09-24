from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic.edit import FormView
from .models import Aluno, AnexoAluno, Professor, AnexoProfessor, Equipe, AnexoEquipe, Disciplina
from .forms import AnexoForm

# View da home -----------------------------------------------------------------

class HomeView(TemplateView):
    template_name = 'home.html'

# View generica de uploads de anexos -------------------------------------------

class UploadAnexosView(FormView):
    template_name = 'object_upload_anexos_form.html'
    form_class = AnexoForm
    model = None  # Será definido nas subclasses
    related_name = 'anexos'  # Nome do campo relacionado para anexos

    def get_object(self):
        return self.model.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context['object'] = obj
        context['anexos'] = getattr(obj, self.related_name).all()
        context['object_url_name'] = f'{self.model.__name__.lower()}_info'
        return context

    def form_valid(self, form):
        arquivos = self.request.FILES.getlist('arquivos')
        obj = self.get_object()
        tipo_documento = form.cleaned_data['tipo_documento']

        for arquivo in arquivos:
            if isinstance(obj, Aluno):
                AnexoAluno.objects.create(aluno=obj, arquivo=arquivo, tipo_documento=tipo_documento)
            elif isinstance(obj, Professor):
                AnexoProfessor.objects.create(professor=obj, arquivo=arquivo, tipo_documento=tipo_documento)  # Aqui o campo correto é 'professor'
            elif isinstance(obj, Equipe):
                AnexoEquipe.objects.create(equipe=obj, arquivo=arquivo, tipo_documento=tipo_documento)

        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse(f'{self.model.__name__.lower()}_info', kwargs={'pk': self.kwargs['pk']})

class ExcluirAnexoView(View):
    def post(self, request, pk):
        # Tenta encontrar o anexo para alunos ou professores
        anexo_aluno = AnexoAluno.objects.filter(pk=pk).first()
        anexo_professor = AnexoProfessor.objects.filter(pk=pk).first()
        anexo_equipe = AnexoEquipe.objects.filter(pk=pk).first()

        anexo = anexo_aluno or anexo_professor or anexo_equipe

        if anexo:
            anexo.delete()
            messages.success(request, "Anexo excluído com sucesso!")
        else:
            messages.error(request, "Anexo não encontrado!")

        # Redireciona de volta para a página do objeto (aluno/professor)
        return redirect(request.META.get('HTTP_REFERER', '/'))

# Views das classes de alunos --------------------------------------------------

# View da lista de alunos

class AlunosListView(ListView):
    model = Aluno
    template_name = 'alunos_list.html'
    context_object_name = 'alunos'

    def get_queryset(self):
        # Ordena os alunos pelo nome em ordem alfabética
        return Aluno.objects.all().order_by('nome')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        alunos = context['alunos']

        # Cria uma lista para adicionar dados de idade e turma ativa
        for aluno in alunos:
            aluno.idade = aluno.idade  # Calcula a idade usando a propriedade
            aluno.turma_ativa = aluno.turma_ativa()  # Obtém a turma ativa usando o método

        context['alunos'] = alunos  # Atualiza a lista de alunos com os dados adicionais
        return context

# View das informações de um aluno

class AlunoInfoView(View):
    def get(self, request, *args, **kwargs):
        aluno = get_object_or_404(Aluno, pk=kwargs['pk'])

        # Passa os anexos do aluno para o contexto
        anexos = aluno.anexos.all()

        # Cria o contexto com aluno e anexos
        context = {
            'aluno': aluno,
            'anexos': anexos
        }

        return render(request, "aluno_info.html", context)

# View para cadastrar um aluno

class AlunoCreateView(CreateView):
    model = Aluno
    fields = ["id_num", "nome", "data_nascimento", "sexo", "rg", "cpf", "nome_mae",
              "cpf_mae", "nome_pai","cpf_pai","cep_residencia","bairro","endereco",
              "numero_residencia","complemento","telefone","email","historico_saude"]
    success_url = reverse_lazy("aluno_upload_anexos")
    template_name = "aluno_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Aluno cadastrado com sucesso!")
        aluno = form.save()  # Salva o aluno e retorna o objeto criado
        return redirect('aluno_upload_anexos', pk=aluno.pk)

# View para atualizar um aluno

class AlunoUpdateView(UpdateView):
    model = Aluno
    fields = ["id_num", "nome", "data_nascimento", "sexo", "rg", "cpf", "nome_mae",
              "cpf_mae", "nome_pai","cpf_pai","cep_residencia","bairro","endereco",
              "numero_residencia","complemento","telefone","email","historico_saude"]
    success_url = reverse_lazy("alunos_list")
    template_name = "aluno_form.html"

# View para upload dos anexos

class AlunoAnexosView(UploadAnexosView):
    model = Aluno
    related_name = 'anexos'


# Views das classes de professores ---------------------------------------------

# View da lista de professores

class ProfessoresListView(ListView):
    model = Professor
    template_name = 'professores_list.html'
    context_object_name = 'professores'

    def get_queryset(self):
        # Ordena os professores pelo nome em ordem alfabética
        return Professor.objects.all().order_by('nome')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        professores = context['professores']

        # Cria uma lista para adicionar dados de status e turma ativa
        for professor in professores:
            professor.status = professor.status  # Calcula o satus usando a propriedade
            professor.turma_ativa = professor.turma_ativa()  # Obtém a turma ativa usando o método

        context['professores'] = professores  # Atualiza a lista de professores com os dados adicionais
        return context

# View para cadastrar professor

class ProfessorCreateView(CreateView):
    model = Professor
    fields = ["id_num","nome","sexo","data_inicio","telefone","email"]
    success_url = reverse_lazy("professores_list")
    template_name = "professor_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Professor cadastrado com sucesso!")
        professor = form.save()  # Salva o professor e retorna o objeto criado
        return redirect('professor_upload_anexos', pk=professor.pk)

# View para visualizar informações de um professor

class ProfessorInfoView(View):
    def get(self, request, *args, **kwargs):
        professor = get_object_or_404(Professor, pk=kwargs['pk'])

        # Passa os anexos do professor para o contexto
        anexos = professor.anexos.all()

        # Cria o contexto com professor e anexos
        context = {
            'professor': professor,
            'anexos': anexos
        }

        return render(request, "professor_info.html", context)

# View para atualizarinformações de um professor

class ProfessorUpdateView(UpdateView):
    model = Professor
    fields = ["id_num", "nome", "sexo", "data_inicio","data_saida", "telefone", "email"]
    success_url = reverse_lazy("professores_list")
    template_name = "professor_form.html"

# View para upload de anexos de professores

class ProfessorAnexosView(UploadAnexosView):
    model = Professor
    related_name = 'anexos'


# Views das classes de equipe --------------------------------------------------

# View da lista de equipe

class EquipeListView(ListView):
    model = Equipe
    template_name = 'equipe_list.html'
    context_object_name = 'equipe'

    def get_queryset(self):
        # Ordena os membros da equipe pelo nome em ordem alfabética
        return Equipe.objects.all().order_by('nome_profissional')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        equipe = context['equipe']

        # Cria uma lista para adicionar dados de status
        for membro in equipe:
            membro.status = membro.status  # Calcula o status usando a propriedade

        context['equipe'] = equipe  # Atualiza a lista de membros da equipe com os dados adicionais
        return context

# View para cadastrar membro da equipe

class EquipeCreateView(CreateView):
    model = Equipe
    fields = ["id_num","nome_profissional","funcao","sexo","data_inicio","email","telefone"]
    success_url = reverse_lazy("equipe_list")
    template_name = "equipe_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Membro da equipe cadastrado com sucesso!")
        equipe = form.save()  # Salva o membro da equipe e retorna o objeto criado
        return redirect('equipe_upload_anexos', pk=equipe.pk)

# View para uload de anexos de equipe

class EquipeAnexosView(UploadAnexosView):
    model = Equipe
    related_name = 'anexos'

# View para visualizar informações de um membro da equipe

class EquipeInfoView(View):
    def get(self, request, *args, **kwargs):
        equipe = get_object_or_404(Equipe, pk=kwargs['pk'])

        # Passa os anexos do membro da equipe para o contexto
        anexos = equipe.anexos.all()

        # Cria o contexto com o nome 'equipe'
        context = {
            'equipe': equipe,
            'anexos': anexos
        }

        return render(request, "equipe_info.html", context)

# View para atualizar informações de um membro da equipe

class EquipeUpdateView(UpdateView):
    model = Equipe
    fields = ["id_num", "nome_profissional", "funcao", "sexo", "data_inicio", "data_saida", "email", "telefone"]
    success_url = reverse_lazy("equipe_list")
    template_name = "equipe_form.html"

# Views da classe de disciplinas -----------------------------------------------

# View da lista de disciplinas

class DisciplinasListView(ListView):
    model = Disciplina
    template_name = 'disciplinas_list.html'
    context_object_name = 'disciplinas'

    def get_queryset(self):
        # Ordena as disciplinas pelo nome em ordem alfabética
        return Disciplina.objects.all().order_by('codigo_disciplina')