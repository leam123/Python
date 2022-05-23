/*$(document).ready(function () {

	function increaseValue() {
		var value = parseInt(document.getElementById('number').value, 10);
		value = isNaN(value) ? 0 : value;
		value++;
		document.getElementById('number').value = value;
	}

	function decreaseValue() {
		var value = parseInt(document.getElementById('number').value, 10);
		value = isNaN(value) ? 0 : value;
		value < 1 ? value = 1 : '';
		value--;
		document.getElementById('number').value = value;
	}
});*/

$(document).ready(function () {
	var date = new Date();

	var day = date.getDate();
	var month = date.getMonth() + 1;
	var year = date.getFullYear();

	if (month < 10) month = "0" + month;
	if (day < 10) day = "0" + day;

	var today = year + "-" + month + "-" + day;


	document.getElementById('dateRegistered').value = today;
});




/*alert-error*/
$(document).ready( function () {
    setTimeout(function(){
        if ($('#msgE').length > 0) {
            $('#msgE').remove();
        }
    }, 5000)
});

/* filter image format only */
/*$(document).ready( function () {
	var upload=document.getElementById("image1");
	var array=["image/jpg","image/png","image/jpeg"];
	upload.accept=array;
	upload.addEventListener("change",()=>{

	console.log(upload.value)
	})

	var upload2=document.getElementById("image2");
	var array2=["image/jpg","image/png","image/jpeg"];
	upload2.accept=array2;
	upload2.addEventListener("change",()=>{

	console.log(upload2.value)
	})

	var upload3=document.getElementById("image3");
	var array3=["image/jpg","image/png","image/jpeg"];
	upload3.accept=array3;
	upload3.addEventListener("change",()=>{

	console.log(upload3.value)
	})
});*/

function preview_image1(event) {
	var fileName = document.getElementById("image1").value;
    var idxDot = fileName.lastIndexOf(".") + 1;
    var extFile = fileName.substr(idxDot, fileName.length).toLowerCase();
    if (extFile=="jpg" || extFile=="jpeg" || extFile=="png"){
        var reader = new FileReader();
		reader.onload = function(){
			var output = document.getElementById('output_image1');
			output.src = reader.result;
		}
		reader.readAsDataURL(event.target.files[0]);
    }else{
        alert("Sorry. Only jpg/jpeg and png files are allowed.");
        document.getElementById("image1").value = "";
    } 
}

function preview_image2(event) {
	var fileName = document.getElementById("image2").value;
    var idxDot = fileName.lastIndexOf(".") + 1;
    var extFile = fileName.substr(idxDot, fileName.length).toLowerCase();
    if (extFile=="jpg" || extFile=="jpeg" || extFile=="png"){
        var reader = new FileReader();
		reader.onload = function(){
			var output = document.getElementById('output_image2');
			output.src = reader.result;
		}
		reader.readAsDataURL(event.target.files[0]);
    }else{
        alert("Sorry. Only jpg/jpeg and png files are allowed.");
        document.getElementById("image2").value = "";
    } 
}

function preview_image3(event) {
	var fileName = document.getElementById("image3").value;
    var idxDot = fileName.lastIndexOf(".") + 1;
    var extFile = fileName.substr(idxDot, fileName.length).toLowerCase();
    if (extFile=="jpg" || extFile=="jpeg" || extFile=="png"){
        var reader = new FileReader();
		reader.onload = function(){
			var output = document.getElementById('output_image3');
			output.src = reader.result;
		}
		reader.readAsDataURL(event.target.files[0]);
    }else{
        alert("Sorry. Only jpg/jpeg and png files are allowed.");
        document.getElementById("image3").value = "";
    } 
}

