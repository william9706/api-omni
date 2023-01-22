from django.db import models



class Country(models.Model):
    """ model for table country. """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)
    verbose_name = "Name of Country"

    def __str__(self):
        return self.name


class State(models.Model):
    """ model for table state """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=4)
    country = models.ForeignKey(
        Country,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "States"


class City(models.Model):
    """ model for table city """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=8)
    state = models.ForeignKey(
        State,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Citys"


class Store(models.Model):
    """ model for table store """
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)


class Client(models.Model):
    """ model for table client. """
    name = models.CharField(max_length=100)
    sumame = models.CharField(max_length=100)

    country = models.ForeignKey(
        Country,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    state = models.ForeignKey(
        State,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    city = models.ForeignKey(
        City,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    favorite_store = models.ForeignKey(
        Store,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Client"

