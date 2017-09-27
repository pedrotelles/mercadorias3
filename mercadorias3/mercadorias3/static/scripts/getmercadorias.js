$.ajax({
url: '/api/mercadorias',
type: "GET",
dataType: "json",
success: function (data) {
    var trHTML = '';
    $.each(data, function (i, val2) {
        val = val2['Mercadoria']
        $("#tabelaPS tbody").append(
            "<tr><td>" + val['codMer'] + "</td><td>" + val.tipoMer + "</td><td>" + val.nomeMer + "</td><td>" + val.qtdMer + "</td><td>" + val.preco + "</td><td>" + (val.tNegocio == 1 ? "Venda" : "Compra") + "</td></tr>"
        )

    })
    
}
});