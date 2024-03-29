# Generated by Django 4.2.7 on 2023-12-22 09:29

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields
import wagtail.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('text', models.TextField(verbose_name='Текст обращения')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
            },
            bases=(wagtail.models.PreviewableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='FeedbackPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True, verbose_name='Текст на странице формы')),
                ('success_text', wagtail.fields.RichTextField(blank=True, verbose_name='Текст на странице благодарности')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Общие настройки',
            },
            bases=('wagtailcore.page',),
        ),
    ]
