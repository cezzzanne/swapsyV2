let myDays = [];

$(document).ready(function() {
    let csrftoken = Cookies.get('csrftoken');
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });
    function setAvailability() {
        console.log("here");
        let csrftoken = Cookies.get('csrftoken');
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        });
        let startTime = document.getElementById("start-time").value;
        let endTime = document.getElementById("end-time").value;
        let address = document.getElementById("address").value;
        console.log(startTime);
        $.ajax({
            type: 'post',
            url: "/set/user/availability",
            data: {
                start_time: startTime,
                end_time: endTime,
                address: address,
                days: myDays
            },
            success: function (result) {
                console.log(result);
            }
        });
    }
});

function setDays(element) {
    let name = element.innerHTML;
    if (myDays.includes(name)) {
        let ind = myDays.indexOf(name);
        if (ind > -1) {
            myDays.splice(ind, 1);
        }
        element.style.color = "";
        console.log(myDays);
    } else {
        myDays.push(element.innerHTML);
        console.log(myDays);
        element.style.color = "blue";
    }
}
