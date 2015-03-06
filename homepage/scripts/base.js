/**
 * Created by Daniel on 3/5/2015.
 */

$(function() {

    $("#login-button").on("click", function() {
        $.ajax({
            url: "/homepage/index.loginform",
            success: function(data) {
                $("#login-modal").find(".modal-body").html(data);
                $("#login-modal tr label").each(function() {
                    var text = $(this).text();
                    $(this).text(text.substr(0, text.length - 1));
                }); //remove colon
            } //success
        }); //ajax
    }); //login click

    $("#login-modal .modal-body").off("focus.remove", "input").on("focus.remove", "input", function() {
        $(this).prev(".errorlist").remove();
    }); //modal input keyup

}); //ready