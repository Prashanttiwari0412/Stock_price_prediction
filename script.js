$(document).ready(function(){
    $("select.type").change(function(){
        var selectedType = $(this).children("option:selected").val();
        volumeField = document.getElementById("volume");
        adjCloseField = document.getElementById("adj_close");
        timeField = document.getElementById("time");
        if(selectedType == "NIFTY"){
            $(volumeField).hide();
            $(adjCloseField).hide();
            $(time).show();
        }else{
            $(volumeField).show();
            $(adjCloseField).show();
            $(time).hide();
        }
    });
});