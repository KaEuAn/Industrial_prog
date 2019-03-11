# Generated by Django 2.1.7 on 2019-03-11 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions_site', '0002_auto_20190312_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='answers_table',
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='questions_site.Questions'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answers',
            name='text',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='questions',
            name='text',
            field=models.CharField(max_length=250),
        ),
    ]
