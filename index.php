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
        <p>
            <label for="cost">Enter transaction cost:</label>
            <input type="text" name="cost" id="cost" placeholder="Enter cost">
        </p>

        <p>
            <label for="vendor">Enter vendor name:</label>
            <input type="text" name="vendor" id="vendor" placeholder="Enter vendor name">
        </p>

        <p>
            <button type="submit" name="submit_transaction" value="Submit Transaction">Submit</button>
        </p>
    </form>

    <?php

	if (isset($_POST['submit_transaction'])) {
                $cost = escapeshellarg($_POST['cost']);
                $vendor = escapeshellarg($_POST['vendor']);
                $output = shell_exec('sudo python3 addtransaction.py ' . $cost . ' ' . $vendor);
                file_put_contents('/var/www/html/command_output.log', $output, FILE_APPEND);
                //$new_total = file_get_contents('./transactions.csv', FALSE, null,)
                //$new_transaction = $vendor . ',' . $cost . ',' . 
                //file_put_contents('transactions.csv', )
        }
    ?>
</body>
</html>
