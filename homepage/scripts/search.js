/**
 * Created by Daniel on 4/9/2015.
 */

$(function() {
    $(document).on("click", "#events-table th:not(:last-child)", function () {
        window.location = "/homepage/items.order/" + $(this).data('name') + "/";
    });

    $(document).on("mouseover", "#items-table th:not(:last-child)", function () {
        if ($(this).children('.message-box').length < 1) {
            var box = document.createElement('div');
            box.className = "message-box";
            box.innerHTML = "Click to sort by " + $(this).text();

            $(this).append(box);
            $(box).fadeIn().css('bottom', '45px');
        }

        $(document).on("mouseleave", "#items-table th:not(:last-child)", function () {
            $(this).children(".message-box").fadeOut(function () {
                $(this).remove()
            }).css('bottom', '35px');
        })
    });

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

}); //ready
























