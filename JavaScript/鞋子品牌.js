javascript:(() => {
document.querySelector("body > div:nth-child(2) > div.full-screen-container > div > div > div > div.product-edit__main > section:nth-child(3) > div > div.attribute-select-container > div.attribute-select-list > div:nth-child(1) > div > div.edit-input.edit-text > div > div > div > div > div > div > div.shopee-selector__inner.line-clamp--1").click();

setTimeout(function(){
document.evaluate("/html/body/div[8]/ul/div[1]/div/input", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.value = 'Air Jordan';
var evt = document.createEvent('HTMLEvents');
evt.initEvent('input', false, true);
document.evaluate("/html/body/div[8]/ul/div[1]/div/input", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.dispatchEvent(evt);
}, 1000);

setTimeout(function(){
document.querySelector("body > div:nth-child(48) > ul > div.shopee-select__menu.shopee-select__menu_no_top_radius > div > div:nth-child(1)").click()
}, 1000);
document.querySelector("body > div:nth-child(48) > ul > div.shopee-select__menu.shopee-select__menu_no_top_radius > div > div:nth-child(1)").click()
})();