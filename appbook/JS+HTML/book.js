const domain = 'http://localhost:8000/';

let list = document.getElementById('list');
let listLoader = new XMLHttpRequest();

listLoader.addEventListener('readystatechange', () => {
    if (listLoader.readyState == 4) {
        if (listLoader.status == 200) {
            let data = JSON.parse(listLoader.responseText);
            let s = '<ul>', d;
            for (let i = 0; i < data.length; i++) {
                d = data[i];
                s += '<li>' + d.name + '<a href="' + domain + 'api/' + d.id + '/" class=""detail"></a></li>';
            }
            s += '</ul>'
            list.innerHTML = s;
            let links = list.querySelectorAll('ul li a.detail');
            links.forEach((link) => {
                link.addEventListener('click', bookLoad);})
        } else
            window.alert(listLoader.statusText);
    }
});

function listLoad() {
    listLoader.open('GET', domain + 'api/', true);
    listLoader.send();
}
listLoad();

let id =document.getElementById('id');
let name = document.getElementById('name');
let bookLoader = new XMLHttpRequest();

bookLoader.addEventListener('readystatechange', () => {
    if (bookLoader.readyState == 4) {
        if (bookLoader.status == 200) {
            let data = JSON.parse(bookLoader.responseText);
            id.value = data.id;
            name.value = data.name;
        } else
            window.alert(bookLoader.statusText);
    }
});

function bookLoad(evt) {
    evt.preventDefault();
    bookLoader.open('GET', evt.target.href, true);
    bookLoader.send();
}
