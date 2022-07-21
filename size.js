javascript:(() => {
document.getElementsByClassName('repeater-add shopee-button shopee-button--normal')[0].click();

var size_array = ["尺码", "36","36.5","37","37.5","38","38.5","39","40","40.5","41","42","42.5","43","44","44.5","45","46"];

setTimeout(function(){
	for (let i = 0; i < size_array.length-2; i++) {
		document.getElementsByClassName('repeater-add shopee-button shopee-button--normal')[0].click();
	}
}, 1000);

setTimeout(function(){
	for (let i = 0; i < size_array.length; i++) {
		var element = document.getElementsByClassName('shopee-input__input')[i+3];
		element.value = size_array[i];
		var evt = document.createEvent('HTMLEvents');
		evt.initEvent('input', false, true);
		element.dispatchEvent(evt);
	}
}, 1000);
})();