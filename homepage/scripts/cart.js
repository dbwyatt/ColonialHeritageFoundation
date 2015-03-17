/**
 * Created by Daniel on 3/7/2015.
 */

$(function() {
    $("#cart-form").ajaxForm(function(data) {
        //if (data == "logged_in") {
        //    $("#login-modal").find("#login-form").html("<div class='success'>You're logged in!</div>");
        //    setTimeout(function() {
        //        window.location.reload(true);
        //    }, 1000); //timeout
        //}
        //else {
            $("#cart-modal").find(".modal-body").html(data);
        //}
        $("#cart-modal tr label").each(function() {
            var text = $(this).text();
            $(this).text(text.substr(0, text.length - 1));
        }); //remove colon
    }); //ajax

    $(".delete").on("click", function() {
        $.ajax({
            url: "/homepage/cart.delete/" + $(this).attr("data-id"),
            success: function(data) {
                window.location.reload(true);
            }
        })
    })
}); //ready