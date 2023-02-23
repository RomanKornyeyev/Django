<?php

  require("src/init.php");

  //errores para form
  $datos = [];
  $errores = [];

  //si el user no tiene sesión iniciada
  if (!isset($_SESSION['nombre'])) {
    //si el form se ha enviado
    if (isset($_POST['submit'])) {
      //comprobación nombre
      if (isset($_POST['login']) && $_POST['login'] != "" && $_POST['login'] != null) $datos['login'] = clean_input($_POST['login']);
      else $errores['login'] = "<span class='error'>*El campo nombre no puede estar vacío</span>";

      //comprobación passwd
      if (isset($_POST['password']) && $_POST['password'] != "" && $_POST['password'] != null) $datos['password'] = clean_input($_POST['password']);
      else $errores['password'] = "<span class='error'>*El campo password no puede estar vacío</span>";

      //si NO hay errores, buscamos al user en la BD
      if (count($errores) == 0) {
        $db->ejecuta(
          "SELECT * FROM usuarios WHERE nombre=?",
          $datos['login']
        );
        $consulta = $db->obtenElDato();

        //si hay un user que coincide
        if ($consulta != "") {
          //verificamos la pass, si es correcta metemos valores a $_SESSION
          if(password_verify($datos['password'], $consulta["secreto"])){
            //si es correcta, establecemos los datos en sesion
            $_SESSION['nombre'] = $consulta['nombre'];
            $_SESSION['id'] = $consulta['id'];
            $_SESSION['id_grupo'] = $consulta['id_grupo'];
            
            //si viniese de otra página, se le redirige
            header("Location: ".$paginaAnterior);
            die();
          }else{
            $errores['errorAutentificacion'] = "nombre/pass incorrectas";
          }
        }else{
          $errores['errorAutentificacion'] = "nombre/pass incorrectas";
        }
      }
    }
  //si está logueado, redirect al index
  }else{
    header("Location: index.php");
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
  <form action="login.php" method="post" class="login">
      <p>
        <label for="login">Nombre:</label>
        <input type="text" name="login" id="login" value="<?=$datos['login']?>">
      </p>
      <?php if(isset($errores['login'])) echo $errores['login']."<br>" ?>
      <!-- error personalizado de campo -->

      <p>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password" value="">
      </p>
      <?php if(isset($errores['password'])) echo $errores['password']."<br>" ?>
      <!-- error personalizado de campo-->

      <?php if(isset($errores['errorAutentificacion'])) echo "<div class='error'>".$errores['errorAutentificacion']."</div>" ?>
      <!-- error de autentificación -->

      <p class="login-submit">
        <label for="submit">&nbsp;</label>
        <button type="submit" name="submit" class="login-button">Login</button>
      </p>
  </form>
</body>
</html>