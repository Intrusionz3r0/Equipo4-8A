
function ChecarTipoUSR() {
    tipo = document.getElementById("TIPO_U").value;
    if (tipo == "NA") {
        alert("Seleccione Tipo de Usuario");
        OcultarDiv("ListaUsuarioAlum");
        OcultarDiv("ListaUsuarioAlum");
        OcultarDiv("datos")
    }
    if (tipo == "EMP") {
        
        OcultarDiv("SelectTipo")
        MostrarDiv("ListaUsuarioEmp");
        OcultarDiv("ListaUsuarioAlum");
        MostrarDiv("datos");

    }

    if (tipo == "ALU") {
        
        OcultarDiv("SelectTipo")
        MostrarDiv("ListaUsuarioAlum");
        OcultarDiv("ListaUsuarioEmp");
        MostrarDiv("datos");

    }

}

function AsignarID() {
    tipo = document.getElementById("TIPO_U").value;

    if (tipo == "EMP") {
            
            id = document.getElementById("Sel_E").value;
            
            return id;
        
    }

    if (tipo == "ALU") {
            
            id = document.getElementById("Sel_A").value;
            
            return id;
        
    }
}


function MostrarDiv(div) {
    document.getElementById(div).style.display = "block";
}

function OcultarDiv(div) {
    document.getElementById(div).style.display = "none";
}


