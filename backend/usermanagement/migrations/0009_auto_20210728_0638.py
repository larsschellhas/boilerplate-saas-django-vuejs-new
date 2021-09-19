# Generated by Django 3.2.5 on 2021-07-28 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0008_subscriptionplan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workspace',
            old_name='name',
            new_name='workspace_name',
        ),
        migrations.AddField(
            model_name='workspace',
            name='company_name',
            field=models.CharField(
                default='Schellhas Engineering', max_length=100, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='features',
            field=models.JSONField(
                verbose_name='The plan\'s features as a list of dictionaries e.g. [{"text": "", "icon": ""}]'),
        ),
    ]
