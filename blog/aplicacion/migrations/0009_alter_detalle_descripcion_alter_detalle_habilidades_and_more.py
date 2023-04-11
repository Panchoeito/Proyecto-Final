# Generated by Django 4.2 on 2023-04-11 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0008_detalle_habilidades_detalle_otros_proyectos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='descripcion',
            field=models.OneToOneField(blank=True, default='Ingrese aquí sus proyectos', null=True, on_delete=django.db.models.deletion.RESTRICT, to='aplicacion.persona'),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='habilidades',
            field=models.CharField(blank=True, default='Ingrese aquí sus proyectos', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='mi_blog',
            field=models.CharField(blank=True, default='Ingrese aquí sus proyectos', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='otros_proyectos',
            field=models.CharField(blank=True, default='Ingrese aquí sus proyectos', max_length=400, null=True),
        ),
    ]