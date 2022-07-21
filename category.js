javascript:(() => {
setTimeout(function(){
	document.evaluate("/html/body/div[1]/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[1]/li[24]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()
}, 0);

setTimeout(function(){
	document.evaluate("/html/body/div[1]/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[2]/li[2]/p", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()
}, 500);

setTimeout(function(){
	document.evaluate("/html/body/div[1]/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[3]/li[1]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()
}, 500);


setTimeout(function(){
	document.evaluate("/html/body/div[1]/div[2]/div/div/div/button", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()
}, 500);
})();