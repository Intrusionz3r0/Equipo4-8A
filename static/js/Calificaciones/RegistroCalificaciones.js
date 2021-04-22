function validarDatosCalificaciones(){
    var formDatos={};
    var mensaje="";
    var aux=true;
    formDatos[0]=document.getElementById("id_alumno").Value;
    formDatos[1]=document.getElementById("unidad_Materia").Value;
    formDatos[2]=document.getElementById("calif_alumno").Value;

    for(const key in formDatos){
        if(formDatos[key]==""){
            mensaje=mensaje + "Varios campos son incorrectos. \n\n"
            aux=false;
            break;
        }
    }

    function validarCalificacion(calif){
        
    }
}