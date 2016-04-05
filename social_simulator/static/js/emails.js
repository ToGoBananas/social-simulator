$("input[name='send_message']").on('click', function () {
    var form = $('#create_form');
    $.ajax({
        method: form.attr('method'),
        url: form.attr('action'),
        data: form.serialize()
    }).done(function(data, textStatus, xhr)  {
        if (xhr.status == 200) {
            alert('Done!');
        } else {
            alert('Fail')
        }
    });
});
