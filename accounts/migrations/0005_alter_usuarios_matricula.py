from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_remove_usuarios_nome_remove_usuarios_sobrenome_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuarios",
            name="matricula",
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
