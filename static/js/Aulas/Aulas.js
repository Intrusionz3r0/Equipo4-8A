function validar(form){
    var cad=validaridAula(form.idAula.value);
        cad+=validaridEdificio(form.idEdificio.value);
        cad+=validarnombre(form.nombre.value);
        cad+=validarcapacidad(form.capacidad.value);
        cad+=validarestado(form.estado.value);

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


function validaridAula(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else{
        return "El id del Aula es invalido, debe ser mayor a 1 <br>";
    }
}

function validaridEdificio(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else{
        return "Id de Edificio invalido <br>";
    }
}

function validarnombre(cad)
{
    if(cad.length==0)
    {
        return 'Debes informar el nombre de la persona <br>';
    }
    else{
        return " ";
    }
}

function validarcapacidad(cad)
{
    if(cad>=15 && cad<=40)
    {
        return '';
    }
    else{
        return "Capacidad de aula invalido <br>";
    }
}

function validarestado(cad)
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
var arrayAulas=[];
class Aula
{
    constructor(idAula,idEdificio,nombre,capacidad,estado)
    {
        this.idAula =idAula;
        this.idEdificio =idEdificio;
        this.nombre=nombre;
        this.capacidad=capacidad;
        this.estado=estado;
    }
    toString()
    {
        return "Id_aula: "+this.idAula+", Id_edificio: "+this.idEdificio + ", nombre: " + this.nombre + ", capacidad: " + this.capacidad + ", estado: "+this.estado;
    }

    guardar()
    {
        //Almacenará el objeto en la BD
        arrayAulas.push(this)
    }
    actualizar()
    {
        for(i=0;i<arrayAulas.length;i++){
            if(arrayAulas[i].id==this.id){
                arrayAulas[i]=this;
            }
        }
    }

    eliminar()
    {
      alert("Se borraran datos");
        for(i=0;i<arrayAulas.length;i++){
            if(arrayAulas[i].id==this.id){
                arrayAulas.splice(i,1);
            }
        }
    }
    consultar()
    {
        for(i=0;i<arrayAulas.length;i++){
            if(arrayAulas[i].id==this.id){
                return arrayAulas[i];
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
