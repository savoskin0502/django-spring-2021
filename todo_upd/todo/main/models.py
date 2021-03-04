from django.db import models
from django.utils import timezone


class TaskList(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False,
                             default='Worker', verbose_name='Заголовок')

    class Meta:
        verbose_name = 'Список задач'
        verbose_name_plural = 'Список задач'


class Task(models.Model):
    title = models.CharField(max_length=250, null=False,
                             blank=False, verbose_name='Заголовок')
    created = models.DateField(default=timezone.now, null=False,
                               blank=True, verbose_name='Дата создания')
    due_on = models.DateField(null=False, blank=False, verbose_name='Дедлайн')
    owner = models.CharField(max_length=250, null=False, blank=True,
                             default='admin', verbose_name='Владелец')
    mark = models.BooleanField(default=False, verbose_name='Статус')
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE,
                                  blank=False, null=False,
                                  related_name='tasks', verbose_name='Задачи',)

    class Meta:
        ordering = ['mark', 'due_on', '-created']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
