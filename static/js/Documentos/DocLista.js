var extValidas = [".pdf"]; 

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
                modal.find('.modal-body').text("Solo se permiten archivos con extenciones: .pdf")
                modal.modal('show')                                                                                                                                     
                oninput.value = "";                                             
                return false;                                   
            }                                                                  
        }                                                                           
    }                                                                               
    return true;                                                        
}

function AñadirDoc(){
    vali=document.getElementById('Sel_A').value;

    if(vali=='NA'){
        alert("Seleccione un Elemento Valido")
    }else{
        MostrarDiv('datos')
    }
}





function MostrarDiv(div) {
    document.getElementById(div).style.display = "block";
}

function OcultarDiv(div) {
    document.getElementById(div).style.display = "none";
}


