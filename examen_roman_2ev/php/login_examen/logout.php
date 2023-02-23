<?php

    require("src/init.php");


    if (isset($_SESSION['nombre'])) {
        unset($_SESSION['nombre']);
    }

    //Esto es lo necesario
    session_destroy();
    //Esta destrucción de cookie es opcional
    setcookie("PHPSESSID", null, time()-1);
    
    header('Location: '.$paginaAnterior);
    die();

?>