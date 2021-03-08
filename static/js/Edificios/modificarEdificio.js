function validarDatosEdificio(){
    var formDatos={};
    var mensaje="";
    var aux=true;
    formDatos[0]=document.getElementById("NombreEdif");
    formDatos[1]=document.getElementById("DescripcionEdif");
    formDatos[2]=document.getElementById("TipoEdif");
    formDatos[3]=document.getElementById("EstadoEdif");

    for(const key in formDatos){
        if(formDatos[key]==""){
            mensaje=mensaje+"Varios campos estan vacios. \n\n"
            aux=false;
            break;
        }
    }

    if(!validarNombre(formDatos[0])){
        mensaje=mensaje+" *Nombre no valido \n\n"
        aux=false;
    }

    if(!validarDescripcion(formDatos[1])){
        mensaje=mensaje+" *Descripcion Erronea \n\n"
        aux=false;
    }

    if(!validarTipo(formDatos[2])){
        mensaje=mensaje+" *Tipo no valido \n\n"
        aux=false;
    }

    

    if(aux){
        Mostrar("btnRegEdif")
        Ocultar("btnComprobarEdif")
    }else{
        var modal = $('#errorModal')
        modal.find('.modal-title').text("Error")
        modal.find('.modal-body').text(mensaje)
        modal.modal('show')
    }


}

function validarNombre(valor){
    var regex = /^\w[a-zA-Z]/                                                  
    var response = regex.test(valor)                                                           
    return response;  
}

function validarDescripcion(valor){
    var regex = /^\w[a-zA-Z]/                                                  
    var response = regex.test(valor)                                                           
    return response; 
}

function validarTipo(valor){
    var regex = /^\w[a-zA-Z]/                                                  
    var response = regex.test(valor)                                                           
    return response; 
}



function Mostrar(objeto){
document.getElementById(objeto).style.display="block";
}

function Ocultar(objeto){
document.getElementById(objeto).style.display="none";
}