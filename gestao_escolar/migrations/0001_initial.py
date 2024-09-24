# Generated by Django 5.1.1 on 2024-09-14 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Aluno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("id_num", models.CharField(max_length=50, unique=True)),
                ("nome", models.CharField(max_length=255)),
                ("data_nascimento", models.DateField()),
                ("sexo", models.CharField(blank=True, max_length=10, null=True)),
                ("rg", models.CharField(max_length=20)),
                ("cpf", models.CharField(max_length=14)),
                ("nome_mae", models.CharField(max_length=255)),
                ("cpf_mae", models.CharField(max_length=14)),
                ("nome_pai", models.CharField(blank=True, max_length=255, null=True)),
                ("cpf_pai", models.CharField(blank=True, max_length=14, null=True)),
                ("cep_residencia", models.CharField(max_length=9)),
                ("bairro", models.CharField(max_length=100)),
                ("endereco", models.CharField(max_length=255)),
                ("numero_residencia", models.CharField(max_length=10)),
                (
                    "complemento",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("telefone", models.CharField(max_length=20)),
                ("email", models.EmailField(blank=True, max_length=255, null=True)),
                ("historico_saude", models.TextField(blank=True, null=True)),
                (
                    "tipo_documento",
                    models.CharField(
                        blank=True,
                        choices=[
                            (
                                "Documento de identificação",
                                "Documento de identificação",
                            ),
                            ("Comprovante de residência", "Comprovante de residência"),
                            ("Laudo Médico", "Laudo Médico"),
                            ("Outro", "Outro"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Disciplina",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codigo_disciplina", models.CharField(max_length=50, unique=True)),
                ("nome_disciplina", models.CharField(max_length=255)),
                (
                    "tipo_documento",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("plano_ensino", "Plano de Ensino"),
                            ("plano_aula", "Plano de Aula"),
                            ("lista_frequencia", "Lista de Frequência"),
                            ("outro", "Outro"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "anexos",
                    models.FileField(
                        blank=True, null=True, upload_to="documentos/disciplinas/"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Equipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("id_num", models.CharField(max_length=50, unique=True)),
                ("nome_profissional", models.CharField(max_length=255)),
                ("funcao", models.CharField(max_length=255)),
                ("sexo", models.CharField(blank=True, max_length=10, null=True)),
                ("data_inicio", models.DateField()),
                ("data_saida", models.DateField(blank=True, null=True)),
                ("email", models.EmailField(blank=True, max_length=255, null=True)),
                ("telefone", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "tipo_documento",
                    models.CharField(
                        blank=True,
                        choices=[
                            (
                                "Documento de identificação",
                                "Documento de identificação",
                            ),
                            ("Comprovante de residência", "Comprovante de residência"),
                            ("Laudo Médico", "Laudo Médico"),
                            ("Outro", "Outro"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "anexos",
                    models.FileField(
                        blank=True, null=True, upload_to="documentos/equipe/"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AnexoAluno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("arquivo", models.FileField(upload_to="documentos/alunos/")),
                (
                    "tipo_documento",
                    models.CharField(
                        choices=[
                            (
                                "Documento de identificação",
                                "Documento de identificação",
                            ),
                            ("Comprovante de residência", "Comprovante de residência"),
                            ("Laudo Médico", "Laudo Médico"),
                            ("Outro", "Outro"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "aluno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="anexos",
                        to="gestao_escolar.aluno",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Atendimento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_atendimento", models.DateField()),
                ("tipo_atendimento", models.CharField(max_length=255)),
                ("descricao", models.TextField()),
                (
                    "tipo_documento",
                    models.CharField(
                        blank=True,
                        choices=[
                            (
                                "Documento de identificação",
                                "Documento de identificação",
                            ),
                            ("Comprovante de residência", "Comprovante de residência"),
                            ("Laudo Médico", "Laudo Médico"),
                            ("Outro", "Outro"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "anexos",
                    models.FileField(
                        blank=True, null=True, upload_to="documentos/atendimentos/"
                    ),
                ),
                (
                    "aluno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="atendimentos_aluno",
                        to="gestao_escolar.aluno",
                    ),
                ),
                (
                    "responsavel_atendimento",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="responsavel_atendimento",
                        to="gestao_escolar.equipe",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="aluno",
            name="atendimentos",
            field=models.ManyToManyField(
                blank=True,
                related_name="aluno_atendimentos",
                to="gestao_escolar.atendimento",
            ),
        ),
        migrations.CreateModel(
            name="AlunoDisciplina",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_matricula", models.DateField()),
                (
                    "aluno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestao_escolar.aluno",
                    ),
                ),
                (
                    "disciplina",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestao_escolar.disciplina",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="aluno",
            name="disciplinas",
            field=models.ManyToManyField(
                blank=True,
                through="gestao_escolar.AlunoDisciplina",
                to="gestao_escolar.disciplina",
            ),
        ),
        migrations.CreateModel(
            name="Frequencia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data", models.DateField()),
                ("presente", models.BooleanField()),
                (
                    "aluno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestao_escolar.aluno",
                    ),
                ),
                (
                    "disciplina",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestao_escolar.disciplina",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="disciplina",
            name="frequencias",
            field=models.ManyToManyField(
                related_name="frequencias_aluno",
                through="gestao_escolar.Frequencia",
                to="gestao_escolar.aluno",
            ),
        ),
        migrations.CreateModel(
            name="Nota",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("atividade", models.CharField(max_length=255)),
                ("nota", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "aluno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestao_escolar.aluno",
                    ),
                ),
                (
                    "disciplina",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestao_escolar.disciplina",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="disciplina",
            name="notas",
            field=models.ManyToManyField(
                related_name="notas_aluno",
                through="gestao_escolar.Nota",
                to="gestao_escolar.aluno",
            ),
        ),
        migrations.CreateModel(
            name="Professor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("id_num", models.CharField(max_length=50, unique=True)),
                ("nome", models.CharField(max_length=255)),
                ("sexo", models.CharField(blank=True, max_length=10, null=True)),
                ("data_inicio", models.DateField()),
                ("data_saida", models.DateField(blank=True, null=True)),
                ("email", models.EmailField(blank=True, max_length=255, null=True)),
                ("telefone", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "tipo_documento",
                    models.CharField(
                        blank=True,
                        choices=[
                            (
                                "Documento de identificação",
                                "Documento de identificação",
                            ),
                            ("Comprovante de residência", "Comprovante de residência"),
                            ("Laudo Médico", "Laudo Médico"),
                            ("Outro", "Outro"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "disciplinas",
                    models.ManyToManyField(
                        blank=True,
                        related_name="professores_disciplina",
                        to="gestao_escolar.disciplina",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="disciplina",
            name="professor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="disciplinas_professor",
                to="gestao_escolar.professor",
            ),
        ),
        migrations.CreateModel(
            name="AnexoProfessor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("arquivo", models.FileField(upload_to="documentos/professores/")),
                (
                    "tipo_documento",
                    models.CharField(
                        choices=[
                            (
                                "Documento de identificação",
                                "Documento de identificação",
                            ),
                            ("Comprovante de residência", "Comprovante de residência"),
                            ("Laudo Médico", "Laudo Médico"),
                            ("Outro", "Outro"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "professor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="anexos",
                        to="gestao_escolar.professor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Turma",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_turma", models.CharField(max_length=255)),
                ("ano_turma", models.IntegerField()),
                (
                    "alunos",
                    models.ManyToManyField(
                        related_name="turmas_aluno", to="gestao_escolar.aluno"
                    ),
                ),
                (
                    "disciplinas",
                    models.ManyToManyField(
                        related_name="turmas_disciplina", to="gestao_escolar.disciplina"
                    ),
                ),
                (
                    "professores",
                    models.ManyToManyField(
                        related_name="turmas_professor", to="gestao_escolar.professor"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="professor",
            name="turmas",
            field=models.ManyToManyField(
                related_name="professores_turma", to="gestao_escolar.turma"
            ),
        ),
        migrations.AddField(
            model_name="aluno",
            name="turma",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="alunos_turma",
                to="gestao_escolar.turma",
            ),
        ),
    ]
