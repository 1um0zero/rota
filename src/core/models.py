import datetime
from hashlib import md5
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=100, null=True)
    ddd = models.CharField(max_length=2)
    phone = models.CharField(max_length=30)
    
    def get_name(self):
        return self.social_name if self.social_name else self.user.first_name


class Contest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    regulation = models.TextField(null=True)
    is_free = models.BooleanField(default=1)
    subscription_limit = models.IntegerField(default=0)
    subscription_open = models.BooleanField(default=0)
    url = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200, null=True)
    date = models.CharField(max_length=30, null=True)
    display_on_site = models.BooleanField(default=False)
    text_guest = models.CharField(max_length=100, null=True)
    has_subscription = models.BooleanField(default=1)
    email = models.CharField(max_length=100, null=True)
    subscription_start = models.DateTimeField(null=True)
    subscription_end = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.name

    def has_limit(self):
        subs = Subscription.objects.filter(contest_id=self.id).count()
        has = subs < self.subscription_limit
        if self.subscription_limit == 0:
            has = True
        return has


class CuradorGroup(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)


class Folder(models.Model):
    parent = models.ForeignKey('Folder', null=True, default=None,
        on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    data = models.TextField(null=True)
    status = models.IntegerField(default=0)
    group = models.ForeignKey(CuradorGroup, on_delete=models.DO_NOTHING,
        null=True, default=None)
    folder = models.ForeignKey(Folder, null=True, default=None,
        on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def get_status(self):
        statuses = {
            0: 'Em análise',
            1: 'Aprovada',
            2: 'Reprovada'
        }
        return statuses[self.status]

    @staticmethod
    def get_table():
        subscriptions = Subscription.objects.all().order_by('-created_at')
        for sub in subscriptions:
            orders = Order.objects.filter(subscription_id=sub.id)
            sub.payments = len(orders)
            payment_status = 0
            for order in orders:
                if payment_status != 3:
                    payment_status = order.status

            sub.payment_status = Order.get_status(payment_status)
        return subscriptions



class Page(models.Model):
    title = models.CharField(max_length=100)
    status = models.IntegerField()
    content = models.TextField(null=True)
    url = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    display_on_menu = models.BooleanField(default=False)
    fixed = models.BooleanField(default=False)


class PasswordRecoveryToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=32)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    @staticmethod
    def generate_token(user_id):
        salt = 'ROTA-#*&XWT%YN*(#BBN X*W$T#W*#W*&%NWNMB(Z*WTNW'
        _str = str(user_id) + str(datetime.datetime.now())
        token = md5((salt + _str).encode()).hexdigest()
        PasswordRecoveryToken(user_id=user_id, token=token).save()
        return token


class Short(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.datetime.now)


class Script(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    original_filename = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.datetime.now)


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=10, null=True, default=None)
    description = models.TextField()
    price = models.FloatField()
    price2 = models.FloatField(null=True, default=None)
    price2_date = models.CharField(max_length=30, null=True, default=None)
    is_enabled = models.BooleanField(default=0)
    url = models.CharField(max_length=100, null=True, default=None)
    position = models.IntegerField(null=True, default=0)

    def is_price2(self):
        if not self.price2:
            return False        
        date2 = datetime.datetime.strptime(self.price2_date, '%d/%m/%Y')        
        return datetime.datetime.now() >= date2
       

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    status = models.IntegerField(default=0)
    payment_method = models.IntegerField(default=0)
    error = models.CharField(max_length=250, null=True)
    card_brand = models.CharField(max_length=20, null=True)
    card_end = models.IntegerField(null=True)
    link_boleto = models.CharField(max_length=250, null=True, default=None)
    parcelas = models.IntegerField(null=True, default=1)
    valor_parcela = models.FloatField(null=True, default=None)
    total_prazo = models.FloatField(null=True, default=None)
    data_desejada = models.CharField(max_length=10, null=True, default=None)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    @staticmethod
    def get_status(status):
        statuses = {
            0: 'Pedido realizado',
            1: 'Aguardando pagamento',
            2: 'Em análise',
            3: 'Pagamento aprovado',
            4: 'Disponível',
            5: 'Em disputa',
            6: 'Devolvido',
            7: 'Cancelado',
            8: 'Gratuito',
        }
        return statuses.get(status)

    @staticmethod
    def get_payment_method(payment_method):
        methods = {
            0: 'Cartão de crédito',
            1: 'Boleto',
        }
        return method[payment_method]


class Role(models.Model):
    name = models.CharField(max_length=30)



class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, null=True, default=None)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    group = models.ForeignKey(CuradorGroup, on_delete=models.DO_NOTHING,
        null=True, default=None)


class Curador(models.Model):
    contest = models.ForeignKey(Contest, null=True, on_delete=models.DO_NOTHING, blank=True)
    name = models.CharField(max_length=250)
    picture = models.CharField(max_length=250, null=True, blank=True)
    bio = models.TextField(max_length=2000, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    category_order = models.IntegerField(null=True, blank=True, default=0)
    
    class Meta:
        ordering = ['category_order', 'name']

    def save(self, *args, **kwargs):
        if self.category == 'curador' or self.category == 'curadora':
            self.category_order = 0
        elif self.category == 'jurado' or self.category == 'jurada':
            self.category_order = 1
        super(Curador, self).save(*args, **kwargs)

