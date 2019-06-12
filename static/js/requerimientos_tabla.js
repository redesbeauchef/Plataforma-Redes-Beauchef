// $(document).ready(function () {
//     $('#carreraselect-1').select2();
//     $('#ofertaselect-1').select2();
// });

function addOferta(id_carrera){
    var header = document.getObjectById("header-oferta");
    var oferta = document.getObjectById("ofertaselect-" + id_carrera.split("-")[1]);
    header.hidden = false;
    oferta.hidden = false;
}

function addCupos(id_oferta){
    var header = document.getObjectById("header-cupos");
    var cupos = document.getObjectById("cuposselect-" + id_oferta.split("-")[1]);
    header.hidden = false;
    cupos.hidden = false;
}

