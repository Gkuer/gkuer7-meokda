# Generated by Django 3.1.4 on 2021-01-22 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
        ('user', '0003_auto_20210103_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('file', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('tags', models.ManyToManyField(to='tag.Tag', verbose_name='태그\x1d')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.meokda_user', verbose_name='작성자')),
            ],
        ),
    ]
