# Generated by Django 5.0.4 on 2024-05-28 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('as2_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('supervisor_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('department', models.CharField(max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='thesisproject',
            name='id',
        ),
        migrations.AlterField(
            model_name='thesisproject',
            name='relv_desc',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='thesisproject',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='thesisproject',
            name='topic_num',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('student_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('major', models.CharField(max_length=100)),
                ('thessis', models.ManyToManyField(related_name='students', to='as2_app.thesisproject')),
            ],
        ),
        migrations.AlterField(
            model_name='thesisproject',
            name='superviser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theses_supervised', to='as2_app.supervisor'),
        ),
    ]
