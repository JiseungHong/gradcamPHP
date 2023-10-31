<?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['images'])) {
        $imageFolder = './tf.keras-gradcamplusplus/user_images/'; // The folder where you want to save the uploaded images

        $images = $_FILES['images'];

        foreach ($images['tmp_name'] as $key => $tmp_name) {
            if ($images['error'][$key] === UPLOAD_ERR_OK) {
                $uploadedFilePath = $imageFolder . basename($images['name'][$key]);
                move_uploaded_file($tmp_name, $uploadedFilePath);
            }
        }

        $labels = $_POST['labels'];
        $imagePath = './tf.keras-gradcamplusplus/user_images';
        $command = "python3 ./tf.keras-gradcamplusplus/example.py $imagePath $labels";
        $output = shell_exec($command);

        // Display the result on the webpage
        echo "Classified label: " . $output;
    }
?>
