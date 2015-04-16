$(document).ready(function(){ 
    $.get('/c/content/notice', function(data){
               $('#notice').html(data);
           });
           
    $('#prev').click(function(){
        alert('Hello dude prev');
        var test_action;
        test_action = $(this).attr("test-action");
        alert(test_action);
        $.get('/t/etests/etest/', {category_id: catid}, function(data){
                   $('#like_count').html(data);
                   $('#likes').hide();
               });
    });
    
    $('#next').click(function(){
        $.get('/t/etest/sr/2', function(data){
                   // alert(data);
                   $('#test_area').html(data);
                   $('#subm').hide();
               });
    });
       
});

