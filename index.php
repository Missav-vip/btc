<?php
// Menangani proses upload file
if (isset($_POST['submit'])) {
    $targetDir = "uploads/";
    $targetFile = $targetDir . basename($_FILES["file"]["name"]);
    $uploadOk = 1;
    $fileType = strtolower(pathinfo($targetFile, PATHINFO_EXTENSION));

    // Cek apakah file sudah ada
    if (file_exists($targetFile)) {
        echo "File sudah ada.";
        $uploadOk = 0;
    }

    // Cek ukuran file
    if ($_FILES["file"]["size"] > 5000000) { // Maksimal 5MB
        echo "Maaf, file terlalu besar.";
        $uploadOk = 0;
    }

    // Cek tipe file (gambar atau video)
    if ($fileType != "jpg" && $fileType != "png" && $fileType != "jpeg" && $fileType != "gif" && $fileType != "mp4" && $fileType != "avi" && $fileType != "mov") {
        echo "Maaf, hanya file gambar atau video yang diperbolehkan.";
        $uploadOk = 0;
    }

    // Jika semuanya oke, upload file
    if ($uploadOk == 1) {
        if (move_uploaded_file($_FILES["file"]["tmp_name"], $targetFile)) {
            echo "File ". basename($_FILES["file"]["name"]). " telah diupload.";
        } else {
            echo "Terjadi kesalahan saat mengupload file.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Media</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
            margin: 0;
        }

        .container {
            text-align: center;
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }

        h1 {
            margin-bottom: 20px;
        }

        form input[type="file"] {
            margin-bottom: 20px;
        }

        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
        }

        .media {
            margin-top: 30px;
        }

        img, video {
            margin: 10px;
            max-width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Upload Video atau Gambar</h1>
        <form action="" method="POST" enctype="multipart/form-data">
            <input type="file" name="file" accept="image/*, video/*" required>
            <button type="submit" name="submit">Upload</button>
        </form>

        <div class="media">
            <!-- Media yang telah diupload akan ditampilkan di sini -->
            <?php
                // Menampilkan file yang ada di folder uploads
                $files = glob("uploads/*");
                foreach($files as $file) {
                    $file_extension = pathinfo($file, PATHINFO_EXTENSION);
                    if (in_array($file_extension, ['mp4', 'avi', 'mov'])) {
                        echo '<video width="320" height="240" autoplay muted loop>
                                <source src="'.$file.'" type="video/'.$file_extension.'">
                                Your browser does not support the video tag.
                              </video>';
                    } else {
                        echo '<img src="'.$file.'" alt="Uploaded Image">';
                    }
                }
            ?>
        </div>
    </div>
</body>
</html>
