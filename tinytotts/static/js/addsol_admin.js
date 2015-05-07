$(document).ready(function(){ 
    $.get('/c/content/notice', function(data){
               $('#notice').html(data);
           });
           
    $.get('/t/etest/testlist', function(data){
               $('#tests').html(data);
           });
    
    $('#start').click(function(){
        var test_action;
        action = $(this).attr("test-action");
        $.get('/t/etest/sr/' + action, function(data){
                   // alert(data);
                   $('#test_area').html(data);
                   $('#start').hide();
               });
    });

});


function admin_nav(action)
{
    alert(action);
}


// Record Marks
function marks( ans )
{
    //example use
    var scriptUrl = "/t/etest/ans/" + ans;
    var msg=getURL(scriptUrl);
    $('#ans_area').html(msg);
}

function getURL(url){
    return $.ajax({
        type: "GET",
        url: url,
        cache: false,
        async: false
    }).responseText;
}



