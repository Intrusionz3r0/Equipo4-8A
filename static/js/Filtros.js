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

function getTextoAula(texto){
    dato=document.getElementById("clavesita").value;
    location.href="/filtrarAula/"+dato
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

function getTextoGrupo(texto){
    dato=document.getElementById('clave').value;
    location.href="/FiltrarGrupos/"+dato
}

function getTextoTurno(texto){
    dato=document.getElementById("clavesita").value;
    //alert(dato)
    location.href="/filtrarTurno/"+dato
}

function getTextoMateria(texto){
    dato=document.getElementById("clavesita").value;
    //alert(dato)
    location.href="/filtrarMateria/"+dato
}

function getTextoAluGru(texto){
    dato=document.getElementById("clavesita").value;
    location.href="/filtrarAluGru/"+dato
}

function getTextoAsistencia(texto){
    dato=document.getElementById("clavesita").value;
    //alert(dato)
    location.href="/filtrarAsistencia/"+dato
}