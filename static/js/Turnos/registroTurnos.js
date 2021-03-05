function comprobar(){

    DatosForm = {}
    mensaje = ""
    aux = true;

    DatosForm[0] = document.getElementById('nombre').value
    DatosForm[1] = document.getElementById('hentrada').value
    DatosForm[2] = document.getElementById('hsalida').value
   

    if(!validarNombre(DatosForm[0])){
        mensaje = mensaje + "El nombre del turno no es correcto.  \n\n"
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

function validarNombre(valor){                  
    var regex = /^\w[a-zA-Z]/                                                  
    var response = regex.test(valor)                                                           
    return response;                                                                        
}    