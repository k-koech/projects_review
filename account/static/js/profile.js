$(document).ready(function(){
    $(".profileBtn").click(function()
    {
        $( "#updateProfile").fadeIn( "fast" );
        $( "#api").fadeOut( "fast" );
        $( "#myProjects").fadeOut( "fast" );
        
    });

    $(".projectsBtn").click(function()
    {
        $( "#updateProfile").fadeOut("fast");
        $( "#api").fadeOut("fast");
        $( "#myProjects").fadeIn( "fast" );
    });

    $(".apiBtn").click(function()
    {
        $( "#updateProfile").fadeOut("fast");
        $( "#api").fadeIn("fast");
        $( "#myProjects").fadeOut( "fast" );
    });


});



// API
document.getElementById("usersApi").innerHTML=document.location.hostname+"/api/users/";
document.getElementById("projectsApi").innerHTML=document.location.hostname+"/api/projects/";