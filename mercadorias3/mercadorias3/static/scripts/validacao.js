$().ready(function() {
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
                rangelength: [0.01,9999999.99]
            },
            tNegocio: {
                required: true,
            }
        },
        messages: {
            codMer: "Campo Obrigat&oacute;rio.",
            tipoMer: {
                required: "Campo Obrigat&oacute;rio.",
                minlength: "Esse campo precisa de no m&iacute;nimo dois caracteres."
            },
            nomeMer: {
                required: "Campo Obrigat&oacute;rio.",
                minlength: "Esse campo precisa de no m&iacute;nimo dois caracteres."
            },
            qtdMer: {
                required: "Campo Obrigat&oacute;rio.",
                min: "Esse campo precisa de um valor de no m&iacute;nimo 1 mercadoria",
                max: "Esse campo precisa de um valor de no m&aacute;ximo 9999999 mercadorias"
            },
            precoMer: {
                required: "Campo Obrigat&oacute;rio.",
                rangelength: "Esse campo precisa de um valor de no m&iacute;nimo R$ 0,01 ou de um valor de no m&aacute;ximo R$ 9999999,99",
            },
            tNegocio: {
                required: "Campo Obrigat&oacute;rio.",
            }
        }
    })
}
);