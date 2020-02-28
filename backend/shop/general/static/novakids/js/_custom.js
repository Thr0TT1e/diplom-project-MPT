document.addEventListener("DOMContentLoaded", function() {

    $(document).ready(function () {
        $('#slider_img-inner').slick({
            accessibility: true,
            speed: 300,
            autoplay: true,
            arrows: false,
            dots: true,
            adaptiveHeight: true,
        });
    });
});
