# Generated by Django 5.1.6 on 2025-02-08 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=500)),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('createdat', models.DateTimeField(auto_now_add=True, null=True)),
                ('editedat', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
