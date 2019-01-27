$(document).ready(function() {

    function toggleSidebar() {
      $(".a").toggleClass("active");
      $("main").toggleClass("move-to-left");
      $(".sidebar-item").toggleClass("active");
    }
  
    $(".a").on("click tap", function() {
      toggleSidebar();
    });
  
    $(document).keyup(function(e) {
      if (e.keyCode === 27) {
        toggleSidebar();
      }
    });

  });

function buyBook(bookId) {
    let csrftoken = Cookies.get('csrftoken');
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });
    $.ajax({
        type: 'get',
        url: "/user/buy/book",
        data: {
            book_id : bookId,
        },
        success: function(result) {
            console.log(result);
            console.log("#my" + bookId);
            $("#my" + bookId).html(result);
            }
    });
}

function moreInfo(bookId) {
    let csrftoken = Cookies.get('csrftoken');
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });
    $.ajax({
        type: 'get',
        url: "/user/show/book",
        data: {
            book_id : bookId,
        },
        success: function(result) {
            console.log(result);
            console.log("#my" + bookId);
            $("#info" + bookId).html(result);
            }
    });
}

function addBooks() {
    $("#main-div").load("/user/add-book", function() {
        $("#main-div").fadeIn('slow');
    })
}
