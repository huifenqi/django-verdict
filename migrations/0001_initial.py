# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-31 13:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(db_column=b'f_id', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, db_column=b'f_create_time')),
                ('update_time', models.DateTimeField(auto_now=True, db_column=b'f_update_time')),
                ('state', models.BooleanField(db_column=b'f_state', default=True)),
                ('name', models.CharField(db_column=b'f_name', max_length=64, unique=True)),
                ('description', models.CharField(db_column=b'f_description', max_length=64)),
            ],
            options={
                'db_table': 't_verdict_group',
            },
        ),
        migrations.CreateModel(
            name='GroupPermission',
            fields=[
                ('id', models.AutoField(db_column=b'f_id', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, db_column=b'f_create_time')),
                ('update_time', models.DateTimeField(auto_now=True, db_column=b'f_update_time')),
                ('state', models.BooleanField(db_column=b'f_state', default=True)),
                ('group', models.ForeignKey(db_column=b'f_group_id', on_delete=django.db.models.deletion.CASCADE, to='verdict.Group')),
            ],
            options={
                'db_table': 't_verdict_group_permission',
            },
        ),
        migrations.CreateModel(
            name='GroupUser',
            fields=[
                ('id', models.AutoField(db_column=b'f_id', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, db_column=b'f_create_time')),
                ('update_time', models.DateTimeField(auto_now=True, db_column=b'f_update_time')),
                ('state', models.BooleanField(db_column=b'f_state', default=True)),
                ('group', models.ForeignKey(db_column=b'f_group_id', on_delete=django.db.models.deletion.CASCADE, to='verdict.Group')),
                ('user', models.ForeignKey(db_column=b'f_user_id', on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 't_verdict_group_user',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(db_column=b'f_id', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, db_column=b'f_create_time')),
                ('update_time', models.DateTimeField(auto_now=True, db_column=b'f_update_time')),
                ('state', models.BooleanField(db_column=b'f_state', default=True)),
                ('name', models.CharField(db_column=b'f_name', max_length=128, unique=True)),
                ('description', models.CharField(db_column=b'f_description', max_length=64)),
            ],
            options={
                'db_table': 't_verdict_permission',
            },
        ),
        migrations.CreateModel(
            name='PermissionPile',
            fields=[
                ('id', models.AutoField(db_column=b'f_id', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, db_column=b'f_create_time')),
                ('update_time', models.DateTimeField(auto_now=True, db_column=b'f_update_time')),
                ('state', models.BooleanField(db_column=b'f_state', default=True)),
                ('permission', models.ForeignKey(db_column=b'f_permission_id', on_delete=django.db.models.deletion.CASCADE, to='verdict.Permission')),
            ],
            options={
                'db_table': 't_verdict_permission_pile',
            },
        ),
        migrations.CreateModel(
            name='Pile',
            fields=[
                ('id', models.AutoField(db_column=b'f_id', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, db_column=b'f_create_time')),
                ('update_time', models.DateTimeField(auto_now=True, db_column=b'f_update_time')),
                ('state', models.BooleanField(db_column=b'f_state', default=True)),
                ('name', models.CharField(db_column=b'f_name', max_length=128, unique=True)),
            ],
            options={
                'db_table': 't_verdict_pile',
            },
        ),
        migrations.AddField(
            model_name='permissionpile',
            name='pile',
            field=models.ForeignKey(db_column=b'f_pile_id', on_delete=django.db.models.deletion.CASCADE, to='verdict.Pile'),
        ),
        migrations.AddField(
            model_name='grouppermission',
            name='permission',
            field=models.ForeignKey(db_column=b'f_permission_id', on_delete=django.db.models.deletion.CASCADE, to='verdict.Permission'),
        ),
        migrations.AlterUniqueTogether(
            name='groupuser',
            unique_together=set([('group', 'user', 'state')]),
        ),
        migrations.AlterUniqueTogether(
            name='grouppermission',
            unique_together=set([('group', 'permission', 'state')]),
        ),
    ]
