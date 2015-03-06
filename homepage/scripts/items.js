/**
 * Created by Daniel on 2/5/2015.
 */

$(document).on("click", "#items-table th:not(:last-child)", function() {
    window.location = "/homepage/items.order/" + $(this).data('name') + "/";
});

$(document).on("mouseover", "#items-table th:not(:last-child)", function() {
    if ($(this).children('.message-box').length < 1) {
        var box = document.createElement('div');
        box.className = "message-box";
        box.innerHTML = "Click to sort by " + $(this).text();

        $(this).append(box);
        $(box).fadeIn().css('bottom', '45px');
    }

    $(document).on("mouseleave", "#items-table th:not(:last-child)", function() {
        $(this).children(".message-box").fadeOut(function(){$(this).remove()}).css('bottom', '35px');
    })
});
