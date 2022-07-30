javascript: (function() { 
function copyToClipboard(text) {
    if (window.clipboardData && window.clipboardData.setData) {
        return clipboardData.setData("Text", text);
    } else if (document.queryCommandSupported && document.queryCommandSupported("copy")) {
        var textarea = document.createElement("textarea");
        textarea.textContent = text;
        textarea.style.position = "fixed";
        document.body.appendChild(textarea);
        textarea.select();
        try {
            return document.execCommand("copy");
        } catch (ex) {
            console.warn("Copy to clipboard failed.", ex);
            return false;
        } finally {
            document.body.removeChild(textarea);
        }
    }
}

var data = document.querySelectorAll("script[type='application/ld+json']");
for (var i = 0; i < data.length; i++) {
    item = data[i].innerText;
    if (JSON.parse(item).hasOwnProperty('name') && JSON.parse(item)['name'].indexOf('StockX') == -1) {
        product_id = document.getElementsByClassName('chakra-text css-1fo8xgy')[0].textContent;
        copyToClipboard(`${JSON.parse(item)['name']} ${product_id}`.replace("'", ''));
    }
}
})();