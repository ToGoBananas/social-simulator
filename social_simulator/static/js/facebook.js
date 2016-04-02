$('.show_comments').on('click', function () {
    var parent = $(this).closest('.post');
    var comments = parent.find('.comments');
    if( comments.is(':empty') ) {
        $.ajax({
            method: 'POST',
            url: 'show_comments/',
            data: { pk: parent.data('pk') }
        }).done(function (data) {
            comments.append(data)
        });
    }
    var comments_block = parent.find('.comments_block');
    comments_block.toggle();
});


$('textarea').keypress(function(e) {
    if(e.which == 13 && !e.shiftKey) {
        var parent = $(this).closest('.post');
        var comments = parent.find('.comments');
        $.ajax({
            method: 'POST',
            url: 'add_comment/',
            data: {
                pk: parent.data('pk'),
                text: $(this).val()
            }
        }).done(function(data) {
            comments.replaceWith(data)
        });
    }
});


$('.like').on('click', function () {
    var parent = $(this).closest('.post');
    $.ajax({
        method: 'POST',
        url: 'like/',
        data: { pk: parent.data('pk') }
    }).done(function(data, textStatus, xhr)  {
        if (xhr.status == 200) {
            var likes = parent.find('.likes_quantity');
            likes.html(parseInt(likes.html())+1);
        } else {
            alert('You already like this post')
        }
    });
});
