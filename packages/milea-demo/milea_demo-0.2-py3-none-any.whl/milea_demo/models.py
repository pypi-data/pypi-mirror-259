from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from milea_base.models import MileaModel
from milea_notify.utils import Notify


class DefaultModal(MileaModel):

    OBJ_VERB_TAG = "KN"

    TYP_CHOICES = [
        ('choice1', "Choice1"),
        ('choice2', "Choice2"),
        ('choice3', "Choice3"),
    ]

    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=128, unique=True)
    url = models.URLField(max_length=128, blank=True)
    text = models.TextField(blank=True)
    decimal = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='demo/image/', default='no-img.jpg', blank=True)
    date = models.DateField()
    time = models.TimeField()
    timestamp = models.DateTimeField()
    boolean = models.BooleanField(default=False)
    radio = models.CharField(max_length=64, choices=TYP_CHOICES)
    tags = models.ManyToManyField('Tag', blank=True)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    progress = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = "Default Model"
        verbose_name_plural = "Default Models"


class Position(MileaModel):
    default_model = models.ForeignKey('milea_demo.DefaultModal', on_delete=models.CASCADE)
    pos = models.PositiveIntegerField()
    title = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=16, decimal_places=2, default=1)
    price = models.DecimalField(max_digits=16, decimal_places=2)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['pos']


class Tag(MileaModel):
    tag_name = models.CharField(max_length=64)

    def __str__(self):
        return str(self.tag_name)


@receiver(post_save, sender=DefaultModal)
def create_manager_notification(sender, instance, created, **kwargs):
    if created:
        notify = Notify(
            user=instance.manager,
            title="Neues Demo Object",
            content="Das ist eine Demo Benachrichtigung, da kannst sie ignorieren :)",
            url=instance.get_admin_url(),
        )
        notify.to_browser()
