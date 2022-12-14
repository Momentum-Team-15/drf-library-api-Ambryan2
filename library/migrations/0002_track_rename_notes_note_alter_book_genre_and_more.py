# Generated by Django 4.1.3 on 2022-11-09 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('WANT', 'Want to Read'), ('READING', 'Reading'), ('READ', 'Read')], default='WANT', max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='Notes',
            new_name='Note',
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Fantasy', 'Fantasy'), ('Mystery', 'Mystery'), ('History', 'History'), ('Nonfiction', 'Nonfiction'), ('Sci-Fi', 'Sci-Fi'), ('Thriller', 'Thriller'), ('Kids', 'Kids')], default='Nonfiction', max_length=50),
        ),
        migrations.DeleteModel(
            name='Tracks',
        ),
        migrations.AddField(
            model_name='track',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.book'),
        ),
        migrations.AddField(
            model_name='track',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
