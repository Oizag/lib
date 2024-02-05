# Generated by Django 4.2.7 on 2023-12-22 09:29

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.admin.forms.choosers
import wagtail.blocks
import wagtail.contrib.routable_page.models
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('introduction', models.TextField(blank=True, help_text='Text to describe the page')),
                ('body', wagtail.fields.StreamField([('text', wagtail.blocks.RichTextBlock(label='Текст')), ('html_code', wagtail.blocks.RawHTMLBlock(label='Код')), ('image_block', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('embed_block', wagtail.embeds.blocks.EmbedBlock(label='Видео')), ('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='Текст кнопки', max_length=255, required=True)), ('link', wagtail.blocks.StructBlock([('link_to', wagtail.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL'), ('email', 'Email'), ('anchor', 'Anchor'), ('phone', 'Phone')], classname='link_choice_type_selector', label='Link to', required=False)), ('page', wagtail.blocks.PageChooserBlock(form_classname='page_link', label='Page', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', label='File', required=False)), ('custom_url', wagtail.blocks.CharBlock(form_classname='custom_url_link url_field', label='Custom URL', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('anchor', wagtail.blocks.CharBlock(form_classname='anchor_link', label='#', max_length=300, required=False)), ('email', wagtail.blocks.EmailBlock(required=False)), ('phone', wagtail.blocks.CharBlock(form_classname='phone_link', label='Phone', max_length=30, required=False)), ('new_window', wagtail.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))], closed=True, label=' ', max_length=255, required=True)), ('classes', wagtail.blocks.CharBlock(help_text='Дополнительные CSS классы.                    Вводятся через пробел', label='Дополнительные классы', max_length=255, required=False))])), ('documents', wagtail.blocks.StructBlock([('documents', wagtail.blocks.StreamBlock([('document', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(label='Название документа', max_length=255, required=True)), ('file', wagtail.documents.blocks.DocumentChooserBlock(label='Файл', required=True))], required=True))], help_text='Максимальное количество документов 10', label='Документы', max_num=10))])), ('cols', wagtail.blocks.StructBlock([('class_column', wagtail.blocks.CharBlock(help_text='Пример: col-12 col-md-6 col-lg-4', max_length=30, verbose_name='Классы для разметки колонок')), ('content', wagtail.blocks.StreamBlock([('content', wagtail.blocks.RichTextBlock()), ('html_code', wagtail.blocks.RawHTMLBlock()), ('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='Текст кнопки', max_length=255, required=True)), ('link', wagtail.blocks.StructBlock([('link_to', wagtail.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL'), ('email', 'Email'), ('anchor', 'Anchor'), ('phone', 'Phone')], classname='link_choice_type_selector', label='Link to', required=False)), ('page', wagtail.blocks.PageChooserBlock(form_classname='page_link', label='Page', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', label='File', required=False)), ('custom_url', wagtail.blocks.CharBlock(form_classname='custom_url_link url_field', label='Custom URL', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('anchor', wagtail.blocks.CharBlock(form_classname='anchor_link', label='#', max_length=300, required=False)), ('email', wagtail.blocks.EmailBlock(required=False)), ('phone', wagtail.blocks.CharBlock(form_classname='phone_link', label='Phone', max_length=30, required=False)), ('new_window', wagtail.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))], closed=True, label=' ', max_length=255, required=True)), ('classes', wagtail.blocks.CharBlock(help_text='Дополнительные CSS классы.                    Вводятся через пробел', label='Дополнительные классы', max_length=255, required=False))])), ('documents', wagtail.blocks.StructBlock([('documents', wagtail.blocks.StreamBlock([('document', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(label='Название документа', max_length=255, required=True)), ('file', wagtail.documents.blocks.DocumentChooserBlock(label='Файл', required=True))], required=True))], help_text='Максимальное количество документов 10', label='Документы', max_num=10))]))], help_text='Максимальное количество документов 10', label='Контент', max_num=10))]))], blank=True, use_json_field=True, verbose_name='Page body')),
                ('date_published', models.DateField(blank=True, null=True, verbose_name='Date article published')),
                ('image', models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блог',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='BlogGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='blog.blogpage')),
            ],
            options={
                'verbose_name': 'Галерея блога',
                'verbose_name_plural': 'Галерея блога',
            },
        ),
    ]