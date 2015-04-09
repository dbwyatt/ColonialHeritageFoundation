/**
 * Created by Daniel on 3/7/2015.
 */

$(function() {
    $(".buy").on("click", function() {
        var $this = $(this);
        var id = $(this).attr("data-id");
        var select = $(this).parent().find("select option:selected").val();
        var quantity = select;

        $.ajax({
            url: "/homepage/cart.updatecartadd/" + id + "/" + quantity,
            async: false,
            success: function(ret) {
                if (ret == "Login") {
                    $('#login-button').trigger('click');
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

        //$.ajax({
        //    url: "/homepage/cart.getcart/",
        //    async: false,
        //    success: function(data) {
        //        $("#cart-modal").find(".modal-body").html(data);
        //        $("#cart-modal tr label").each(function() {
        //            var text = $(this).text();
        //            $(this).text(text.substr(0, text.length - 1));
        //        }); //remove colon
        //    } //success
        //}); //ajax
    }); //click

    /* Search for a product */
    //$('#id_search').keypress(function(e) {
    //    if(e.which == 13) {
    //      var search = $('#id_search').val();
    //      $.ajax({
    //        url: '/catalog/index.search/',
    //        data: {
    //          s: search,
    //        },
    //        type: "POST",
    //        success: function(resp){
    //          //evaluate response, send appropriate html response
    //        },//success
    //      });//ajax
    //};//if enter pressed

}); //ready