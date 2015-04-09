/**
 * Created by Daniel on 3/7/2015.
 */

$(function() {
    $("tr").on("click", function() {
        var $this = $(this);
        var id = $(this).attr("data-id");

        $.ajax({
            url: "/homepage/cart.updatecartadd/" + id + "/" + '1',
            async: false,
            success: function() {
                $("table").after("<p class='added-to-cart'>Added to cart</p>");
                setTimeout(function() {
                    $('.added-to-cart').first().remove();
                }, 10);
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