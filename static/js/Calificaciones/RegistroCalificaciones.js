


function showmodal() {
    var modal = $('#gruposmodal')
    modal.find('.modal-title').text("Grupos")
    modal.modal('show')
}


function getValues(id_grupo,id_mat){
    alert(id_grupo)
    datos= document.getElementById('unidad'+id_mat).value
    alert("Unidad: " +datos)
    location.href = "/modificarGrupo/"+id_grupo+"/"+datos
    
}


function geteliValues(id_grupo,id_mat){
    alert(id_grupo)
    datos= document.getElementById('unidad'+id_mat).value
    alert("Unidad: " +datos)
    location.href = "/EliminarGrupo/"+id_grupo+"/"+datos
    
}

$('#gruposmodal').modal({backdrop: 'static', keyboard: false})