
function logoutFunction () {
    $("logout").load("frontend/logout.html")
};

function notifyFunction() {
    if (confirm("Email sent!")) {
        ;
    } else {
       ;
    }
};    

$(".delete-row").click(function(){
$(this).parents("tr").remove();
});

 $(document).ready(function(){
    $('select').formSelect();
  });
        
$(document).ready(function(){
    $(".modify-button").click(function(){
        $("#001").replaceWith();
    });
});

$(document).ready(function($)
{
$(".dropdown-trigger").dropdown();
$(document).ready(function(){
    $('.datepicker').datepicker();
  });
 (function($) {
   $(function() {

     $('.button-collapse').sideNav();
     $('select').material_select();
     $('.dropdown-button').dropdown();

   }); // end of document ready
  });
 })(jQuery);

