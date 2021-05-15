
var extValidas = [".jpg", ".jpeg",".png"];                                                                                                                                 
                                                                                                                                                               
function ValidarArchivo(oninput) { //Verifica las extenciones de lo archivos.                                                                                                                                                      
    if (oninput.type == "file") {  // S                                                                                                                                                           
        var nombre = oninput.value;                                                                                                                                   
         if (nombre.length > 0) {                                                                                                                                                              
            var bandera = false;                                                                                                                                               
            for (var j = 0; j < extValidas.length; j++) {                                                                                                                  
                var sCurExtension = extValidas[j];                              
                if (nombre.substr(nombre.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {                                         
                    bandera = true;                            
                    break;                                                                                                                                                                      
                }                                                                                                                                                                                 
            }                                                                  
                                                                        
            if (!bandera) {    
                var modal = $('#errorfileModal')
                modal.find('.modal-title').text("Error")
                modal.find('.modal-body').text("Solo se permiten archivos con extenciones: jpg,png,jpeg.")
                modal.modal('show')                                                                                                                                     
                oninput.value = "";                                             
                return false;                                   
            }                                                                  
        }                                                                           
    }                                                                               
    return true;                                                        
}   



function comprobar(){
    formDatos = {};
    mensaje = ""
    aux=true
    formDatos[0] = document.getElementById('nombre').value
    formDatos[1] = document.getElementById('apaterno').value
    formDatos[2] = document.getElementById('amaterno').value
    formDatos[3] = document.getElementById('genero').value
    formDatos[4] = document.getElementById('colonia').value
    formDatos[5] = document.getElementById('calle').value
    formDatos[6] = document.getElementById('ncasa').value
    formDatos[7] = document.getElementById('fnacimiento').value
    formDatos[8] = document.getElementById('fregistro').value
    formDatos[9] = document.getElementById('correo').value
    formDatos[10] = document.getElementById('telefono').value
    formDatos[11] = document.getElementById('usuario').value
    formDatos[12] = document.getElementById('pass1').value
    formDatos[13] = document.getElementById('pass2').value
    formDatos[14] = document.getElementById('file').value





    if(formDatos[12] != formDatos[13]){
        mensaje = mensaje + "Las contraseñas no coinciden. \n\n"
        aux=false;
    }

    for (const key in formDatos) { //Recorre todo los campos del formulario.

        if(formDatos[key] == ""){ //Verifica si los campos estan vacios y si es así devuelve un error y en la variable aux devuelve un false.
            mensaje = mensaje + "Alguno de los campos esta vacio. \n\n"
            aux =false;
            break;
        }
    }



    if(!validarCorreo(formDatos[9])){
        mensaje = mensaje + "El correo es invalido. \n\n"
        aux =false;
    }

    if(!validarTelefono(formDatos[10])){
        mensaje = mensaje + "El telefono es invalido. \n\n"
        aux =false;
    }


    if(!validarDigito(formDatos[6])){
        mensaje = mensaje + "El numero de casa debe ser un dígito. \n\n"
        aux =false;
    }

    if(!logitudUsuario(formDatos[11])){
        mensaje = mensaje + "El usuario debe tener 8 caracteres. \n\n"
        aux =false;
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


function validarDigito(valor){                  
    var regex = /^\d+$/                                                  
    var response = regex.test(valor)                                                           
    return response;                                                                        
}   

function validarTelefono(valor){                                
    var regex = /^\d{3}-\d{3}-\d{4}$/                                                     
    var response = regex.test(valor)                                            
    return response;                                                                        
}   

function validarCorreo(valor){                                
    var regex = /^\w[a-zA-Z.-_$,]+@\w[a-zA-Z]+\.\w[a-zA-Z]+\.?\w+/                                                     
    var response = regex.test(valor)                                            
    return response;                                                                        
}   

function logitudUsuario(valor){                                
    var regex = /^\w{8,}/                                                     
    var response = regex.test(valor)                                            
    return response;                                                                        
}

function logitudnss(valor){                                
    var regex = /^\d{10}$/                                                     
    var response = regex.test(valor)                                            
    return response;                                                                        
}