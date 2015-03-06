/**
 * Created by Daniel on 2/6/2015.
 */

$(document).on("click", "#users-table th:not(:last-child):not(#change-password)", function() {
    window.location = "/homepage/users.order/" + $(this).data('name') + "/";
});

$(document).on("mouseover", "#users-table th:not(:last-child):not(#change-password)", function() {
    if ($(this).children('.message-box').length < 1) {
        var box = document.createElement('div');
        box.className = "message-box";
        box.innerHTML = "Click to sort by " + $(this).text();

        $(this).append(box);
        $(box).fadeIn().css('bottom', '45px');
    }

    $(document).on("mouseleave", "#users-table th:not(:last-child)", function() {
        $(this).children(".message-box").fadeOut(function(){$(this).remove()}).css('bottom', '35px');
    })
});