# Generated by Django 3.1.4 on 2021-01-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_auto_20210130_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='view_count',
            new_name='price',
        ),
        migrations.AddField(
            model_name='video',
            name='foodname',
            field=models.CharField(default='모르겠어요', max_length=128, verbose_name='음식이름'),
        ),
        migrations.AddField(
            model_name='video',
            name='restaurant',
            field=models.CharField(default='모르겠어요', max_length=128, verbose_name='가게이름'),
        ),
        migrations.AddField(
            model_name='video',
            name='status',
            field=models.CharField(choices=[('eating', '먹는중'), ('before eating', '먹기전')], max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='거리',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(default='모르겠어요', max_length=128, verbose_name='제목'),
        ),
    ]
