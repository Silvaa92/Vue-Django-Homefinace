from django.db import models
from django.utils import timezone


TRANSACTION_TYPES = [
        ('INC', 'Income'),
        ('EXP', 'Expences'),
        ('TEC', 'Technical')
    ]

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    currency = models.ForeignKey('Currency', related_name='transactions', on_delete=models.PROTECT)
    trans_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    category = models.ForeignKey('Category', related_name='transactions', on_delete=models.PROTECT, blank=True, null=True)
    subcategory = models.ForeignKey('Subcategory', related_name='transactions', on_delete=models.PROTECT, blank=True, null=True)
    from_account = models.ForeignKey('Account', related_name="transactions_from_account", on_delete=models.PROTECT, blank=True, null=True)
    on_account = models.ForeignKey('Account', related_name="transactions_on_account", on_delete=models.PROTECT, blank=True, null=True)
    create_datetime = models.DateTimeField(default=timezone.now)
    place = models.ForeignKey('Place', related_name='transactions', on_delete=models.PROTECT, blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return '{}, {} {}, {}'.format(self.notes, 
                                        self.amount, 
                                        self.currency, 
                                        self.create_datetime
                                        )


class Account(models.Model):
    title = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    currency = models.ForeignKey('Currency', related_name='accounts', on_delete=models.PROTECT)
    notes = models.TextField(blank=True)
    create_datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}, {} {}'.format(self.title, self.amount, self.currency)


class Currency(models.Model):
    name = models.CharField(max_length=3)
    full_name = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.name)


class Category(models.Model):
    name = models.CharField(max_length=20)
    cat_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)

    def __str__(self):
        return '{}'.format(self.name)

class Subcategory(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.PROTECT)

    def __str__(self):
        return '{}, {}'.format(self.name, self.category)


class Place(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)
