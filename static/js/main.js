// DRAG and DROP
const dropItems = document.getElementById('drop_container');

new Sortable(dropItems, {
    animation: 350,
    chosenClass: "sortable-chosen",
    dragClass: "sortable-drag",
    swapThreshold: 1,
    direction: 'horizontal',
    store: {
        // keep the order of the list
        set: (sortable) => {
            const order = sortable.toArray()
            localStorage.setItem(sortable.options.group.name, order.join('|'))
        },
        // get the order of the list
        get: (sortable) => {
            const order = localStorage.getItem(sortable.options.group.name)
            return order ? order.split('|') : []
        }
    }
});


// modal info box
let icon = document.getElementById("icon-question");
let info = document.getElementById("info-box");

function displayModal() {
    info.style.display = 'block';
    setTimeout(function () {
        info.style.display = 'none';
    }, 5000);
}

icon.addEventListener("mouseover", displayModal, false);
