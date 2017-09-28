$document.ready(function() {
    $('#cadMercadoria').validate({
        rules: {
            codMer: "required",
            tipoMer: {
                required: true,
                minlength: 2
            },
            nomeMer: {
                required: true,
                minlength: 2
            },
            qtdMer: {
                required: true,
                min: 0,
                max: 9999999
            },
            precoMer: {
                required: true,
                min: 0.01,
                max: 9999999.99
            },
            tNegocio: {
                required: true,
            }
        },
        messages: {
            codMer: "Campo Obrigatório.",
            tipoMer: {
                required: "Campo Obrigatório.",
                minlength: 2
            },
            nomeMer: {
                required: "Campo Obrigatório.",
                minlength: 2
            },
            qtdMer: {
                required: "Campo Obrigatório.",
                min: 0,
                max: 9999999
            },
            precoMer: {
                required: "Campo Obrigatório.",
                min: 0.01,
                max: 9999999.99
            },
            tNegocio: {
                required: "Campo Obrigatório.",
            }
        }
    })
}
);