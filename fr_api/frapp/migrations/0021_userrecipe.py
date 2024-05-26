# Generated by Django 5.0.4 on 2024-05-02 06:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frapp', '0020_userfavoriterecipe_delete_userrecipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=150)),
                ('featured_img', models.ImageField(null=True, upload_to='recipe_imgs/')),
                ('recipe_description', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frapp.user')),
            ],
            options={
                'verbose_name_plural': '5. User Recipe',
            },
        ),
    ]