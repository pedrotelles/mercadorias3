$("#cadMercadoria").submit(function (e) {

    var url = "/api/mercadoria"; // the script where you handle the form input.

    $.ajax({
        type: "POST",
        url: url,
        data: $("#cadMercadoria").serialize(), // serializes the form's elements.
        success: function (data) {
            if (data.success == 'true') {
                window.location.href = "/tables"
            }
        }
    });

    e.preventDefault(); // avoid to execute the actual submit of the form.
});