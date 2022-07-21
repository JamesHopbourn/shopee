javascript:(() => {
var element = document.getElementsByClassName('shopee-input__input')[21];
element.value = 99;
var evt = document.createEvent('HTMLEvents');
evt.initEvent('input', false, true);
element.dispatchEvent(evt);
document.getElementsByClassName('shopee-button shopee-button--primary shopee-button--normal br')[0].click()
})();