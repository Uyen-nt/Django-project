# Generated by Django 4.2.16 on 2024-11-07 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ('exercises', '0001_initial'),  # Đảm bảo 'exercises' được chạy trước
    ('quiz', '0003_remove_studentanswer_selected_option_and_more'),
]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='exercises',
            field=models.ManyToManyField(blank=True, related_name='assessment', to='exercises.exercise'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='questions',
            field=models.ManyToManyField(blank=True, related_name='assessment', to='quiz.question'),
        ),
    ]
