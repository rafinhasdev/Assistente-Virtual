import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Backlogs",
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
                ("num_versao", models.FloatField(null=True, unique=True)),
                ("data_postagem", models.DateField(auto_now_add=True)),
                ("data_alteracao", models.DateTimeField()),
                ("descricao", models.TextField()),
                ("dev_responsavel", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="SupportMensagens",
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
                ("descricao", models.TextField(null=True)),
                ("data_envio", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "usuario",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
