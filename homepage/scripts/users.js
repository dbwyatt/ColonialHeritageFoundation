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

    $(".edit-user, .add-user, .change-password").on("click", function() {
        var $this = $(this);
        var $modal = $("#user-modal");
        var $body = $modal.find(".modal-body");
        $body.empty();

        var url = '';
        if ($(this).hasClass("edit-user")) {
            url = "/homepage/users.edit/" + $(this).attr("data-id");
        }
        else if ($(this).hasClass("add-user")) {
            url = "/homepage/users.create/";
        }
        else if ($(this).hasClass("change-password")) {
            url = "/homepage/users.changepassword/" + $(this).attr("data-id");
        }

        $.ajax({
            url: url,
            success: function(data) {
                //append modal with form
                $body.append(data);

                //change actions of form
                if ($this.hasClass("edit-user")) {
                    //edit user
                    $("#user-form").attr("action", "/homepage/users.edit/" + $this.attr("data-id"));
                    $modal.find(".modal-title").text("Edit " + $body.find("input[name='first_name']").val() + " " + $body.find("input[name='last_name']").val());
                }
                else if ($this.hasClass("add-user")) {
                    //add user
                    $("#user-form").attr("action", "/homepage/users.create/");
                    $modal.find(".modal-title").text("New User");
                }
                else if ($this.hasClass("change-password")) {
                    //change password
                    $("#user-form").attr("action", "/homepage/users.changepassword/" + $this.attr("data-id"));
                    $modal.find(".modal-title").text("Change Password");
                }

                $("#user-modal tr label").each(function() {
                    var text = $(this).text();
                    $(this).text(text.substr(0, text.length - 1));
                }); //remove colon
                $('#user-modal').modal(); //initiate modal
            } //success
        }); //ajax
    }); //edit click

    $("#user-modal .modal-body").off("focus.remove", "input").on("focus.remove", "input", function() {
        $(this).prev(".errorlist").remove();
    }); //modal input keyup

}); //ready