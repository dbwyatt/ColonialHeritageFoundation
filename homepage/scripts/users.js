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

$(function() {

    $(".edit-user").on("click", function() {
        $("#edit-modal").find(".modal-body").empty();
        $.ajax({
            url: "/homepage/users.edit/" + $(this).attr("data-id"),
            success: function(data) {
                $("#edit-modal").find(".modal-body").append(data); //append modal with form
                $("#edit-modal tr label").each(function() {
                    var text = $(this).text();
                    $(this).text(text.substr(0, text.length - 1));
                }); //remove colon
                $('#edit-modal').modal(); //initiate modal
            } //success
        }); //ajax
    }); //edit click

    $("#edit-modal .modal-body").off("focus.remove", "input").on("focus.remove", "input", function() {
        $(this).prev(".errorlist").remove();
    }); //modal input keyup

    $(".add-user").on("click", function() {
        $("#edit-modal").find(".modal-body").empty();
        $.ajax({
            url: "/homepage/users.create/",
            success: function(data) {
                $("#edit-modal").find(".modal-body").append(data); //append modal with form
                $("#edit-modal tr label").each(function() {
                    var text = $(this).text();
                    $(this).text(text.substr(0, text.length - 1));
                }); //remove colon
                $('#edit-modal').modal(); //initiate modal
            } //success
        }); //ajax
    }); //add click


}); //ready