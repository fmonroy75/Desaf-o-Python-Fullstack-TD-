$('#enviar_correo').click(function () {

    alert("El correo fue enviado correctamente...")
})

//$('#ingredientes').dblclick(function(){

$("#ingredientes" ).on( "dblclick", function() {
    var color = $("#ingredientes").css("color");
    //alert(color=="rgb(33, 37, 41)");
    if(color=="rgb(33, 37, 41)"){
        $(this).css({
            "color": "red",
        });
    }else{
        $(this).css({
            "color": "black",
        });
    }    
});



$("#preparacion" ).on( "dblclick", function() {
    var color = $("#preparacion").css("color");
    //alert(color=="rgb(33, 37, 41)");
    if(color=="rgb(33, 37, 41)"){
        $(this).css({
            "color": "red",
        });
    }else{
        $(this).css({
            "color": "black",
        });
    }    
});
//};

$('.card-title').click(function(){
    $('.recetas-relacionadas p').toggle("hide");
})