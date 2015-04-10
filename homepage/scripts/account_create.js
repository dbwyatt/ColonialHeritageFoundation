/**
 * Created by Daniel on 3/7/2015.
 */

$(function() {

    $("#new-user-form tr label").each(function() {
        var text = $(this).text();
        $(this).text(text.substr(0, text.length - 1));
    }); //remove colon

}); //ready