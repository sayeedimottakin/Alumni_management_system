$(document).ready(function () {

    /* Every time the window is scrolled ... */
    $(window).scroll(function () {

        /* Check the location of each desired element */
        $('.fade').each(function (i) {

            var bottom_of_object = $(this).position().top + $(this).outerHeight();
            var bottom_of_window = $(window).scrollTop() + $(window).height();

            /* If the object is completely visible in the window, fade it it */
            if (bottom_of_window > bottom_of_object) {

                // $(this).animate({ 'opacity': '1', fontSize: '50px' }, 1200);
                // $(this).animate({  left: '200px' }, 2000);
            }

        });

    });

});

// Add the following code if you want the name of the file appear on select
// $(".custom-file-input").on("change", function () {
//     var fileName = $(this).val().split("\\").pop();
//     $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
// });