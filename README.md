# fastapi
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
