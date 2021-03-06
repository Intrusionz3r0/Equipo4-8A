function validarDatosEdificio(){
    var formDatos={};
    var mensaje="";
    var aux=true;
    formDatos[0]=document.getElementById("NombreEdif").value;
    formDatos[1]=document.getElementById("DescripcionEdif").value;
    formDatos[2]=document.getElementById("TipoEdif").value;
    

    for(const key in formDatos){
        if(formDatos[key]==""){
            mensaje=mensaje+"Varios campos estan vacios. \n\n"
            aux=false;
            break;
        }
    }

    if(!validarDescripcion(formDatos[0])){
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
        document.getElementById("btnComprobarEdif").style.display='block';
        document.getElementById("btnRegEdif").style.display='none';
    }else{
        var modal = $('#errorModal')
        modal.find('.modal-title').text("Error")
        modal.find('.modal-body').text(mensaje)
        modal.modal('show')
    }


}

function validarNombre(algo){
    var regex = /^\w{8,}/                                                   
    var response = regex.test(algo)                                                           
    return response;  
}

function validarDescripcion(algo){
    var regex = /^\w{8,}/                                                   
    var response = regex.test(algo)                                                           
    return response; 
}

function validarTipo(algo){
    var regex = /^\w{8,}/                                                  
    var response = regex.test(algo)                                                           
    return response; 
}