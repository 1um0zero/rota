import json
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from core.forms.billing import BillingForm
from core.models import Order, Subscription, UserProfile, Contest, Product
from core.pagseguro import PagSeguro


def index(request):
    product_id = request.GET.get('id')
    subscription_data = {}

    is_seminario = product_id == '3'
    msg = request.session.get('msg', '')
    request.session['msg'] = ''
    msg_class = request.session.get('msg_class', '')
    request.session['msg_class'] = ''

    if not product_id:
        products = Product.objects.filter(is_enabled=True).order_by('position')
        return render(request, 'core/billing.html', {
            'title': 'Planos e preços',
            'products': products,
            'msg_class': msg_class,
            'msg': msg,
        })

    if not request.user.is_authenticated:
        return redirect('/entrar')

    product = Product.objects.get(pk=product_id)
    subscription = None
    
    if 'subscription' in request.session:
        subscription = Subscription.objects.get(pk=request.session['subscription_id'])
    else:
        _subscription = Subscription.objects.filter(
            user_id=request.user.id).order_by('-created_at')
        if _subscription:
            subscription = _subscription[0]

    if subscription:
        address = json.loads(subscription.data)
    else:
        address = {
            'address': 'Av. Brigadeiro Faria Lima',
            'address_number': '1384',
            'address_complement': '',
            'address_neighborhood': 'Jardim Paulistano',
            'address_city': 'São Paulo',
            'address_state': 'SP',
            'cep': '01452002',
        }

    if request.get_host() == 'localhost:8000':
        environment = 'sandbox'
    else:
        environment = 'production'

    ps = PagSeguro(environment=environment)
    form = BillingForm()

    # tentativa de pagamento
    if request.POST:
        user_profile = UserProfile.objects.get(user_id=request.user.id)
        payment_method = request.POST.get('payment_method')
        sender_hash = request.POST.get('sender_hash')
        cpf = request.POST.get('cpf').replace('.', '').replace('-', '')
        data_desejada =  None

        order_id = None
        if 'order_id' in request.session and request.session['order_id']:
            order_id  = request.session['order_id']

        if product.id == 3:
            data_desejada = request.POST.get('data_desejada')
            if data_desejada not in ['04', '05', '06']:
                data_desejada = '04'

        # cartão de crédito
        if payment_method == '0':
            installments = request.POST.get('installments').split('x')

            form = BillingForm(request.POST)

            card_token = request.POST['card_token']
            birthdate = request.POST['birthdate'].replace('.', '').replace('-', '')
            
            if  not order_id:
                order = Order(
                    user_id = request.user.id,
                    product_id = product.id,
                    price = product.price,
                    card_brand = request.POST['brand'],
                    card_end = request.POST['card_number'][-4:],
                    parcelas = installments[0],
                    valor_parcela = installments[1],
                    total_prazo = installments[2],
                    data_desejada = data_desejada
                )

                order.save()
                request.session['order_id'] = order.id

            else:
                order = Order.objects.get(pk=order_id)
                order.product_id = product.id
                order.price = product.price
                order.card_brand = request.POST['brand']
                order.card_end = request.POST['card_number'][-4:]
                order.parcelas = installments[0]
                order.valor_parcela = installments[1]
                order.total_prazo = installments[2]
                order.data_desejada = data_desejada
                order.link_boleto = None
                order.payment_method = 0
                order.save()

            res = ps.new_credit_card_order(
                order,
                user_profile,
                card_token,
                sender_hash,
                cpf,
                birthdate,
                address,
                installments[0],
                installments[1],
            )

        # boleto
        elif payment_method == '1':
            if not order_id:
                order = Order(
                    user_id = request.user.id,
                    product_id = product.id,
                    price = product.price,
                    payment_method = 1,
                    data_desejada = data_desejada
                )
                order.save()
                request.session['order_id'] = order.id

            else:
                order = Order.objects.get(pk=order_id)
                order.user_id = request.user.id
                order.product_id = product.id
                order.price = product.price
                order.data_desejada = data_desejada
                order.card_brand = None
                order.card_end = None
                order.parcelas = 1
                order.valor_parcela = None
                order.total_prazo = None
                order.payment_method = 1

            res = ps.new_boleto_order(
                order,
                user_profile,
                sender_hash,
                cpf,
                address,
            )
            print(res)

            if res.get('link'):
                order.link_boleto = res.get('link')
                order.save()
            

        if res['success']:
            order.error = None
            request.session['order_id'] = None
        else:
            order.error = res['error']

        order.save()

        response = HttpResponse(json.dumps(res))
        return response


    return render(request, 'core/billing.html', {
        'title': 'Pagamento',
        'form': form,
        'session_id': ps.session_id,
        'product_id': product_id,
        'product': product,
        'msg_class': msg_class,
        'msg': msg,
        'environment': environment,
        'is_seminario': is_seminario,
    })


def create_payment(request, subscription_id):
    # subscription = Subscription.objects.get(pk=subscription_id,
        # user_id=request.user.id)
    # order = Order(user_id=request.user.id,
                  # subscription_id=subscription.id,
                  # price=1)

    # order.save()
    # request.session['order_id'] = order.id
    return redirect('/planos-e-precos')


def confirmation(request):
    return render(request, 'core/payment_confirmation.html', {
        'title': 'Obrigado!'
    })


@csrf_exempt
def notification(request):
    if request.POST:
        ps = PagSeguro()
        notification = ps.read_notification(request.POST['notificationCode'])
        order = Order.objects.get(pk=notification.get('reference'))
        order.status = notification.get('status')
        order.save()

    return HttpResponse('ok')

