$(document).ready(function(){ 
    $.get('/c/content/notice', function(data){
               $('#notice').html(data);
           });
           
    $.get('/t/etest/testlist', function(data){
               $('#tests').html(data);
           });
           
    $('#prev').click(function(){
        var test_action;
        action = $(this).attr("test-action");
        $.get('/t/etest/sr/' + action, function(data){
                   // alert(data);
                   $('#test_area').html(data);
               });
    });
    
    $('#next').click(function(){
        var test_action;
        action = $(this).attr("test-action");
        $.get('/t/etest/sr/' + action, function(data){
                   // alert(data);
                   $('#test_area').html(data);
               });
    });
    
    $('[name=ans]').click(function(){
        var ans_action;
        ans = $(this).attr("ans-action");
        $.get('/t/etest/ans/' + ans, function(data){
                   // alert(data);
                   $('#ans_area').html(data);
               });
    });

       
});

