/**
 * Created by Daniel on 3/4/2015.
 */

$(function() {
    $("#login-form").ajaxForm(function(data) {
        $("#login-modal").find(".modal-body").html(data);
        $("#login-modal tr label").each(function() {
            var text = $(this).text();
            $(this).text(text.substr(0, text.length - 1));
        }); //remove colon
    }); //ajax
}); //ready