<?php

  require("src/init.php");

  //si no tiene sesión iniciada, le mandamos al login
  if (!isset($_SESSION['nombre'])) {
    header("Location: login.php");
    die();
  }

?>
<html>
<head>
  <link rel="stylesheet" type="text/css" media="all" href="css/estilo.css">
</head>
<body>
<h1>Bienvenido!!</h1>
  <?php include('menu.php')?>
  <p>PRIVADO: Información solo para gente autentificada</p>
</body>
</html>
