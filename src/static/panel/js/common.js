
function atualiza_notas(sub_id, campos_notas)
{   
  var total_valor = 0;
  var campos = document.getElementById('avaliacao_form_' + sub_id).elements;
  var tem_nota = false;

  for (var i = 0, c; c = campos[i++];) {
      if (campos_notas.includes(c.name) && c.checked) {
          document.getElementById('nota_' + c.name + '_' + sub_id).innerHTML = c.value;
          total_valor += parseFloat(c.value);
          tem_nota = true;
      }
  }

  if (tem_nota) document.getElementById('nota_total_' + sub_id).innerHTML = total_valor;
}


function submete_avaliacao(sub_id, msg_indicados)
{
    var msg_temp = '';
    var indicados = JSON.parse(msg_indicados);
    var form = document.getElementById('avaliacao_form_' + sub_id);
    var elementos_form = document.getElementById('avaliacao_form_' + sub_id).elements;
    var campos = new Set();
    for (var i = 0, e; e = elementos_form[i++];) { 
        campos.add(e.name);
    }

    console.log(campos);
    for (let c of campos) {        
        if (Object.keys(indicados).includes(c) && form[c].value == 'sim') {
            for (let m of indicados[c]) {
                msg_temp += m + '\n';
            }
        }
    }
    
    if (msg_temp != '') {
        alert('Você atingiu o limite máximo de indicações nas categorias abaixo. Se quiser mudar sua indicação, desmarque as indicações que fez anteriormente: \n\n' + msg_temp);
        return;
    }

    form.submit();
}

function atualiza_notas_roteiro(sub_id) {
    atualiza_notas(sub_id, ['estrutura_narrativa','trama','personagens','dialogos','originalidade']);
}

function atualiza_notas_lab(sub_id) {
    atualiza_notas(sub_id, ['clareza', 'originalidade', 'universo', 'personagens', 'atualidade']);
}

function atualiza_notas_mostra(sub_id) {
    atualiza_notas(sub_id, ['estrutura_narrativa','trama','personagens','dialogos','originalidade']);
}

function promover()
{
    var selecionados = [];
    var sel_campo = document.getElementById('selecionados');
    var projetos = document.getElementsByName('projetos');
    for (var i = 0; i < projetos.length; i++){
        if ( projetos[i].checked ) {
            selecionados.push(projetos[i].value);
        }
    }

    if (document.getElementById('step').value == '' || document.getElementById('step').value == '0') {
        alert('Etapa deve ser maior que zero!');
        return;
    }

    if (document.getElementById('qtd_grupos').value == '' || document.getElementById('qtd_grupos').value == '0') {
        alert('Quantidade de grupos deve ser maior que zero!');
        return;
    }

    if (document.getElementById('grupo_prefixo').value == '') {
        alert('Prefixo não pode ser vazio!');
        return;
    }

    if (selecionados.length == 0) {
        alert('Nenhum projeto selecionado!');
        return;
    }

    sel_campo.value = selecionados;

    document.getElementById('promover_form').submit();
}


function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }


function toogle_juri_popular(contest_id, valor)
{
    request = $.ajax({
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        url: "/painel/toogle_juri_popular",
        type: "post",
        data: {contest_id: contest_id, valor: valor}
    });

    // Callback handler that will be called on success
    request.done(function (response, textStatus, jqXHR){
        // Log a message to the console
        console.log("Hooray, it worked! " + textStatus);
    });

    // Callback handler that will be called on failure
    request.fail(function (jqXHR, textStatus, errorThrown){
        // Log the error to the console
        console.error(
            "The following error occurred: "+
            textStatus, errorThrown
        );
    });

    // Callback handler that will be called regardless
    // if the request failed or succeeded
    request.always(function () {
        //
    });
}