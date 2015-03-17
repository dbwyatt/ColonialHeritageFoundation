/**
 * Created by Daniel on 3/7/2015.
 */

$(function() {
    $(".buy").on("click", function() {
        var id = $(this).attr("data-id");
        var select = $(this).parent().find("select option:selected").val();
        var quantity = select;

        $.ajax({
            url: "/homepage/cart.updatecart/" + id + "/" + quantity,
            async: false,
            success: function() {

            } //success
        }); //ajax

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