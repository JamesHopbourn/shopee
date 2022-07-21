javascript:(() => {
document.querySelector("body > div:nth-child(2) > div.full-screen-container > div > div > div > div.product-edit__main > section:nth-child(5) > div > div:nth-child(1) > div.edit-input.edit-text-mini > div > div > div > div > div > input").value='0.8';
var evt = document.createEvent('HTMLEvents');
evt.initEvent('input', false, true);
document.querySelector("body > div:nth-child(2) > div.full-screen-container > div > div > div > div.product-edit__main > section:nth-child(5) > div > div:nth-child(1) > div.edit-input.edit-text-mini > div > div > div > div > div > input").dispatchEvent(evt);


document.querySelector("body > div:nth-child(2) > div.full-screen-container > div > div > div > div.product-edit__main > section:nth-child(6) > div > div:nth-child(1) > div.edit-input.edit-main > div > div > div.shopee-popover__ref > div > div > input").value='3';
var evt = document.createEvent('HTMLEvents');
evt.initEvent('input', false, true);
document.querySelector("body > div:nth-child(2) > div.full-screen-container > div > div > div > div.product-edit__main > section:nth-child(6) > div > div:nth-child(1) > div.edit-input.edit-main > div > div > div.shopee-popover__ref > div > div > input").dispatchEvent(evt);
})();