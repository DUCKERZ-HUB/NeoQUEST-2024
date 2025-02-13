<?php
if (session_status() == PHP_SESSION_NONE) {
  session_start();
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
  $username = $_POST['username'];
  $password = $_POST['password'];

  if ($username === "hr" && $password === "S7t:rWRG$)=3Nfzmha@cZ") {
    $_SESSION['auth'] = $username;

    setcookie(session_name(), session_id(), [
      'expires' => 0,
      'path' => '/',
      'domain' => '',
      'secure' => isset($_SERVER['HTTPS']),
      'httponly' => true,
      'samesite' => 'Strict'
    ]);

    header('Location: profile.php');
    exit(); 
  }
}

if(isset($_SESSION['auth'])) {
  session_destroy();
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Вход</title>
  <link href="static/css/login.css" rel="stylesheet" />
</head>
<body>
  <div class="entryPage">
    <div class="entryTitle">Вход</div>
    <form class="entryForm" method="post">
      <div class="entryContent">
        <input type="text" name="username" class="entryInput" placeholder="username">
        <input type="password" name="password" class="entryInput" placeholder="password">
      </div>
      <input class="submitInput" value="войти" type="submit">
    </form>
  </div>
</body>
</html>
