from django.conf import settings
from django.db import models
from django.utils import timezone


class TodoList(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False,
                             default='DefaultTitle', verbose_name='Title')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    class Meta:
        # db_table = 'TodoLists'
        verbose_name = 'TodoList'
        verbose_name_plural = 'TodoLists'


class Todo(models.Model):
    title = models.CharField(max_length=250, null=False,
                             blank=False, verbose_name='Title')
    created = models.DateField(default=timezone.now, null=False,
                               blank=True, verbose_name='Created at')
    due_on = models.DateField(null=False, blank=False, verbose_name='Deadline',
                              default=timezone.now)
    owner = models.CharField(max_length=250, null=False, blank=True,
                             verbose_name='Owner')
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                           on_delete=models.CASCADE)
    mark = models.BooleanField(default=False, verbose_name='Status')
    task_list = models.ForeignKey(TodoList, on_delete=models.CASCADE,
                                  blank=False, null=False,
                                  related_name='todos',
                                  verbose_name='TodoList')

    class Meta:
        # db_table = 'Todos'
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
