//   ==========REVIEW==============
$(document).ready(function()
{
    $('#rateForm').on('submit', function(e)
    {
    var id = $('#rateForm').attr('actionData');
    console.log("kip")
   
    url='project/rate/'+id 
    console.log(url)
    e.preventDefault();
    $.ajax({
        method:'POST',
        url:'/project/rate/'+id,
    data:{
        design:$('#design').val(),
        usability:$('#usability').val(),
        content:$('#content').val(),
       
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        }, 

        beforeSend: function () 
        {
            $('#rateBtn').text('Rating ...')
            swal({
                title:"Saving",
                text:"Loading . . .",
                timer: 2000,
              });
        },
        success: function(response) 
        {
                       
            if(response.success=="success")
            {   
                swal({
                    title:"Saved",
                    icon:"success",
                    timer: 2000,
                  });                     
            }
            if(response.error=="error")
            {
                swal({
                    title:"Error",
                    text:"You have already rated this project!!",
                    icon:"error",
                    timer: 4000,
                  });  
            }
            setInterval('location.reload()', 2000); 

            $('#design').val(''),
            $('#usability').val(''),
            $('#content').val('')

            $('#rateBtn').text('Rate')
        },

        error: function (error) {
            alert('Error');
        }

    });
    
    });
});

// <!-- AVERAGE CHART -->
var average = $('#averageData').attr('data');
var remainder=10-average

    window.onload=function(){
    var data = {
    labels: [
    "Average",
    "kk"
    ],
    datasets: [
    {
        data: [average, remainder],
        backgroundColor: ["Green","#fff"],
        hoverBackgroundColor: [
        "#FF6283","#36A2EB"
        ]
    }]
};
var promisedDeliveryChart = new Chart(document.getElementById('myChart'), {
    type: 'doughnut',
    data: data,
    options: {
    responsive: true,
    legend: {
        display: false
    },
    pieHole: 0.9,
    }
});
Chart.pluginService.register({
    beforeDraw: function(chart) {
    var width = chart.chart.width,
        height = chart.chart.height,
        ctx = chart.chart.ctx;
    ctx.restore();
    var fontSize = (height / 194).toFixed(2);
    ctx.font = fontSize + "em sans-serif";
    ctx.textBaseline = "middle";
    var text = "Average "+average,
    textX = Math.round((width - ctx.measureText(text).width) / 2),
        textY = height / 2;
    ctx.fillText(text, textX, textY);
    ctx.save();
    }
});
    }
