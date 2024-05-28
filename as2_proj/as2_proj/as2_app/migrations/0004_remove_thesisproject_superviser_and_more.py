# Generated by Django 5.0.4 on 2024-05-28 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('as2_app', '0003_alter_thesisproject_superviser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thesisproject',
            name='superviser',
        ),
        migrations.AddField(
            model_name='thesisproject',
            name='supervisor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='theses_supervised', to='as2_app.supervisor'),
            preserve_default=False,
        ),
    ]
