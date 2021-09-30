$(document).ready(function(){
    $(".profileBtn").click(function()
    {
        $( "#updateProfile").fadeIn( "fast" );
        $( "#api").fadeOut( "fast" );
        $( "#myProjects").fadeOut( "fast" );
        $( "#updatePassword").fadeOut( "fast" );
        
    });

    $(".projectsBtn").click(function()
    {
        $( "#myProjects").fadeIn("fast");
        $( "#api").fadeOut("fast");
        $( "#updateProfile").fadeOut( "fast" );
        $( "#updatePassword").fadeOut( "fast" );
    });

    $(".apiBtn").click(function()
    {
        $( "#updateProfile").fadeOut("fast");
        $( "#api").fadeIn("fast");
        $( "#myProjects").fadeOut( "fast" );
        $( "#updatePassword").fadeOut( "fast" );
    });

    $(".passwordBtn").click(function()
    {
        $( "#api").fadeOut("fast");
        $( "#updatePassword").fadeIn("fast");
        $( "#myProjects").fadeOut( "fast" );
        $( "#updateProfile").fadeOut( "fast" );
    });


});



// API
// document.getElementById("usersApi").innerHTML=document.location.hostname+"/api/users/";
// document.getElementById("projectsApi").innerHTML=document.location.hostname+"/api/projects/";

// document.getElementById( 'usersApiLink' ).href="https://"+window.location.hostname+"/api/users/";
// document.getElementById( 'projectsApiLink' ).href="https://"+window.location.hostname+"/api/projects/";