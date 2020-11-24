

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

function regulamento(){
    $([document.documentElement, document.body]).animate({
        scrollTop: $("#h4_regulamento").offset().top - 100
    }, 150);
  }

function convidados(){
    $([document.documentElement, document.body]).animate({
        scrollTop: $("#h4_convidados").offset().top - 100
    }, 150);
}

function inscricao(){
    $([document.documentElement, document.body]).animate({
        scrollTop: $("#h4_inscricao").offset().top - 100
    }, 150);
}

function juri_popular(){
    $([document.documentElement, document.body]).animate({
        scrollTop: $("#h4_juri_popular").offset().top - 100
    }, 150);
  }

function votar(sub_id, cat_id)
{    
    var ip = '';

    $.ajax ({
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        type: "GET",
        url: "https://ipgeolocation.abstractapi.com/v1/?api_key=6df09b35db2d49a0b66f3c13d91ded09",
        success: function(response) { 
            ip = response.ip_address;
            //ip = Math.floor(Math.random() * 1000000).toString();

            request = $.ajax({
                headers: { "X-CSRFToken": getCookie("csrftoken") },
                url: "/votar",
                type: "post",
                data: {subscription_id: sub_id, categoria_id: cat_id, ip: ip}
            });
        
            // Callback handler that will be called on success
            request.done(function (response, textStatus, jqXHR){
                
                if (response == 'OK')
                    alert('Voto computado com sucesso!');
                else
                    alert('Você já votou nesta categoria!');
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
    });
  
}