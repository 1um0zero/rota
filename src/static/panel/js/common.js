
function atualiza_notas(sub_id, campos_notas)
{   
  var total_valor = 0;      
  var campos = document.getElementById('avaliacao_form_' + sub_id).elements;
  for (var i = 0, c; c = campos[i++];) {
      if (campos_notas.includes(c.name) && c.checked) {
          document.getElementById('nota_' + c.name + '_' + sub_id).innerHTML = c.value;
          total_valor += parseFloat(c.value);
      }
  }

  document.getElementById('nota_total_' + sub_id).innerHTML = total_valor;
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
            msg_temp += indicados[c] + '\n';            
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