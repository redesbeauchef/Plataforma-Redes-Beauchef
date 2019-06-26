// $(document).ready(function () {
//     $('#carreraselect-1').select2();
//     $('#ofertaselect-1').select2();
// });

function addOferta(id_fila){
    if(document.getElementById('header-oferta') == null){
        var header = document.getObjectById("head");
        var headHtml = header.innerHtml;
        headHtml = headHtml + "<th id='header-oferta'>Oferta:</th>";
        header.innerHtml = headHtml;
    }
    var fila = document.getElementById(id_fila);
    if(document.getElementById('ofertaselect-'+id_fila.split("-")[1]) == null){
        var filaHtml = fila.innerHTML;
        filaHtml = filaHtml + "<th id='ofertaselect-1' onchange='addCupos(this.id)'>" + "\n" +
            "<select id='oferta-1' name='oferta[]' multiple='multiple' style='width: 300px'>" + "\n" +
                                        "<option value='1'>Practica 1</option>" +"\n" +
                                        "<option value='2'>Practica 2</option>" + "\n" +
                                        "<option value='3'>Practica 3</option>" + "\n" +
                                        "<option value='4'>Memoria</option>"    + "\n" +
                                        "<option value='5'>Part-Time</option>" + "\n" +
                                    "</select>" + "\n" +
                               "</th>";
        var script = document.getElementById('scripts');
        var scriptHtml = script.innerHTML;
        scriptHtml = scriptHtml + "<script type='text/javascript'>" + "\n" +
            "$(document).ready(function () {" + "\n" +
                "$('#oferta-' + id_fila.split('-')[1]).select2();" + "\n" +
            "});" +"\n" +
        "</script>";
        fila.innerHTML = filaHtml;
        script.innerHTML = scriptHtml;
    }
}

function addCupos(id_oferta){
    var header = document.getObjectById("header-cupos");
    var cupos = document.getObjectById("cuposselect-" + id_oferta.split("-")[1]);
    header.hidden = false;
    cupos.display = block;
}

