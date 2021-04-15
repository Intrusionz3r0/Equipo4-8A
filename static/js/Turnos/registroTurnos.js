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


function asignarSalida(){
    

    var HrE = document.getElementById("hentrada").value
    var HrS = document.getElementById("hsalida")
    HrS.value= addTimes(HrE,"08:00").split(":")[0] + ":" + addTimes(HrE,"08:00").split(":")[1]
}

function addTimes(start, end) {
    times = [];
    times1 = start.split(':');
    times2 = end.split(':');
  
    for (var i = 0; i < 3; i++) {
      times1[i] = (isNaN(parseInt(times1[i]))) ? 0 : parseInt(times1[i])
      times2[i] = (isNaN(parseInt(times2[i]))) ? 0 : parseInt(times2[i])
      times[i] = times1[i] + times2[i];
    }
  
    var seconds = times[2];
    var minutes = times[1];
    var hours = times[0];
  
    if (seconds % 60 === 0) {
      hours += seconds / 60;
    }
  
    if (minutes % 60 === 0) {
      res = minutes / 60;
      hours += res;
      minutes = minutes - (60 * res);
    }
  
    return hours + ':' + minutes + ':' + seconds;
  }
