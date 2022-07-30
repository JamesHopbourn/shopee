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

    function isJsonString(str) {
        try {
            JSON.parse(str);
        } catch (e) {
            return false;
        }
        return true;
    }

    var data = document.getElementsByTagName("script");
    for (var i = 0; i < data.length; i++) {
        if (isJsonString(data[i].innerText) && JSON.parse(data[i].innerText).hasOwnProperty('name') && JSON.parse(data[i].innerText)['name'].indexOf('StockX') == -1) {
            product_id = document.getElementsByClassName('chakra-text css-1fo8xgy')[0].textContent;
            copyToClipboard(`${JSON.parse(data[i].innerText)['name']} ${product_id}`.replace("'", ''));
        }
    }
})();