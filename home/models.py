from django.db import models

class teachers(models.Model):
    bio = models.CharField('Ф.И.О', max_length=100)
    number = models.CharField('Номер телефона', max_length=13)
    couple = models.CharField('Какой предмет', max_length=15)
    description = models.CharField('Oписание', max_length=300)
    img = models.ImageField('Фотография', upload_to='post_image', null=True, blank=True)
    exp = models.IntegerField('Опыт работы')
    slug = models.SlugField(unique=True, max_length=200, auto_created=True)

    def __str__(self):
        return self.bio
