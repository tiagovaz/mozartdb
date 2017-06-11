    $(document).ready(function() {
        $('#dataTables-example').DataTable({
               "language": {
                   "lengthMenu": "Afficher _MENU_",
                   "zeroRecords": "Aucun résultat",
                   "info": "Page _PAGE_ de _PAGES_",
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
                stateSave: true
        });
    });
