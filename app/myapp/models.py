from django.db import models


class Person(models.Model):
    SHIRT_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )
    # choices의 DB값은 tuple의 0번째 값
    # tuple의 1번째 값을 가져오고 싶으면, get_FOO_display()를 사용
    #   FOO: Model의 choices를 가진 field명
    shirt_size = models.CharField(
        max_length=1, choices=SHIRT_SIZE, help_text='셔츠 사이즈이다')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
