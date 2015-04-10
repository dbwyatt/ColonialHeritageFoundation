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

    $(document).off("focus.remove", "form input").on("focus.remove", "form input", function() {
        $(this).prev(".errorlist").remove();
    }); //modal input keyup

    $('#logout-button').on('click', function() {
        $.ajax({
            url: '/homepage/index.logout_page/',
            success: function() {
                window.location.reload(true);
            }
        })
    }); //logout

    $(document).on("click", ".cart", function() {
        $.ajax({
            url: "/homepage/cart.getcart/",
            async: false,
            success: function(data) {
                $("#cart-modal").find(".modal-body").html(data);
                $("#cart-modal tr label").each(function() {
                    var text = $(this).text();
                    $(this).text(text.substr(0, text.length - 1));
                }); //remove colon
            } //success
        }); //ajax
    }); //click

    $('#search-button').click(function() {
        var search = $('#search-box').val();
        console.log(search);
        $('#search-form').attr('action', '/homepage/search/' + search);
        $('#search-form').submit();
    }); //search click

}); //ready