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

function getNombreEdif(nombre){
    dato=document.getElementById('nombreEFLT').value;
    location.href="/FiltradoEdificios/"+dato
}

function getNombreDA(nombre){
    dato=document.getElementById('nombreDAFLT').value;
    location.href="/filtrarDocAlumnos/"+dato
}

function getNombreDE(nombre){
    dato=document.getElementById('nombreDEFLT').value;
    location.href="/filtrarDocEmpleados/"+dato
}

function getDescripcionPago(nombre){
    dato=document.getElementById('DescriFLT').value;
    location.href="/FiltradoPagos/"+dato
}