var index = 0;

function getTexto(texto){
    dato=document.getElementById("clavesita").value;
    //alert(dato)
    location.href="/filtrarAlumnos/"+dato
}


function getTextoEmpleado(texto){
    dato=document.getElementById("clavesita").value;
    //alert(dato)
    location.href="/filtrarEmpleado/"+dato
}

function getTextoHorario(texto){
    dato=document.getElementById("clavesita").value;
    //alert(dato)
    location.href="/filtrarHorario/"+dato
}
