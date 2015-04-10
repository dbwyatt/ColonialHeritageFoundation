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

$(function() {

    $(".edit-item, .add-item").on("click", function() {
        var $this = $(this);
        var $modal = $("#items-modal");
        var $body = $modal.find(".modal-body");
        $body.empty();

        var url = '';
        if ($(this).hasClass("edit-item")) {
            url = "/homepage/items.edit/" + $(this).attr("data-id");
        }
        else if ($(this).hasClass("add-item")) {
            url = "/homepage/items.create/";
        }

        $.ajax({
            url: url,
            success: function(data) {
                //append modal with form
                $body.append(data);

                //change actions of form
                if ($this.hasClass("edit-item")) {
                    //edit user
                    $("#items-form").attr("action", "/homepage/items.edit/" + $this.attr("data-id"));
                    $modal.find(".modal-title").text("Edit " + $body.find("input[name='name']").val());
                }
                else if ($this.hasClass("add-item")) {
                    //add user
                    $("#user-form").attr("action", "/homepage/items.create/");
                    $modal.find(".modal-title").text("New Item");
                }

                $("#items-modal tr label").each(function() {
                    var text = $(this).text();
                    $(this).text(text.substr(0, text.length - 1));
                }); //remove colon
                $('#items-modal').modal(); //initiate modal
            } //success
        }); //ajax
    }); //edit click

    $("#items-modal .modal-body").off("focus.remove", "input").on("focus.remove", "input", function() {
        $(this).prev(".errorlist").remove();
    }); //modal input keyup

}); //ready
