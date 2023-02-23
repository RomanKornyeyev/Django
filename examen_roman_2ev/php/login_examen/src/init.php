<?php 

    require("config.php");
    require("DWESBaseDatos.php");

    $db = DWESBaseDatos::obtenerInstancia();
    $db->inicializa(
        $CONFIG['db_name'],
        $CONFIG['db_user'],
        $CONFIG['db_pass']
    );

    session_start();

    require("paginaAnterior.php");

    //datos de usuario (nombre y grupo), de serie anónimos
    $userGroup = "anónimo";
    $userName = "anónimo";

    //si está session de nombre, significa que el user está logueado y hay $_SESSION['nb_grupo'] y $_SESSION['nombre'] (obviamente)
    if (isset($_SESSION['nombre'])) {
        //cargamos la info del user en las variables
        //grupo del usuario
        $userGroup = $_SESSION['nb_grupo'];
        //y username del usuario
        $userName = $_SESSION['nombre'];
    }

    //función para evitar crossite scripting, la uso en el login
    function clean_input($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }

?>