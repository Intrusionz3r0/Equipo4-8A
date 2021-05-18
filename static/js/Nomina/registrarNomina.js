function comprobar(){


    DatosForm = {}
    mensaje = ""
    aux = true;

    DatosForm[0] = document.getElementById('id').value
    DatosForm[1] = document.getElementById('subtotal').value
    DatosForm[2] = document.getElementById('dretencion').value
    DatosForm[3] = document.getElementById('iretencion').value
    DatosForm[4] = document.getElementById('ptotal').value
    DatosForm[5] = document.getElementById('dbonos').value
    DatosForm[6] = document.getElementById('ibonos').value
    DatosForm[7] = document.getElementById('fpago').value

    

    if(!validarId(DatosForm[0])){
        mensaje = mensaje + "El Id del empleado no es correcto.  \n\n"
        aux =false;
    }
    if(!validarSubtotal(DatosForm[1])){
        mensaje = mensaje + "El subtotal no se encuentra bien definido.  \n\n"
        aux =false;
    }
    if(!validarDescripcionRetencion(DatosForm[2])){
        mensaje = mensaje + "La Descripcion de retencion no esta bien descrita.  \n\n"
        aux =false;
    }
    if(!validarImporteRetencion(DatosForm[3])){
        mensaje = mensaje + "El importe no se encuentra bien definido.  \n\n"
        aux =false;
    }
    if(!validarPagoTotal(DatosForm[4])){
        mensaje = mensaje + "El pago total no se encuentra bien definido.  \n\n"
        aux =false;
    }
    if(!validarDescripcionBonos(DatosForm[5])){
        mensaje = mensaje + "La Descripcion de Bonos no esta bien descrita.  \n\n"
        aux =false;
    }
    if(!validarImporteBonos(DatosForm[6])){
        mensaje = mensaje + "El importe no se encuentra bien definido.  \n\n"
        aux =false;
    }
    
    if(!validarFormaPago(DatosForm[7])){
        mensaje = mensaje + "La forma de pago no se encuentra bien definido.  \n\n"
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

function validarId(dato){                  
    var regex = /^\d/                                                  
    var response = regex.test(dato)                                                           
    return response;                                                                        
} 
function validarSubtotal(dato){                  
    var regex = /^\d/                                                  
    var response = regex.test(dato)                                                           
    return response;                                                                        
}
 
function validarDescripcionRetencion(valor){                  
    var regex = /^\w[a-zA-Z]/                                                  
    var response = regex.test(valor)                                                           
    return response;                                                                        
} 

function validarImporteRetencion(dato){                  
    var regex = /^\d/                                                  
    var response = regex.test(dato)                                                           
    return response;                                                                        
}

function validarPagoTotal(dato){                  
    var regex = /^\d/                                                  
    var response = regex.test(dato)                                                           
    return response;                                                                        
}

function validarDescripcionBonos(valor){                  
    var regex = /^\w[a-zA-Z]/                                                  
    var response = regex.test(valor)                                                           
    return response;                                                                        
} 

function validarImporteBonos(dato){                  
    var regex = /^\d/                                                  
    var response = regex.test(dato)                                                           
    return response;                                                                        
}

function validarFormaPago(dato){                  
    var regex = /^\w[a-zA-Z]/                                                  
    var response = regex.test(dato)                                                           
    return response;                                                                        
}

