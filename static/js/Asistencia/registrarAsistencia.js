function comprobar(){

    DatosForm = {}
    mensaje = ""
    aux = true;

    
    DatosForm[0] = document.getElementById('observaciones').value
    

    if(!validarDescrip(DatosForm[0])){
        mensaje = mensaje + "Las Observaciones no estan bien descritas.  \n\n"
        aux =false;
    }

    for (const key in DatosForm) {
        if(DatosForm[key] == ""){
            mensaje = mensaje + "Algunos de los campos estan vacios \n\n"
            aux=false
            break
        }
    }

    
    if(aux){
        document.getElementById("btn-registrar").style.display = 'block';
        document.getElementById("btn-comprobar").style.display = 'none';

    }
    else{
        var modal = $('#errorModal')
        modal.find('.modal-title').text("Error")
        modal.find('.modal-body').text(mensaje)
        modal.modal('show')

    }

}

function validarDescrip(valor){                  
    var regex = /^\w[a-zA-Z]/                                                  
    var response = regex.test(valor)                                                           
    return response;                                                                        
}    




