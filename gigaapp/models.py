from django.db import models


class Volunteer(models.Model):
    uid = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=256, verbose_name='Имя', blank=True)
    surname = models.CharField(max_length=256, verbose_name='Фамилия', blank=True)
    email = models.CharField(max_length=256, verbose_name='Email', blank=True)
    phone = models.CharField(max_length=128, verbose_name='Телефон', blank=True)
    city = models.CharField(max_length=256, verbose_name='Город', blank=True)
    company = models.CharField(max_length=256, verbose_name='Компания', blank=True)
    position = models.CharField(max_length=256, verbose_name='Позиция', blank=True)
    consent = models.BooleanField(verbose_name='Согласие на ОПД', blank=True)

    competence = models.ForeignKey('Competence', on_delete=models.DO_NOTHING, verbose_name='Выбранная компетенция',
                                   blank=True, null=True)
    contacts = models.ManyToManyField('Contact', verbose_name='Полученные контакты', blank=True)
    resource = models.ForeignKey('Resource', verbose_name='Направление развития', blank=True, null=True,
                                 on_delete=models.DO_NOTHING)
    curator = models.ForeignKey('Curator', verbose_name='Cоциальная адаптация молодежи', null=True, blank=True,
                                on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Волонтер'
        verbose_name_plural = 'Волонтеры'


class Competence(models.Model):
    competence_name = models.CharField(max_length=128, verbose_name='Название компетенции:')
    box1 = models.TextField(blank=True, verbose_name='Ты можешь считать ее развитой, если')
    box2 = models.TextField(blank=True, verbose_name='Задуматься о том, чтобы подтянуть эту компетенцию, стоит, если')
    box3 = models.TextField(blank=True, verbose_name='Вариант развития №1:')
    box4 = models.TextField(blank=True, verbose_name='Вариант развития №2:')
    box5 = models.TextField(blank=True, verbose_name='Вариант развития №3:')
    box6 = models.TextField(blank=True, verbose_name='Вариант развития №4:')
    box7 = models.TextField(blank=True, verbose_name='Вариант развития №5:')

    def __str__(self):
        return self.competence_name

    class Meta:
        verbose_name = 'Компетенция'
        verbose_name_plural = 'Компетенции'


class Contact(models.Model):
    leader_name = models.TextField(max_length=256, verbose_name='Имя лидера', blank=True)
    city = models.TextField(max_length=256, verbose_name='Город', blank=True, null=True)
    company = models.TextField(max_length=256, verbose_name='Название компании', blank=True)
    position = models.TextField(max_length=256, verbose_name='Должность', blank=True)
    phone = models.TextField(max_length=256, verbose_name='Телефон', blank=True)
    email = models.TextField(max_length=128, verbose_name='Email', blank=True)

    def __str__(self):
        return self.leader_name

    class Meta:
        verbose_name = 'Контакт лидера'
        verbose_name_plural = 'Контакты лидеров'
        ordering = ('city',)


class Resource(models.Model):
    course = models.CharField(max_length=128, verbose_name='Направление')
    contact = models.TextField(verbose_name='Контакты')

    def __str__(self):
        return self.course

    class Meta:
        verbose_name = 'База ресурсов'
        verbose_name_plural = 'База ресурсов'


class Curator(models.Model):
    city = models.CharField(max_length=128, verbose_name='Регион')
    course = models.CharField(max_length=128, verbose_name='Направление')
    contact = models.TextField(verbose_name='Контакты в регионе')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Cоциальная адаптация молодежи'
        verbose_name_plural = 'Cоциальная адаптация молодежи'
        ordering = ('city',)
