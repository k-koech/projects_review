// switching in modal
$(".forgot_pass").click(function() 
{
    $( ".forgot_password" ).fadeIn( "fast" );
    $( ".login" ).fadeOut( "fast" );
});

$(".forgot_password_login").click(function() 
{
    $( ".forgot_password" ).fadeOut( "fast" );
    $( ".login" ).fadeIn( "fast" );
});

$(".login_register").click(function() 
{
    $( ".register" ).fadeIn( "fast" );
    $( ".login" ).fadeOut( "fast" );
});

$(".register_login").click(function() 
{
    $( ".login" ).fadeIn( "fast" );
    $( ".register" ).fadeOut( "fast" );
    
});

//   ==========REGISTER==============
$(document).ready(function()
{
    $('#registerForm').on('submit', function(e)
    {
    e.preventDefault();
    $.ajax({
        method:'POST',
        url:'register',
    data:{
        username:$('#username').val(),
        email:$('#e-mail').val(),
        phone:$('#phone').val(),
        password:$('#pass').val(),
        confirm_password:$('#confirm_password').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        }, 

        beforeSend: function () 
        {
                       
            $('#registerBtn').text('Saving ...')
           
        },
        success: function(response) 
        {
            console.log(response)
            if(response.error=="username")
            {
                $('#errors').text(response.msg).fadeIn("fast")

                setTimeout(function() {
                    $('#errors').fadeOut("slow")
                }, 4000);   
            }   

            else if(response.error=="email")
            {
                $('#errors').text(response.msg).fadeIn("fast")
                setTimeout(function(){
                    $('#errors').text(response.msg).fadeOut("slow")
                }, 4000);   
            }

            else if(response.error=="password_match")
            {                
                $('#errors').text(response.msg).fadeIn("fast")
                   setTimeout(function() {
                    $('#errors').fadeOut("fast")
                    }, 4000);   
            }
            else if(response.success=="success")
            {
                $('#errors').fadeOut("fast")
                $('#successes').text(response.msg).fadeIn("fast")

                $('#username').val(''),
                $('#e-mail').val(''),
                $('#phone').val(''),
                $('#pass').val(''),
                $('#confirm_password').val(''),

                    setTimeout(function() {
                        $('#successes').fadeOut("fast")
                    }, 4000);    
                        
            }
            $('#registerBtn').text('Register')
        },

        error: function (error) {
            alert('Error');
        }

    });
    
    });
});



//   ==========LOGIN==============
$(document).ready(function()
{
    $('#loginForm').on('submit', function(e)
    {
    e.preventDefault();
    $.ajax({
        method:'POST',
        url:'login',
    data:{
        email:$('#email').val(),
        password:$('#password').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        }, 

        beforeSend: function () 
        {
            $('#loginBtn').text('logging in ...')
        },
        success: function(response) 
        {
                       
            if(response.error=="credentials")
            {
                $('#error').text(response.msg).fadeIn("fast")

                setTimeout(function() {
                    $('#error').fadeOut("slow")
                }, 4000);   
            }   
            
            else if(response.success=="success")
            {
              $('#success').text(response.msg).fadeIn("fast")

              $('#email').val('')
              $('#password').val('')
                    setTimeout(function() {
                        $('#success').fadeOut("fast")
                    }, 4000);  
                    
                $('#login').html(
                    swal({
                        icon: "success",
                        text: "Logged in successfully, Redirecting ...",
                        timer: "3000"
                      })
                ).fadeIn("fast")

                setTimeout(function() 
                {
                    location.reload();
                }, 4000); 
                
            }


            $('#loginBtn').text('Register')
        },

        error: function (error) {
            alert('Error');
        }

    });
    
    });
});

