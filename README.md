# fastapi

To utilize the API, upload your file to any database and then provide the file's URL as input to the API. The API will then return the desired results. Each AI task will be deployed on a dedicated path.

## Call API Detect Deepfake

```javascript
// Gọi API Speech To Text từ JavaScript
async function callDetectDeepfakeAPI(videoUrl) {
  try {
    const response = await fetch(`https://everythingai.onrender.com/detect_deepfake?file_url=${videoUrl}`);
    const data = await response.json();
    return data.message;
  } catch (error) {
    console.error("Lỗi khi gọi API:", error);
    return null;
  }
}

// Ví dụ sử dụng:
const videoUrl = "https://res.cloudinary.com/dqneghcme/video/upload/v1723106326/5_zhofam.mp4";
const language = "Vietnamese";

callDetectDeepfakeAPI(videoUrl)
  .then(text => {
    if (text) {
      console.log("Result:", text);
    }
  });
```
Output:
```javascript
Result: Deepfake.
```
