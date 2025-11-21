from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("=" * 70))
        self.stdout.write(
            self.style.WARNING("Iniciando carga de grupos de usuários...")
        )
        self.stdout.write(self.style.WARNING("=" * 70))

        grupos = ["ADMINISTRADOR", "USUARIO_SIMPLES"]

        grupos_criados = []
        grupos_existentes = []

        for nome_grupo in grupos:
            grupo, created = Group.objects.get_or_create(name=nome_grupo)

            if created:
                grupos_criados.append(nome_grupo)
                self.stdout.write(
                    self.style.SUCCESS(f'   ✓ Grupo "{nome_grupo}" criado com sucesso!')
                )
            else:
                grupos_existentes.append(nome_grupo)
                self.stdout.write(
                    self.style.WARNING(f'   → Grupo "{nome_grupo}" já existe')
                )

        self.stdout.write("\n" + "=" * 70)
        self.stdout.write(self.style.SUCCESS("✓ PROCESSO CONCLUÍDO!"))
        self.stdout.write("=" * 70)

        self.stdout.write("\nRESUMO:\n")

        if grupos_criados:
            self.stdout.write(f'   ✓ Grupos criados: {", ".join(grupos_criados)}')

        if grupos_existentes:
            self.stdout.write(
                f'   → Grupos já existentes: {", ".join(grupos_existentes)}'
            )

        self.stdout.write(f"\n    Total de grupos no sistema: {Group.objects.count()}")

        # Listar todos os grupos
        self.stdout.write("\nGRUPOS CADASTRADOS NO SISTEMA:\n")

        for grupo in Group.objects.all().order_by("name"):
            self.stdout.write(f"│ {grupo.id:<5} │ {grupo.name:<58} │")
