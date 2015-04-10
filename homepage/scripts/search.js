/**
 * Created by Daniel on 4/9/2015.
 */

$(function() {

    $('#events-table tr').click(function() {
        var $this = $(this);
        if (!$this.next("tr").hasClass("description")) {
            var id = $(this).data('id');
            $.ajax({
                url: '/homepage/view_events.getEventDescription/' + id,
                success: function (data) {
                    $('#event-description-modal .modal-body').html(data);
                }
            })
        }
    });
    $('#items-table tr').click(function() {
        var $this = $(this);
        if (!$this.hasClass("no-click")) {
            var id = $(this).data('link');
            window.location = id;
        }
    });

}); //ready
























