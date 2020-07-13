import re
import requests


class PagSeguro:
    
    session_id = None

    def __init__(self, session_id=None, environment='production'):
        
        self.environment =  environment

        if environment == 'production':
            self.url = 'https://ws.pagseguro.uol.com.br/v2/'
            self.email = 'puget@uol.com.br'
            self.token = '4bd0cd86-4a11-473c-9fc0-98b778567c41159187e1426db185f140b2e1f4b1272d0b3a-220a-4a00-b34d-4e9bb12e6be4'

        else:
            # sandbox
            self.url = 'https://ws.sandbox.pagseguro.uol.com.br/v2/'
            self.email = 'puget@uol.com.br'
            self.token = '4DEE09B7702A443DA46B129C84E33674'

        self.session_id = session_id if session_id else self.new_session()

    def get_credentials(self):
        return '?email={email}&token={token}'.format(
            email=self.email,
            token=self.token
        )

    def new_session(self):
        url = self.url + 'sessions' + self.get_credentials()

        req = requests.post(url)
        session_id = re.sub('.*<id>(.*)</id>.*', r'\1', req.text)
        return session_id

    def new_credit_card_order(
            self,
            order,
            user_profile,
            card_token,
            sender_hash,
            cpf,
            nascimento,
            address,
            installment_quantity,
            installment_amount,
            ):
        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        if self.environment == 'production':
            user_email = order.user.email
        else:
            user_email = 'c45534444352796152478@sandbox.pagseguro.com.br'

        data = (
            'paymentMode=default'
            '&paymentMethod=creditCard'
            '&notificationURL=https://www.rotafestival.com/notificacao'
            '&currency=BRL'
            '&extraAmount=0.00'
            '&shippingAddressRequired=false'

            '&reference=' + str(order.id) +

            '&itemId1=' + str(order.product.id) +
            '&itemDescription1=' + order.product.name +
            '&itemAmount1=' + ('%.2f' % order.price) +
            '&itemQuantity1=1'

            '&senderName=' + order.user.first_name +
            '&senderCPF=' + cpf +
            '&senderAreaCode=' + user_profile.ddd +
            '&senderPhone=' + user_profile.phone.replace('-', '') +
            '&senderEmail=' + user_email +
            '&senderHash=' + sender_hash +

            '&creditCardToken=' + card_token +
            '&creditCardHolderName=' + order.user.first_name +
            '&creditCardHolderCPF=' + cpf +
            '&creditCardHolderBirthDate=' + nascimento +
            '&creditCardHolderAreaCode=' + user_profile.ddd +
            '&creditCardHolderPhone=' + user_profile.phone.replace('-', '') +

            '&installmentQuantity=' + installment_quantity +
            '&installmentValue=' + ('%.2f' % float(installment_amount)) +

            '&billingAddressStreet=' + address['address'] +
            '&billingAddressNumber=' + address['address_number'] +
            '&billingAddressComplement=' + address['address_complement'] +
            '&billingAddressDistrict=' + address['address_neighborhood'] +
            '&billingAddressPostalCode=' + address['cep'] +
            '&billingAddressCity=' + address['address_city'] +
            '&billingAddressState=' + address['address_state'] +
            '&billingAddressCountry=BRA'
        )

        url = (
            self.url + 'transactions'
            + self.get_credentials()
        )

        req = requests.post(url, headers=headers, data=data)
        return self.check_response(req.text)

    def new_boleto_order(self, order, user_profile, sender_hash, cpf, address):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        if self.environment == 'production':
            user_email = order.user.email
        else:
            user_email = 'c45534444352796152478@sandbox.pagseguro.com.br'

        data = (
            'paymentMode=default'
            '&paymentMethod=boleto'
            '&notificationURL=https://www.rotafestival.com/notificacao'
            '&currency=BRL'
            '&extraAmount=0.00'
            '&shippingAddressRequired=false'

            '&reference=' + str(order.id) +

            '&itemId1=' + str(order.product.id) +
            '&itemDescription1=' + order.product.name +
            '&itemAmount1=' + ('%.2f' % order.price) +
            '&itemQuantity1=1'

            '&senderName=' + order.user.first_name +
            '&senderCPF=' + cpf +
            '&senderAreaCode=' + user_profile.ddd +
            '&senderPhone=' + user_profile.phone.replace('-', '') +
            '&senderEmail=' + user_email +
            '&senderHash=' + sender_hash +

            '&installmentQuantity=1'
            '&installmentValue=' + ('%.2f' % order.price) +

            '&billingAddressStreet=' + address['address'] +
            '&billingAddressNumber=' + address['address_number'] +
            '&billingAddressComplement=' + address['address_complement'] +
            '&billingAddressDistrict=' + address['address_neighborhood'] +
            '&billingAddressPostalCode=' + address['cep'] +
            '&billingAddressCity=' + address['address_city'] +
            '&billingAddressState=' + address['address_state'] +
            '&billingAddressCountry=BRA'
        )

        url = (
            self.url + 'transactions'
            + self.get_credentials()
        )

        req = requests.post(url, headers=headers, data=data)
        return self.check_response(req.text)

    def read_notification(self, notification_code):
        url = ('https://ws.pagseguro.uol.com.br/v3/transactions/notifications/'
            + notification_code + self.get_credentials())

        req = requests.get(url)
        reference = int(re.sub('.*<reference>([0-9]+)</reference>.*', r'\1', req.text))
        status = int(re.sub('.*<status>([0-9]+)</status>.*', r'\1', req.text))

        res = {
            'reference': reference,
            'status': status,
        }
        return res
    
    def check_response(self, response):
        error = None
        success = True
        link = None
        image = None

        if '<error>' in response:
            error = re.sub(
                '.*<error><code>(.*)</code><message>(.*)</message></error>.*',
                r'\2',
                response,
            )
            success = False

        if '<paymentLink>' in response:
            link = re.sub('.*<paymentLink>(.*)</paymentLink>.*', r'\1',
                response)
            #if link:
                #image = self.get_boleto_image(link)

        return {
            'success': success,
            'error': self.translate(error),
            'link': link,
            'image': image,
        }

    def get_boleto_image(self, link):
        url = 'https://pagseguro.uol.com.br'
        req = requests.get(link)
        find = re.sub(
            '.*<div id="boleto-image-wrapper">.*<img src="(.*)" />.*',
            r'\1',
            req.text.replace('\n', '')
        )
        url += find

        return url

    def translate(self, error):
        msg = error
        if error:
            translations = {
                'sender may not have a negative balance in PagSeguro.' : 'Saldo negativo no PagSeguro.'
            }

            if error in translations:
                return translations[error]
            
            if 'credit card holder cpf invalid value' in error:
                msg = 'CPF inválido.'

            if 'sender cpf invalid value' in error:
                msg = 'CPF inválido.'

            if 'billing address postal code invalid value' in error:
                msg = 'CEP inválido.'

            if 'credit card holder birthdate invalid value' in error:
                msg = 'Data de nascimento inválida.'

            return msg
        return None

