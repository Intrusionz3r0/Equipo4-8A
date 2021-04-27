function validar(form){
    var cad=validarid_grupo(form.id_grupo.value);
        cad+=validargrado(form.grado.value);
        cad+=validargrupo(form.grupo.value);
        cad+=validarcapacidad(form.capacidad.value);
        cad+=validarid_turno(form.id_turno.value);
        cad+=validarid_materia(form.id_materia.value);
        cad+=validarid_usuario(form.id_usuario.value);
        cad+=validarestatus(form.estatus.value);

    var accion = form.accion.value;
    if(cad!=''){
        document.getElementById("notificaciones" + accion).innerHTML='<p>'+cad+'</p>';
        return false;
    }
    else{
        var accion = form.accion.value;
        if (accion == "crear")
        {
          alert("Crear");
        }else {
          alert("Editar")
        }
       return true;
    }
}


function validarid_grupo(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else{
        return "El id del Grupo es invalido, debe ser mayor a 1 <br>";
    }
}

function validargrado(cad)
{
    if(cad>=1 && cad<=6)
    {
        return '';
    }
    else{
        return "El campo no fue llenado correctamente a los grados a nivel primaria ";
    }
}


function validargrupo(cad)
{
    if(cad=='A' ||cad=='B' ||cad=='C' ||cad=='D' ||cad=='E')
    {
        return '';
    }
    else{
        return "Grupo invalido o vacio, debe llenar correctamente <br>";
    }
}

function validarcapacidad(cad)
{
    if(cad>=10 && cad<=25)
    {
        return '';
    }
    else{
        return "Capacidad del grupo invalido <br>";
    }
}

function validarid_turno(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else{
        return "El id del Turno es invalido, debe ser mayor a 1 <br>";
    }
}

function validarid_materia(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else{
        return "El id de la Materia es invalido, debe ser mayor a 1 <br>";
    }
}

function validarid_usuario(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else{
        return "El id del Docente es invalido, debe ser mayor a 1 <br>";
    }
}

function validarestatus(cad)
{
    if(cad.length>1)
    {
        return ' ';
    }
    else
    {
        return 'Debes informar un estado valido <br> ';
    }
    
}
///////////////////////////////////Aquí termina la validación///////////////////
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////Aquí empieza la creación del objeto///////////
var arrayGrupos=[];
class Grupo
{
    constructor(id_grupo,grado,grupo,capacidad,id_turno,id_materia,id_usuario,estatus)
    {
        this.id_grupo=id_grupo;
        this.grado=grado;
        this.grupo=grupo;
        this.capacidad=capacidad;
        this.id_turno=id_turno;
        this.id_materia=id_materia;
        this.id_usuario=id_usuario;
        this.estatus=estatus;
    }
    toString()
    {
        return "Id_grupo: "+this.id_grupo+", grado: "+this.grado + ", grupo: " + this.grupo + ", capacidad: " + this.capacidad + ", turno: "+this.id_turno+", materia: "+this.id_materia+", docente: "+this.id_usuario+", estatus: "+this.estatus;
    }

    guardar()
    {
        //Almacenará el objeto en la BD
        arrayGrupos.push(this)
    }
    actualizar()
    {
        for(i=0;i<arrayGrupos.length;i++){
            if(arrayGrupos[i].id==this.id){
                arrayGrupos[i]=this;
            }
        }
    }

    eliminar()
    {
      alert("Se borraran datos");
        for(i=0;i<arrayGrupos.length;i++){
            if(arrayGrupos[i].id==this.id){
                arrayGrupos.splice(i,1);
            }
        }
    }
    consultar()
    {
        for(i=0;i<arrayGrupos.length;i++){
            if(arrayGrupos[i].id==this.id){
                return arrayGrupos[i];
            }
        }
        return null;
    }
}

function mostrarDiv(){
    document.getElementById("modalEliminacion").style.display="block";
}
function ocultarDiv(){
    document.getElementById("modalEliminacion").style.display="none";
}
