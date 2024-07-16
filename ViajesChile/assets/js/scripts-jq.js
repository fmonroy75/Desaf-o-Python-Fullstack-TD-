
//jq para ocultar
$('.card-title').click(function(){
    $('.destacados p').toggle("hide");
})

//jq para alert de que se envió un correo
$('#enviar_correo').click(function () {

    alert("El correo fue enviado correctamente...")
})



//js para colapsar menu
$(document).ready(function() {
    $('.nav-link').on('click', function() {
      $('.navbar-collapse').collapse('hide');
    });
  });