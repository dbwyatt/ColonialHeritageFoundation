/**
 * Created by Daniel on 3/5/2015.
 */

//$(function() {
    $("#edit-form").ajaxForm(function(data) {
        console.log(data);
        if (data == "True") {
            $("#edit-modal").find("#edit-form").html("<div class='success'>Saved!</div>");
            setTimeout(function() {
                window.location.reload(true);
            }); //reload timeout
        }
        else {
            $("#edit-modal").find(".modal-body").html(data);
        }
        $("#edit-modal tr label").each(function() {
            var text = $(this).text();
            $(this).text(text.substr(0, text.length - 1));
        }); //remove colon
        $('#edit-modal').modal(); //initiate modal
    }); //ajax
//}); //ready