
// <!-- ------------sort table------------------>
// Fonction pour convertir une chaîne en une valeur comparable (nombre ou chaîne en minuscules)
function getComparableValue(td) {
    let textContent = td.innerText.replace(/,/g, '').replace(/\s/g, '');
    let value = parseFloat(textContent);
    return !isNaN(value) ? value : textContent.toLowerCase();
}

// Fonction de tri
function sortTableByColumn(table, columnIndex, asc = true) {
    const dirModifier = asc ? 1 : -1;
    const tBody = table.tBodies[0];
    const rows = Array.from(tBody.querySelectorAll('tr'));

    const sortedRows = rows.sort((a, b) => {
        const aColText = getComparableValue(a.querySelector(`td:nth-child(${columnIndex + 1})`));
        const bColText = getComparableValue(b.querySelector(`td:nth-child(${columnIndex + 1})`));

        return aColText > bColText ? (1 * dirModifier) : (-1 * dirModifier);
    });

    while (tBody.firstChild) {
        tBody.removeChild(tBody.firstChild);
    }

    tBody.append(...sortedRows);

    table.querySelectorAll('th').forEach(th => th.classList.remove('th-sort-asc', 'th-sort-desc'));
    table.querySelector(`th:nth-child(${columnIndex + 1})`).classList.toggle('th-sort-asc', asc);
    table.querySelector(`th:nth-child(${columnIndex + 1})`).classList.toggle('th-sort-desc', !asc);
}

document.addEventListener('DOMContentLoaded', () => {
    // Sélectionner toutes les tables avec la classe 'table-sortable'
    const tables = document.querySelectorAll('.table');

    tables.forEach(table => {
        const headers = table.querySelectorAll('th');
        headers.forEach((header, index) => {
            if (!header.classList.contains('no-sort')) {
                header.addEventListener('click', () => {
                    const currentIsAscending = header.classList.contains('th-sort-asc');
                    sortTableByColumn(table, index, !currentIsAscending);
                });
            }
        });
    });
});

