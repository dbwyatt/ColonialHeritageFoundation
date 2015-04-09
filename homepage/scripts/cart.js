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

    $(document).on("click", ".delete", function() {
        $.ajax({
            url: "/homepage/cart.delete/" + $(this).attr("data-id"),
            success: function(data) {
                window.location.reload(true);
            }
        })
    })

    $(document).on("click", ".update", function() {
        $this = $(this);
        $(this).text("Updating...");
        var id = $(this).attr("data-id");
        var select = $(this).parent().find("#qty").val();
        var quantity = select;

        $.ajax({
            url: "/homepage/cart.updatecart/" + id + "/" + quantity,
            async: false,
            success: function() {
                $this.text("Done");
                setTimeout(function(){
                    $this.text("Update");
                    window.location = window.location;
                }, 10);
            } //success
        }); //ajax
    })
}); //ready