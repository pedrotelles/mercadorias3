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
                rangelength: [0.01,9999999.99]
            },
            tNegocio: {
                required: true,
            }
        },
        messages: {
            codMer: "Campo Obrigat�rio.",
            tipoMer: {
                required: "Campo Obrigat�rio.",
                minlength: "Esse campo precisa de no m�nimo dois caracteres."
            },
            nomeMer: {
                required: "Campo Obrigat�rio.",
                minlength: "Esse campo precisa de no m�nimo dois caracteres."
            },
            qtdMer: {
                required: "Campo Obrigat�rio.",
                min: "Esse campo precisa de um valor de no m�nimo 1 mercadoria",
                max: "Esse campo precisa de um valor de no m�ximo 9999999 mercadorias"
            },
            precoMer: {
                required: "Campo Obrigat�rio.",
                rangelength: "Esse campo precisa de um valor de no m�nimo R$ 0,01 ou de um valor de no m�ximo R$ 9999999,99",
            },
            tNegocio: {
                required: "Campo Obrigat�rio.",
            }
        }
    })
}
);