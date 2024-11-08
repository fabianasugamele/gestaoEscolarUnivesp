# Generated by Django 5.1.1 on 2024-10-05 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "gestao_escolar",
            "0006_disciplina_serie_alter_disciplina_tipo_documento_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="turma",
            name="professores",
        ),
        migrations.AlterField(
            model_name="anexodisciplina",
            name="tipo_documento",
            field=models.CharField(
                choices=[
                    ("Plano de Ensino", "Plano de Ensino"),
                    ("Plano de Aula", "Plano de Aula"),
                    ("Diário de Classe", "Diário de Classe"),
                    ("Lista de Lista de Frequência", "Lista de Frequência"),
                    ("Notas", "Notas"),
                    ("Outro", "Outro"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="disciplina",
            name="tipo_documento",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Plano de Ensino", "Plano de Ensino"),
                    ("Plano de Aula", "Plano de Aula"),
                    ("Diário de Classe", "Diário de Classe"),
                    ("Lista de Lista de Frequência", "Lista de Frequência"),
                    ("Notas", "Notas"),
                    ("Outro", "Outro"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
