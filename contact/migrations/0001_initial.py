# Generated by Django 2.1.7 on 2019-03-17 03:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=26)),
                ('sobrenome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.IntegerField()),
                ('celular', models.IntegerField()),
                ('site', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('texto', models.CharField(max_length=1000)),
                ('contato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Contato')),
            ],
        ),
    ]