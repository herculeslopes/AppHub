let card_wrappers = document.getElementsByClassName('software-card-wrapper');
console.log('fasd');

for (let i = 0; i < card_wrappers.length; i++) {
    card_wrappers[i].addEventListener('click', (event) => {
        let card = event.currentTarget;
        let id = card.getAttribute('id');

        // window.location.replace('../software?id=' + id);
        window.location.href = '../software?id=' + id;

    }, false)
}