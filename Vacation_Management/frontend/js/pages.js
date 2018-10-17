// Send a notification via email: 
function sendMail() {
   window.location.href = "mailto:user@example.com?subject=Subject&body=message%20goes%20here";
};

// Log out:
function logoutFunction () {
    $("logout").load("frontend/logout.html")
};   

//Delete a row from the table
$(".delete-row").click(function(){
$(this).parents("tr").remove();
});

//Display selected item 
 $(document).ready(function(){
    $('select').formSelect();
  });

//Modify changes
$(document).ready(function(){
    $(".modify-button").click(function(){
        $("#001").replaceWith();
    });
});

// Datepicker from calendar
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

   });
  });
 })(jQuery);
