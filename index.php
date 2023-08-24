<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VMServer</title>
</head>

<!--
TO DO
-Add a button for submitting transactions that appends them to the CSV
-Add a way to increment the daily allowance. When the page is loaded? Cron? Idk
-->

<body>
    <p>The page loaded 1</p>

    <!-- Display last 10 transactions -->
    <p>Your previous 10 transactions:</p>
    <p>
    <?php
        passthru('python displaycsv.py')
    ?>
    </p>

    <!-- Display current balance -->
    <p>Your current balance: $
    <?php
        passthru('cat total.txt')
    ?>
    </p>

    <!-- Enter a transaction -->
    <form action="" method="post">
        <label for="arguement">Enter Argument:</label>
        <input type="text" name="argument" id="arguement">
        <input type="submit" name="enter_transaction" value="Enter Transaction">
    </form>

    <?php

	if (isset($_POST['enter_transaction'])) {
                $argument = escapeshellarg($_POST['argument']);
                passthru('python3 addtransaction.py ' . $argument);
        }
    ?>
</body>
</html>
