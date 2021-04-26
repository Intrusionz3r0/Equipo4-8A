
function ChecarTipoUSR() {
    tipo = document.getElementById("TIPO_U").value;
    if (tipo == "NA") {
        alert("Seleccione Tipo de Usuario");
    }
    if (tipo == "EMP") {
        alert("TIpo Usuario :" + tipo);
        OcultarDiv("SelectTipo")
        MostrarDiv("ListaUsuarioEmp");
        OcultarDiv("ListaUsuarioAlum");
        MostrarDiv("datos");

    }

    if (tipo == "ALU") {
        alert("TIpo Usuario :" + tipo);
        OcultarDiv("SelectTipo")
        MostrarDiv("ListaUsuarioAlum");
        OcultarDiv("ListaUsuarioEmp");
        MostrarDiv("datos");

    }

}

function AsignarID() {
    tipo = document.getElementById("TIPO_U").value;

    if (tipo == "EMP") {
            alert("EMPLE");
            id = document.getElementById("Sel_E").value;
            alert("Empleado "+ id);
            return id;
        
    }

    if (tipo == "ALU") {
            alert("ALUM");
            id = document.getElementById("Sel_A").value;
            alert("Alumno "+ id);
            return id;
        
    }
}


function MostrarDiv(div) {
    document.getElementById(div).style.display = "block";
}

function OcultarDiv(div) {
    document.getElementById(div).style.display = "none";
}


