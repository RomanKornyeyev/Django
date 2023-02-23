<?php

  require("src/init.php");

  
  //si tiene sesión iniciada
  if (isset($_SESSION['nombre'])) {
    //pero NO es admin
    if ($_SESSION['id_grupo'] != 1) {
      //se redirige al login
      header("Location: login.php");
      die();
    }
  //si no tiene sesión iniciada
  }else{
    //redirect al login
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
  <p>ADMIN: Información solo para admin</p>
</body>
</html>
