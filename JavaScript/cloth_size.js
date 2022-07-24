javascript:(() => {
for (let i = 0; i < 3; i++) {
	document.getElementsByClassName('repeater-add shopee-button shopee-button--normal')[1].click();
}

size_mapper = [
	["div[1]/div[2]/div/div/div/div/div/input", "XS（PP）"],
	["div[2]/div[2]/div/div/div/div/div/div/input", "S（p）"],
	["div[2]/div[2]/div[2]/div/div/div/div/div/input", "M（M）"],
	["div[2]/div[2]/div[3]/div/div/div/div/div/input", "L（g）"],
	["div[2]/div[2]/div[4]/div/div/div/div/div/input", "XL（gg）"]
];

setTimeout(function(){
	for (let i = 0; i < size_mapper.length; i++){
		var element = document.evaluate("/html/body/div[1]/div[2]/div/div/div/div[1]/section[3]/div/div[1]/div[1]/div[2]/div[2]/div/" + size_mapper[i][0], document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
		element.value = size_mapper[i][1];
		var evt = document.createEvent('HTMLEvents');
		evt.initEvent('input', false, true);
		element.dispatchEvent(evt);
	}
}, 500);
})();