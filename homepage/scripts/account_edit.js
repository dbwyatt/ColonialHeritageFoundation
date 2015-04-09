/**
 * Created by Daniel on 3/5/2015.
 */

//$(function() {
    $("#user-form").ajaxForm(function(data) {
        console.log(data);
        if (data == "True") {
            $("#user-modal").find("#user-form").html("<div class='success'>Saved!</div>");
            setTimeout(function() {
                window.location.reload(true);
            }, 10); //reload timeout
        }
        else {
            $("#user-modal").find(".modal-body").html(data);
        }
        $("#user-modal tr label").each(function() {
            var text = $(this).text();
            $(this).text(text.substr(0, text.length - 1));
        }); //remove colon
        $('#user-modal').modal(); //initiate modal
    }); //ajax
//}); //ready