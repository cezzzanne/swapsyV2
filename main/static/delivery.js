$(function() {
    $(".slider-range").slider({
        range: true,
        min: 0,
        max: 1440,
        step: 15,
        slide: function(e, ui) {
            var hours = Math.floor(ui.value / 60);
            var minutes = ui.value - (hours * 60);

            if(hours.toString().length == 1) hours = '0' + hours;
            if(minutes.toString().length == 1) minutes = '0' + minutes;

            $('#something').html(hours+':'+minutes);
        }
    });
});