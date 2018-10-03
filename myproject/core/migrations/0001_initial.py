# Generated by Django 2.1.2 on 2018-10-03 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='telefone')),
                ('gender', models.CharField(choices=[('0', ''), ('man', 'homem'), ('woman', 'mulher')], default='0', max_length=5, verbose_name='sexo')),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
                'ordering': ('name',),
            },
        ),
    ]