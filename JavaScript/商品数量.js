javascript:(() => {
	document.querySelector("body > div:nth-child(2) > div.full-screen-container > div > div > div > div.product-edit__main > section:nth-child(4) > div > div.product-tier-variation > div.info-panel > div:nth-child(1) > div.edit-main.batch-container > form > div:nth-child(2) > div > div > div > div > input").value = 99;
	var evt = document.createEvent('HTMLEvents');
	evt.initEvent('input', false, true);
	document.querySelector("body > div:nth-child(2) > div.full-screen-container > div > div > div > div.product-edit__main > section:nth-child(4) > div > div.product-tier-variation > div.info-panel > div:nth-child(1) > div.edit-main.batch-container > form > div:nth-child(2) > div > div > div > div > input").dispatchEvent(evt);
	document.querySelector("body > div:nth-child(2) > div.full-screen-container > div > div > div > div.product-edit__main > section:nth-child(4) > div > div.product-tier-variation > div.info-panel > div:nth-child(1) > div.edit-main.batch-container > button").click()
})();