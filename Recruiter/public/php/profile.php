<?php 
  if (session_status() == PHP_SESSION_NONE) {
    session_start();
  }

  if (!isset($_SESSION['auth']) || $_SESSION['auth'] !== 'hr') {
    echo 'Доступ запрещен! Только для HR.';
    exit();
  }

  $err = '';

  if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    if(isset($_GET['apply'])) {
      $name = $_GET['apply'];

      $err =  "PolyCTF{XS5_v14_InFo_PhP}";
    }
  }
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Профиль</title>
  <link href="static/css/profile.css" rel="stylesheet" />
</head>
<body>
  <div class="header">
    <div class="content">
      <div class="title">Рекрутер Ogima Company</div>
    </div>
  </div>

  <div class="list">
    <div class="container">
      <div class="item">
        <div class="name">Иванов Иван</div>
        <div class="ignore">Не перезвонить</div>
        <div href="#" onclick='showModal("Иванов Иван")' class="apply">Взять на работу</div>
      </div>
      <div class="item">
        <div class="name">John Doe</div>
        <div class="ignore">Не перезвонить</div>
        <div href="#" onclick='showModal("John Doe")' class="apply">Взять на работу</div>
      </div>
    </div>
  </div>

  <div class="secret" id="secret" style="display: none;">
    <div class="alert">Подтвердите действие</div>
    <form method="POST" action="">
      <input class="button" type="submit" value="Подтвердить">
    </form>
  </div>
  <div class="error"><?php echo $err; ?></div>


  <script>
    let modal = document.getElementById('secret');

    const showModal = (name) => {
      if(modal.style.display === 'none') {
        modal.style.display = 'flex';

        const newUrl = new URL(window.location.href);
        newUrl.searchParams.set('apply', name);
        history.pushState({}, '', newUrl);
      } else {
        closeModal();
      }
    }

    const closeModal = () => {
      modal.style.display = 'none';

      const newUrl = new URL(window.location.href);
      newUrl.searchParams.delete('apply');
      history.pushState({}, '', newUrl);
    }

    window.onclick = (event) => {
      if (event.target === modal) {
        closeModal();
      }
    }
  </script>
</body>
</html>
