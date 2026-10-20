document.addEventListener("DOMContentLoaded", function () {

    // 1. Ask for confirmation before deleting an expense
    var deleteForms = document.querySelectorAll("form.delete-form");
    deleteForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            if (!confirm("Delete this expense?")) {
                event.preventDefault();
            }
        });
    });

    // 2. Filter the expense table as the user types in the search box
    var search = document.getElementById("search");
    if (search) {
        search.addEventListener("input", function () {
            var term = search.value.toLowerCase();
            var rows = document.querySelectorAll("tr.expense-row");
            rows.forEach(function (row) {
                var text = row.textContent.toLowerCase();
                row.classList.toggle("hidden", !text.includes(term));
            });
        });
    }
});