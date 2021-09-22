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




//   ==========REGISTER==============

$(document).ready(function()
{
    console.log("kkkk")


    $('#profilePhotoForm').on('submit', function(e)
    {    
        var f_obj = $("#profile_photo").get(0).files[0]; 

        var data = new FormData();                                      //Create formdata objects to facilitate file transfer to the back end
        data.append("file",f_obj);
        data.append("csrfmiddlewaretoken",$('input[name=csrfmiddlewaretoken]').val());
// "csrfmiddlewaretoken", "{{ csrf_token }}"

        console.log(data);

    e.preventDefault();
     $.ajax({
        method:'POST',
        url:'profile_photo',
        data: data,
        //   csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        // }, 

        beforeSend: function () 
        {
            $('#updateProfileImgBtn').text('Save ...')
        },
        success: function(response) 
        {  
            console.log(profile_photo)
                       
            if(response.error=="username")
            {
                $('#error').text(response.msg).fadeIn("fast")

                setTimeout(function() {
                    $('#error').fadeOut("slow")
                }, 4000);   
            }   

            else if(response.success=="success")
            {
                $('#success').text(response.msg).fadeIn("fast")
                $('#profile_photo').val(''),
                    setTimeout(function() {
                        $('#success').fadeOut("fast")
                    }, 4000);      
            }
            $('#updateProfileImgBtn').text('Save')
        },

        error: function (error) {
            alert('Error');
        }

    });
    
    });
});



// $(document).ready(function()
//  {

//     $('#profilePhotoForm').on('submit', function(e)
//    {


// jQuery.noConflict();	
// formdata = new FormData();		
// jQuery("#image_to_upload").on("change", function() {
//     var file = this.files[0];
//     if (formdata) {
//         formdata.append("image", file);
//         jQuery.ajax({
//             url: "profile_photo",
//             type: "POST",
//             data: formdata,
//             processData: false,
//             contentType: false,
//             success:function(){}
//         });
//     }						
// });


// });
// });

// API
document.getElementById("usersApi").innerHTML=document.location.hostname+"/api/users/";
document.getElementById("projectsApi").innerHTML=document.location.hostname+"/api/projects/";