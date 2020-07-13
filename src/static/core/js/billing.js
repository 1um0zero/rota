window.paymentError = null;
window.senderHash = null;
window.cardBrand = null;
window.cardInstallments = null;

// PagSeguro integration
function requestSenderHash(){
    PagSeguroDirectPayment.onSenderHashReady(function(response){
        if (response.status == 'error') {
            console.error('unable to get sender hash', response);
        } else {
            window.senderHash = response.senderHash;
        }
    });
}

function getBrand(cardNumber) {
    $('#payment_error').hide();
    if (cardNumber){
        PagSeguroDirectPayment.getBrand({
            cardBin: cardNumber,
            success: function(response){
                window.cardBrand = response.brand.name;
                $('#brand').val(response.brand.name);
                getInstallments(response.brand.name, window.price);
            },
            error: function(response){
                console.log('invalid card brand', response);
                payment_error('Cartão de crédito inválido.');
            }
        });
    }
}

function getInstallments(brand, price, fn) {
    window.cardInstallments = null;
    $('#select_installments').attr('readonly', true);
    $('#select_installments').empty();
    let opt = $('<option>');
    opt.text('carregando opções de parcelamento...');
    opt.appendTo($('#select_installments'));

    PagSeguroDirectPayment.getInstallments({
        brand: brand,
        amount: price,
        success: function(response){
            window.cardInstallments = response.installments[brand];
            $('#select_installments').empty();
            cardInstallments.forEach(function(el){
                let text = (el.quantity + 'x de ' + reais(el.installmentAmount));
                text += ' - Total: ' + reais(el.totalAmount);
                let opt = $('<option>');
                opt.val(el.quantity + 'x' +  el.installmentAmount  + 'x' + el.totalAmount);
                opt.addClass('installments_' + el.quantity).text(text);
                opt.appendTo($('#select_installments'));
            });
        },
        error: function(response) {
            console.error('unable to load installments', response);
        },
    });
}

function createCardToken(){
    console.log('creating card token');
    var card_number = $('#id_card_number').val();
    var cvv = $('#id_card_code').val();
    var exp_month = $('#id_card_date').val().split('/')[0];
    var exp_year = '20' + $('#id_card_date').val().split('/')[1];

    PagSeguroDirectPayment.createCardToken({
        cardNumber: card_number,
        brand: window.cardBrand,
        cvv: cvv,
        expirationMonth: exp_month,
        expirationYear: exp_year,

        success: function(response) {
            $('#card_token').val(response.card.token);
            $('#sender_hash').val(window.senderHash);
            submit_cc_form();
        },

        error: function(response) {
            console.error('unable to create card token', response);
            payment_error('Dados do cartão de crédito inválidos.')
        },
    });
}
////

function reais(num){
    let res = '';
    let _n = String(num).split('.');
    res = 'R$ ' + _n[0] + ',';
    if (_n.length === 1) res += '00';
    else if (_n[1].length === 1) res += _n[1] + '0';
    else res += _n[1];
    return res;
}

function paymentMethodSelector(){
    $('#payment_methods label').each(function(n, el){
        $(el).click(function() {
            let val = $(this).find('input').val();
            if (val == 0) {
                $('#box_credit_card').show();
                $('#box_boleto').hide();
            } else if (val == 1) {
                $('#box_credit_card').hide();
                $('#box_boleto').show();
            }
        });
    });
    $('input[name=payment_method]').eq(0).click();
}

function payment_error(error){
    $('#payment_error .error').text(error);
    $('#payment_error').show();
    toggleFormButton(true);
}

function toggleFormButton(status){
    let el = $('#form_billing button[type=submit]');
    if (status){
        el.addClass('action').removeClass('grey').text('Efetuar pagamento').attr('disabled', false);
    } else {
        el.removeClass('action').addClass('grey').text('Processando pagamento, aguarde...').attr('disabled', true);
        el[0].blur();
    }
}

function submit_cc_form(){
    $('#input_data_desejada').val($('#data_desejada').val());
    $.getJSON({
        method: 'post',
        url: window.location.href,
        data: $('#form_billing').serialize(),
        success: function(r){
            if (r.success){
                window.location = '/confirmacao-pagamento';
            } else {
                if (r.error === 'sender hash is required.'){
                    requestSenderHash();
                }
                payment_error(r.error);
            }
        },
        error: function(){
            console.error('post error');
        }
    });
}

$(document).ready(function(){
    // starting session
    PagSeguroDirectPayment.setSessionId(session_id);
    requestSenderHash();

    // payment method selection
    paymentMethodSelector();
    
    // getting card brand
    $('#id_card_number').blur(function(){
        let number = $(this).val();
        if (number){
            getBrand(number);
        }
    });
    $('#id_card_number').blur();

    // credit card submit
    $('#form_billing').submit(function(ev){
        ev.preventDefault();
        toggleFormButton(false);
        $('#payment_error').hide();

        
        createCardToken();
    });

    // boleto submit
    $('#form_boleto').submit(function(ev){
        ev.preventDefault();

        $('.boleto_error').hide();
        $('#sender_hash_boleto').val(window.senderHash);
        $('#input_data_desejada_boleto').val($('#data_desejada').val());

        $.getJSON({
            url: window.location.href,
            method: 'post',
            data: $('#form_boleto').serialize(),
            success: function(r){
                if (r.error){
                    $('.boleto_error').show();
                    $('.boleto_error .errorlist li.err').remove();
                    $('<li class="err">').text(r.error).appendTo($('.boleto_error .errorlist'));
                    $('#btn_gerar_boleto').addClass('action').removeClass('grey');
                    $('#btn_gerar_boleto').val('Gerar boleto').attr('disabled', false);

                } else {
                    if (r.link){
                        //$('#boleto_image img').attr('src', r.image);
                        //$('#boleto_image img').attr('alt', 'Link para o boleto');
                        //$('#boleto_image').attr('href', r.link).show();
                        $('#boleto_print').attr('href', r.link).show();
                        $('#hide_cpf').hide();
                        $('#sucesso_boleto').show();
                        $('#btn_gerar_boleto').hide();
                    }
                }
            }
        });

        $('#btn_gerar_boleto').removeClass('action').addClass('grey');
        $('#btn_gerar_boleto').val('Aguarde, gerando boleto...').attr('disabled', true);
    });

    // masks
    $('#id_card_number').mask('00000000000000000000');
    $('#id_card_date').mask('00/00');
    $('#id_cpf').mask('000.000.000-00');
    $('#id_cpf_boleto').mask('000.000.000-00');
    $('#id_birthdate').mask('00/00/0000');
});

