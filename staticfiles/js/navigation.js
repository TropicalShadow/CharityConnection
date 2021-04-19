var contentLocation = "/static/Images/Category/";

$(document).ready(function () {
    $("#volunteerBar").hide();

    // Displays the volunteer category nav bar when hovering over "find volunteer opportunities"
    $("#findVolunteerBtn").mouseenter(function () {

        $("#volunteerBar").slideToggle(750);
    });

    $('.catImage').mouseenter(function () {
        var name = $(this).attr('id');
        $('#' + name).attr('src', contentLocation + "Color/" + name + 'Color.svg').width(71).height(61);
    }).mouseleave(function () {
        var name = $(this).attr('id');
        $('#' + name).attr('src', contentLocation + "Gray/" + name + '.svg').width(71).height(61);
    });

});