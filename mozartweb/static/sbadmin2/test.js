    $(document).ready(function() {
        $('#dataTables-example').DataTable({
        dom: '<"row"<"col-sm-4"l><"col-sm-4"B><"col-sm-4"f>>rtip',
        buttons: [
            'excelHtml5',
            'csvHtml5',
            'pdfHtml5'
        ],
               "language": {
                   "lengthMenu": "Afficher _MENU_",
                   "zeroRecords": "Aucun résultat",
                   "info": "Page _PAGE_ de _PAGES_ <br> Entrées _START_ à _END_ d'un total de _TOTAL_ trouvées",
                   "infoFiltered":   "(filtrés de _MAX_ registres)",
                   "search":         "Rechercher :",
                   "infoEmpty": "No records available",
                   "infoFiltered": "(filtered from _MAX_ total records)",
                   "paginate": {
                       "first":      "Première",
                       "last":       "Dernière",
                       "next":       "Suivante",
                       "previous":   "Précedente"
                   }
               },
               "lengthMenu": [[25, 50, 100, -1], [25, 50, 100, "Tous"]],
                responsive: true,
                stateSave: true,
               "columnDefs": [
                       { "width": "4%", "targets": 0 },
                       { "width": "8%", "targets": 6 }
                ],
                "autoWidth": false,
        });
    });
