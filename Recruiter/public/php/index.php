<?php
  $err = "В данный момент резюме можно отправить только через бота - @hr_ogima_bot";
  function check_string($inp) {
    $trimmed = "\r\n\t ";

    if (strpbrk($inp, $trimmed) !== false) {
      return true;
    } else {
      return false;
    }
  }
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Рекрутер</title>
  <link href="static/css/index.css" rel="stylesheet" />
</head>
<body>
  <div class="header">
    <div class="content">
      <div class="left">
        <div class="title">Ogima Company</div>
      </div>
      <div class="right">
        <a class="login" href="login.php">Войти в аккаунт</a>
      </div>
    </div>
  </div>
  <div class="main" id="main">
    <div class="mainTitle">Отправить резюме</div>
      <form class="searchBlock" method="GET" action="">
        <input class="input" name="send" placeholder="Ссылка на резюме" type="text">
        <input class="button" type="submit">
      </form>
      <div class="text">
      <?php 
        if (isset($_GET['send'])) {
          if (check_string($_GET['send'])) {
            echo "В строке есть запрещенные символы.";
          } else {
            echo "<div class='err'>Ваше резюме '" . $_GET['send'] . "' будет рассмотрено рекрутером</div>";
            echo "<div class='error'>$err</div>";
          }
        } else {
          echo '<div>Параметр "send" не найден.</div>';
        }
      ?>
    </div>
  </div>
</body>
</html>
