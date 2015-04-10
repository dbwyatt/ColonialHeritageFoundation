/**
 * Created by Daniel on 3/7/2015.
 */

$(function() {
    $(".rent").on("click", function() {
        var $this = $(this);
        var id = $(this).attr("data-id");
        var select = $(this).parent().find("select option:selected").val();
        var quantity = select;

        $.ajax({
            url: "/homepage/cart.rentupdatecart/" + id + "/" + quantity,
            async: false,
            success: function(ret) {
                console.log(ret);
                if (ret == "Login") {
                    $('#login-button').trigger('click');
                }
                else if (ret == 'False') {
                    $this.text('Already in cart');
                }
                else {
                    $this.text("Added to cart");
                    setTimeout(function () {
                        $this.text("Add to cart");
                        var $current_cart = parseInt($('.cart .badge').text(), 10);
                        $('.cart .badge').text($current_cart + parseInt(quantity, 10));
                    }, 500);
                }
            } //success
        }); //ajax
    })
}); //ready