// ex.js
var elExample = document.getElementById('example');
if (elExample) {
    var lastName = elExample.getAttribute('data-last-name');
    elExample.textContent = 'Hell5255 ' + lastName;
}
