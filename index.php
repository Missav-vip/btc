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
        <form id="uploadForm">
            <input type="file" id="fileInput" accept="image/*, video/*" required>
            <button type="submit">Upload</button>
        </form>

        <div class="media" id="mediaContainer"></div>
    </div>

    <script>
        document.getElementById('uploadForm').addEventListener('submit', function(e) {
            e.preventDefault();

            let file = document.getElementById('fileInput').files[0];
            if (!file) return;

            let reader = new FileReader();
            reader.onload = function(event) {
                let mediaContainer = document.getElementById('mediaContainer');
                let fileType = file.type.split('/')[0];

                if (fileType === 'image') {
                    let img = document.createElement('img');
                    img.src = event.target.result;
                    mediaContainer.innerHTML = ''; // Clear previous media
                    mediaContainer.appendChild(img);
                } else if (fileType === 'video') {
                    let video = document.createElement('video');
                    video.src = event.target.result;
                    video.autoplay = true;
                    video.loop = true;
                    video.muted = true;
                    mediaContainer.innerHTML = ''; // Clear previous media
                    mediaContainer.appendChild(video);
                }
            };
            reader.readAsDataURL(file);
        });
    </script>
</body>
</html>
