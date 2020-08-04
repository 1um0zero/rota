
function atualiza_notas_roteiro(sub_id)
{ 
  var campos_notas = ['estrutura_narrativa','trama','personagens','dialogos','originalidade'];
  total_valor = 0;      
  campos = document.getElementById('avaliacao_form_' + sub_id).elements;
  for (var i = 0, c; c = campos[i++];) {
      if (campos_notas.includes(c.name) && c.checked) {
          document.getElementById('nota_' + c.name + '_' + sub_id).innerHTML = c.value;
          total_valor += parseFloat(c.value);
      }
  }

  document.getElementById('nota_total_' + sub_id).innerHTML = total_valor;
}


function submete_avaliacao_roteiro(sub_id, msg_roteiro, msg_personagem, msg_dialogo, msg_cabiria)
{    
    form = document.getElementById('avaliacao_form_' + sub_id);
    msg = '';
    if (form.indica_roteiro.value == 'sim' && msg_roteiro != '')
        msg += msg_roteiro + '\n';
    if (form.indica_personagem.value == 'sim' && msg_personagem != '')
        msg += msg_personagem + '\n';
    if (form.indica_dialogo.value == 'sim' && msg_dialogo != '')
        msg += msg_dialogo + '\n';
    if (form.premio_cabiria.value == 'sim' && msg_cabiria != '')
        msg += msg_cabiria + '\n';
    
    if (msg != '') {
        alert('Você só pode indicar um roteiro para cada categoria. Se quiser mudar sua indicação, desmarque as indicações que fez anteriormente: \n\n' + msg);
        return;
    }

    form.submit();
}