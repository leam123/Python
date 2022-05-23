$(document).ready(function () {

     // DATE FILTER FOR THE FIRST TABLE 
    let initialTableSettings = {
        //"bFilter": false,
        "pageLength" : 5,
        "lengthMenu" : [[5, 10, 20, -1], [5, 10, 20, 30, 40, 50]],
        dom: 'lrtBi<"posR"p>',
        buttons: [
            'excel'
        ]
    }

    $.fn.dataTable.ext.search.push(
        function (settings, data, dataIndex) {
            var min = $('#min-date').datepicker("getDate");
            var max = $('#max-date').datepicker("getDate");
            // need to change str order before making  date obect since it uses a new Date("mm/dd/yyyy") format for short date.
            var startDate = new Date(data[0])
            if (min == null && max == null) { return true; }
            if (min == null && startDate <= max) { return true;}
            if(max == null && startDate >= min) {return true;}
            if (startDate <= max && startDate >= min) { return true; }
            return false;
        }
    );

    $("#min-date").datepicker({ onSelect: function () { table.draw(); }, changeMonth: true, changeYear: true , dateFormat:"dd/mm/yy"});
    $("#max-date").datepicker({ onSelect: function () { table.draw(); }, changeMonth: true, changeYear: true, dateFormat:"dd/mm/yy" });
    var table = $('#example').DataTable(initialTableSettings);

    // Event listener to the two range filtering inputs to redraw on input
    $('#min-date, #max-date').change(function () {
        table.draw();
    });
});


$(document).ready(function () {

    // DATE FILTER FOR THE SECOND TABLE 
    let initialTableSettings = {
        //"bFilter": false,
        "pageLength" : 5,
        "lengthMenu" : [[5, 10, 20, -1], [5, 10, 20, 30, 40, 50]],
        /*dom: '<"posR"f>lrtBi<"posR"p>',*/
        dom: 'lrtBi<"posR"p>',
        buttons: [
            'excel'
        ]
        
    }

    $.fn.dataTable.ext.search.push(
        function (settings, data, dataIndex) {
            var min = $('#min').datepicker("getDate");
            var max = $('#max').datepicker("getDate");
            // need to change str order before making  date obect since it uses a new Date("mm/dd/yyyy") format for short date.
            var startDate = new Date(data[0])
            if (min == null && max == null) { return true; }
            if (min == null && startDate <= max) { return true;}
            if(max == null && startDate >= min) {return true;}
            if (startDate <= max && startDate >= min) { return true; }
            return false;
        }
    );

    $("#min").datepicker({ onSelect: function () { table.draw(); }, changeMonth: true, changeYear: true , dateFormat:"dd/mm/yy"});
    $("#max").datepicker({ onSelect: function () { table.draw(); }, changeMonth: true, changeYear: true, dateFormat:"dd/mm/yy" });
    var table = $('#example2').DataTable(initialTableSettings);

    // Event listener to the two range filtering inputs to redraw on input
    $('#min, #max').change(function () {
        table.draw();
    });

});


/*alert-info*/
$(document).ready( function () {
    setTimeout(function(){
        if ($('#msgInfo').length > 0) {
            $('#msgInfo').remove();
        }
    }, 2000)
});

/*CUSTOM SEARCH BAR*/
$(document).ready( function () {
    oTable = $('#example2').DataTable();  
    $('#myInput').keyup(function(){
        oTable.search($(this).val()).draw() ;
    })

    oTable1 = $('#example').DataTable();  
    $('#myInput1').keyup(function(){
        oTable1.search($(this).val()).draw() ;
    })

});

function runSpeechRecognition() {
    // new speech recognition object
    var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
    var recognition = new SpeechRecognition();
    var table = $('#example2').DataTable();
    // This runs when the speech recognition service starts
   /* recognition.onstart = function() {
        console.log("We are listening. Try speaking into the microphone.");
    };

    recognition.onspeechend = function() {
        // when user is done speaking
        recognition.stop();
    }*/
                  
    // This runs when the speech recognition service returns result
    recognition.onresult = function(event) {
        var transcript = event.results[0][0].transcript;
        var confidence = event.results[0][0].confidence;
        document.getElementById('myInput').value = transcript;

       table.search( transcript ).draw();
    };
                  
    // start recognition

    recognition.start();
}

/*alert-success*/
$(document).ready( function () {
    setTimeout(function(){
        if ($('#msg').length > 0) {
            $('#msg').remove();
        }
    }, 1000)
});

/*alert-warning*/
$(document).ready( function () {
    setTimeout(function(){
        if ($('#msgW').length > 0) {
            $('#msgW').remove();
        }
    }, 2000)
});

/* else part */
function preview1(event) {
    var fileName = document.getElementById("img1").value;
    var idxDot = fileName.lastIndexOf(".") + 1;
    var extFile = fileName.substr(idxDot, fileName.length).toLowerCase();
    if (extFile=="jpg" || extFile=="jpeg" || extFile=="png"){
        var reader = new FileReader();
        reader.onload = function(){
            var output = document.getElementById('output_img1');
            output.src = reader.result;
        }
        reader.readAsDataURL(event.target.files[0]);
    }else{
        alert("Sorry. Only jpg/jpeg and png files are allowed.");
        document.getElementById("img1").value = "";
    } 
}

function preview2(event) {
    var fileName = document.getElementById('img2').value;
    var idxDot = fileName.lastIndexOf(".") + 1;
    var extFile = fileName.substr(idxDot, fileName.length).toLowerCase();
    if (extFile=="jpg" || extFile=="jpeg" || extFile=="png"){
        var reader = new FileReader();
        reader.onload = function(){
            var output = document.getElementById('output_img2');
            output.src = reader.result;
        }
        reader.readAsDataURL(event.target.files[0]);
    }else{
        alert("Sorry. Only jpg/jpeg and png files are allowed.");
        document.getElementById('img2').value = "";
    } 
}

function preview3(event) {
    var fileName = document.getElementById("img3").value;
    var idxDot = fileName.lastIndexOf(".") + 1;
    var extFile = fileName.substr(idxDot, fileName.length).toLowerCase();
    if (extFile=="jpg" || extFile=="jpeg" || extFile=="png"){
        var reader = new FileReader();
        reader.onload = function(){
            var output = document.getElementById('output_img3');
            output.src = reader.result;
        }
        reader.readAsDataURL(event.target.files[0]); 
    }else{
        alert("Sorry. Only jpg/jpeg and png files are allowed.");
        document.getElementById("img3").value = "";
    } 
}

