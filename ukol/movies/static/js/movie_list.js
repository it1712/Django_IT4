$(document).ready(function () {
    $('table').DataTable({
        "aaSorting": [],
        columnDefs: [{
            orderable: false,
            targets: 2
        }],
        searching: false,
        paging: false,
        info: false,
    });
    $('.dataTables_length').addClass('bs-select');
});