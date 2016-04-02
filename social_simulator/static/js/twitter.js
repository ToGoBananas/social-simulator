$('.retweet').on('click', function () {
    var parent = $(this).closest('.post');
    $.ajax({
        method: 'POST',
        url: 'retweet/',
        data: { pk: parent.data('pk') }
    }).done(function(data, textStatus, xhr)  {
        if (xhr.status == 200) {
            var retweet = parent.find('.retweets_quantity');
            retweet.html(parseInt(retweet.html())+1);
        } else {
            alert('You already retweet this post')
        }
    });
});
