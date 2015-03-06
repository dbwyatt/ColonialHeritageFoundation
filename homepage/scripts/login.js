/**
 * Created by Daniel on 3/4/2015.
 */

$(function() {
    $("#login-form").ajaxForm(function(data) {
        if (data == "logged_in") {
            $("#login-modal").find("#login-form").html("<div class='success'>You're logged in!</div>");
            setTimeout(function() {
                window.location.reload(true);
            }, 1000); //timeout
        }
        else {
            $("#login-modal").find(".modal-body").html(data);
        }
        $("#login-modal tr label").each(function() {
            var text = $(this).text();
            $(this).text(text.substr(0, text.length - 1));
        }); //remove colon
    }); //ajax
}); //ready