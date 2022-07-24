javascript:(() => {
document.querySelector("body > div:nth-child(2) > div.full-screen-container > div > div > div > div.product-edit__main > section:nth-child(3) > div > div.attribute-select-container > div.attribute-select-list > div:nth-child(2) > div > div.edit-input.edit-text > div > div > div > div > div > div > div.shopee-selector__inner.line-clamp--1").click();

setTimeout(function(){
document.querySelector("body > div.shopee-popper.shopee-select-popover-content.popover.adv-select-popover > ul > div.shopee-select__menu.shopee-select__menu_no_top_radius > div > div:nth-child(4)").click();
}, 500);

setTimeout(function(){
document.getElementsByClassName('repeater-add shopee-button shopee-button--normal')[0].click();
}, 500);

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