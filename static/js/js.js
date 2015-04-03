$( document ).ready(function() {

   console.log( "Script initiated!" );

   $('.edit').hide();
   $('#save').hide();
   $('#project-name').hide();

   $('#edit').click(function(){
            $(this).slideUp(500);
            $('#save').slideDown(500);
            $('.edit').slideDown(500);
            $('.project_data').slideUp(500);
   });


});