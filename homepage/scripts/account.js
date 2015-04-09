/**
 * Created by Daniel on 3/7/2015.
 */

$(function() {

    $(".change-password").on("click", function() {
        var $this = $(this);
        var $modal = $("#user-modal");
        var $body = $modal.find(".modal-body");
        $body.empty();

        $.ajax({
            url: "/homepage/account.changepassword/" + $(this).attr("data-id"),
            success: function(data) {
                //append modal with form
                $body.append(data);

                //change password
                $("#user-form").attr("action", "/homepage/account.changepassword/" + $this.attr("data-id"));
                $modal.find(".modal-title").text("Change Password");

                $("#user-modal tr label").each(function() {
                    var text = $(this).text();
                    $(this).text(text.substr(0, text.length - 1));
                }); //remove colon
                $('#user-modal').modal(); //initiate modal
            } //success
        }); //ajax
    }); //edit click

    $(".update-info").on("click", function() {
        var $this = $(this);
        var $modal = $("#user-modal");
        var $body = $modal.find(".modal-body");
        $body.empty();

        $.ajax({
            url: "/homepage/account.edit/" + $(this).attr("data-id"),
            success: function(data) {
                //append modal with form
                $body.append(data);

                //update info
                $modal.find(".modal-title").text("Update Information");

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