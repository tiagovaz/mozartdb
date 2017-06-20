    $(document).ready(function() {
        $('#dataTables-example').DataTable({
               "language": {
                   "lengthMenu": "Afficher _MENU_",
                   "zeroRecords": "Aucun résultat",
                   "info": "_START_ à _END_ d'un total de <b>_TOTAL_</b> resultáts trouvés",
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
                stateSave: true
        });
    });
