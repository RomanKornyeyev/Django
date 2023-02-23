<!-- Cuando inicio sesión, cargo $_SESSION['id'], $_SESSION['nombre'], $_SESSION['id_grupo'] y $_SESSION['nb_grupo'] -->
<!-- Ergo, para saber si el usuario tiene la sesión iniciada, nos basta con ver si tiene un isset de cualquiera de estos sessions -->
<div class="menu">
  <a href="index.php">Inicio</a>

  <!-- si tiene la sesión iniciada Y ES ADMIN -->
  <?php if (isset($_SESSION['nb_grupo']) && $_SESSION['nb_grupo'] == "admin") {?>
    <a href="admin.php">Admin</a>
  <?php }?>

  <!-- si tiene la sesión iniciada -->
  <?php if (isset($_SESSION['nombre'])) {?>
    <a href="privado.php">Privado</a>
  <?php }?>

  <a href="login.php">Login</a>
  <a href="logout.php">Logout</a>
  -
  Bienvenido: <?=$userName?> - grupo: <?=$userGroup?>
</div>
