<?php
    header('Access-Control-Allow-Origin: *');
    header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept");
    header('Access-Control-Allow-Methods: GET, POST, PUT, DELETE');

    if(!file_put_contents('../students.txt', $_POST['data'])){
        echo "Data update error";
    }else{
        echo "Data updated successfully";
    }
?>