<?php

    //para que si venimos de una privada, nos mantenga la página anterior visitada
    $paginaAnterior = (isset($_SESSION['anterior'])) ? $_SESSION['anterior']:$_SERVER['REQUEST_URI'];
    //mientras no sea login, ni register, no actualices $session de anterior
    if ($_SERVER["REQUEST_URI"]!= "/login.php" && $_SERVER["REQUEST_URI"] != "/register.php"){
        $_SESSION["anterior"] = $_SERVER["REQUEST_URI"];
    }

?>