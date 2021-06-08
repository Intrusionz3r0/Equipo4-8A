//Funcion para ambas tablas pagos//
function SelecAlumno() {
    alu = document.getElementById('PagAlu').value;

    if (alu == 'NA') {
        alert("Seleccione a un Alumno Valido")
    }
}
function AsigFecha() {

    var fecha = new Date(); //Fecha actual
    var mes = fecha.getMonth() + 1; //obteniendo mes
    var dia = fecha.getDate(); //obteniendo dia
    var ano = fecha.getFullYear(); //obteniendo año
    

    if (dia < 10){
        dia = '0' + dia; //agrega cero si el menor de 10
    }
    if (mes < 10){
        mes = '0' + mes //agrega cero si el menor de 10
    }
    
    document.getElementById('FchHoy').value = ano + "-" + mes + "-" + dia;

}

function exportTableToExcel(tableID, filename = ''){
    var downloadLink;
    var dataType = 'application/vnd.ms-excel';
    var tableSelect = document.getElementById(tableID);
    var tableHTML = tableSelect.outerHTML.replace(/ /g, '%20');
    
    // Specify file name
    filename = filename?filename+'.xls':'excel_data.xls';
    
    // Create download link element
    downloadLink = document.createElement("a");
    
    document.body.appendChild(downloadLink);
    
    if(navigator.msSaveOrOpenBlob){
        var blob = new Blob(['ufeff', tableHTML], {
            type: dataType
        });
        navigator.msSaveOrOpenBlob( blob, filename);
    }else{
        // Create a link to the file
        downloadLink.href = 'data:' + dataType + ', ' + tableHTML;
    
        // Setting the file name
        downloadLink.download = filename;
        
        //triggering the function
        downloadLink.click();
    }
}
//--Fin de Funcion para ambas tablas pagos//

//Funciones Pagos
function SelecServicio() {
    serv = document.getElementById('tipoPagos').value;
    
    if (serv == 'NA') {
        alert("Seleccione un Servicio Valido")
    }
}

function PrecioServicios(){
    MostrarDiv('Des_Mon');
    AsigFecha();
    serv = document.getElementById('tipoPagos').value;
    monto = 0;
    if (serv == "Constancia") {
        monto = 220;
        alert("El monto es de $"+monto);
        OcultarDiv('MontoPago');
        OcultarDiv('lblMonto');
        document.getElementById('MontoPago').value = monto;
        
        monto = 0;
    }
    if (serv == "Extraordinario") {
        monto = 100;
        alert("El monto es de $"+monto);
        OcultarDiv('MontoPago');
        OcultarDiv('lblMonto');
        document.getElementById('MontoPago').value = monto;
        
        monto = 0;
    }
    if (serv == "HoraTuroria") {
        monto = 120;
        alert("El monto es de $"+monto);
        OcultarDiv('MontoPago');
        OcultarDiv('lblMonto');
        document.getElementById('MontoPago').value = monto;
        
        monto = 0;
    }
    if (serv == "Materiales") {
        monto = 0;
        document.getElementById('MontoPago').value = monto;
        MostrarDiv('MontoPago');
        MostrarDiv('lblMonto');
        monto = 0;
    }
    if (serv == "Festival") {
        monto = 0;
        document.getElementById('MontoPago').value = monto;
        MostrarDiv('MontoPago');
        MostrarDiv('lblMonto');
        monto = 0;
    }
    if (serv == "Viaje") {
        monto = 0;
        document.getElementById('MontoPago').value = monto;
        MostrarDiv('MontoPago');
        MostrarDiv('lblMonto');
        monto = 0;
    }

}

function ModifServ(){
    serv = document.getElementById('tipoPagos1').value;
    monto = 0;
    if (serv == "Constancia") {
        monto = 220;
        //alert("El monto es de $"+monto);
        
        document.getElementById('MontoPago').value = monto;
        
        monto = 0;
    }
    if (serv == "Extraordinario") {
        monto = 100;
        //alert("El monto es de $"+monto);
        
        document.getElementById('MontoPago').value = monto;
        
        monto = 0;
    }
    if (serv == "HoraTuroria") {
        monto = 120;
        //alert("El monto es de $"+monto);
        
        document.getElementById('MontoPago').value = monto;
        
        monto = 0;
    }
    if (serv == "Materiales") {
        monto = 0;
        document.getElementById('MontoPago').value = monto;
        
        monto = 0;
    }
    if (serv == "Festival") {
        monto = 0;
        document.getElementById('MontoPago').value = monto;
        
        monto = 0;
    }
    if (serv == "Viaje") {
        monto = 0;
        document.getElementById('MontoPago').value = monto;
        
        monto = 0;
    }

}


function ocultarBtnPDFPagos(){
    OcultarDiv('DwdPDF');
}

//--Fin de Funciones Pagos

//Funciones Pagos Colegiatura
function AsigColegiatura(){
    var fecha = new Date(); //Fecha actual
    
    var dia = fecha.getDate(); //obteniendo dia
    if(dia>6){
        alert('El pago esta fuera de tiempo, se añadio multa de $50.00 pesos');
        document.getElementById('MontoPago').value=400;
    }else{
        document.getElementById('MontoPago').value=350;
    }
    
}

function AsigCodigo(){
    Fch=new Date();
    mes=Fch.getMonth()+1;
    año=Fch.getFullYear();
    alert(mes);
    MES='';
    
    if(mes==1){
        MES='Enero';
    }else if(mes==2){
        MES='Febreo';
    }else if(mes==3){
        MES='Marzo';
    }else if(mes==4){
        MES='Abril';
    }else if(mes==5){
        MES='Mayo';
    }else if(mes==6){
        MES='Junio';
    }else if(mes==7){
        MES='Julio';
    }else if(mes==8){
        MES='Agosto';
    }else if(mes==9){
        MES='Septiembre';
    }else if(mes==10){
        MES='Octubre';
    }else if(mes==11){
        MES='Noviembre';
    }else if(mes==12){
        MES='Diciembre';
    }

    
   id=document.getElementById('PagAluColeg').value;
    document.getElementById('Codigo').value=MES+'-'+año+'#'+id;
}

function ocultarBtnPDFPagosColeg(){
    OcultarDiv('DwdPDFColeg');
}

function ObtenerMES(){
    Fch=new Date();
    mes=Fch.getMonth()+1;
    año=Fch.getFullYear();
    alert(mes);
    MES='';
    
    if(mes==1){
        MES='Enero';
    }else if(mes==2){
        MES='Febreo';
    }else if(mes==3){
        MES='Marzo';
    }else if(mes==4){
        MES='Abril';
    }else if(mes==5){
        MES='Mayo';
    }else if(mes==6){
        MES='Junio';
    }else if(mes==7){
        MES='Julio';
    }else if(mes==8){
        MES='Agosto';
    }else if(mes==9){
        MES='Septiembre';
    }else if(mes==10){
        MES='Octubre';
    }else if(mes==11){
        MES='Noviembre';
    }else if(mes==12){
        MES='Diciembre';
    }

    
   id=document.getElementById('PagAluColeg').value;
   alert("ObteMEs"+MES+'-'+año+'#'+id);
    return MES+'-'+año+'#'+id;
}
//--Fin de Funciones Pagos Colegiatura//

function MostrarDiv(div) {
    document.getElementById(div).style.display = "block";
}

function OcultarDiv(div) {
    document.getElementById(div).style.display = "none";
}
