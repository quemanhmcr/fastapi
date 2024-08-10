# EverythingAI (AI models trained without data.)

These APIs are applications built using Gemini Flash 1.5 with "Imposing-context" integrated. To utilize the API, upload your file to any database and then provide the file's URL as input to the API. The API will then return the desired results. Each AI task will be deployed on a dedicated path.

## Call API Detect Deepfake

```javascript
// Call the Speech To Text API from JavaScript
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

// Examples of Use:
const videoUrl = "https://res.cloudinary.com/dqneghcme/video/upload/v1723106326/5_zhofam.mp4";
const language = "Vietnamese";

callDetectDeepfakeAPI(videoUrl)
  .then(text => {
    if (text) {
      console.log("Result:", text);
    }
  });
```
Output (Deepfake. or Người thật.):
```javascript
Result: Deepfake.
```
## Call API Speech To Text
```javascript
// Call the Speech To Text API from JavaScript
async function callSpeechToTextAPI(audioUrl, language) {
  try {
    const response = await fetch(`https://everythingai.onrender.com/speech_to_text?file_url=${audioUrl}&language=${language}`);
    const data = await response.json();
    return data.message;
  } catch (error) {
    console.error("Error API:", error);
    return null;
  }
}

// Ví dụ sử dụng:
const audioUrl = "https://res.cloudinary.com/dqneghcme/video/upload/v1723244703/Y2meta.app_-_4_tips_v%C6%B0%E1%BB%A3t_qua_n%E1%BB%97i_s%E1%BB%A3_N%C3%B3i_Ti%E1%BA%BFng_Anh_t%E1%BA%A1i_m%C3%B4i_tr%C6%B0%E1%BB%9Dng_%C4%91a_qu%E1%BB%91c_gia_320_kbps_jfjjat.mp3";
const language = "Vietnamese";

callSpeechToTextAPI(audioUrl, language)
  .then(text => {
    if (text) {
      console.log("Result:", text);
  }});
```
Output:
```javascript
Result: Hello, xin chào các bạn. Dũng lại lập trình đây. Trong video này mình sẽ chia sẻ với các bạn những điều đã thực sự khiến mình cải thiện tiếng Anh trước khi và trong quá trình du học tại Úc. Trước khi du học và trong cái quá trình mới sang du học thì tiếng Anh của mình, cái khoản giao tiếp cực kỳ là kém, đặc biệt là giao tiếp xã hội. Nhưng mà riêng khi cái việc đến trường và ngay giảng ở trên trường và việc học thì mình không cảm thấy có khó khăn gì. Cái việc không thể giao tiếp xã hội một cách tự nhiên khiến mình đã rất khó khăn khi mà tìm việc và làm việc với cả môi trường nước ngoài. Thì sau đây là những việc mà mình nghĩ là mình đã làm sai trước khi du học sang Úc. Điều đầu tiên là trước khi du học mình phải chuẩn bị cho kỳ thi IELTS để vừa đủ điều kiện sang du học, thì mình tập trung quá nhiều vào việc học các cái cụm từ đơn lẻ, các cái từ ngữ phức tạp để được điểm cao trong kỳ thi IELTS, và mình không biết được cách sử dụng chúng như nào và cái hoàn cảnh sử dụng nó như nào. Cái việc mình cố gắng nhồi nhét những cái từ ngữ phức tạp trong giao tiếp, nó khiến mình không linh hoạt, và đối với người bản xứ thì người ta nghe người ta cũng rất là khó hiểu, và đặc biệt là khi mình phát âm còn không chuẩn nữa, thì người ta cũng không hiểu gì luôn. Điểm thứ hai mình đã làm sai, đó là không bao giờ tự đánh giá, tự nghe lại kỹ năng nói của mình. Cũng như rất nhiều bạn đang trong quá trình luyện thi IELTS hoặc là những chứng chỉ khác cho mục đích du học hoặc là đi làm, mình chỉ thích ngồi một chỗ để tự luyện đề, chủ yếu là luyện đề reading, học từ mới, chứ về kỹ năng nói, ba bài nói trong IELTS thì mình không bao giờ dành thời gian để tự luyện và tự nghe lại thì càng không. Cái lý do một phần cũng là vì ngại, tại vì tự nói đã ngại rồi mà nghe lại cái giọng mình nói còn ngại hơn, và đặc điểm là ngày xưa không có những cái công cụ như bây giờ để mình tự đánh giá, tự cải thiện kỹ năng nói của mình, và hậu quả là kỹ năng nói của mình không thể cải thiện. Mặc dù mình nghĩ đây là kỹ năng quan trọng nhất khi học một ngôn ngữ mới, để là mình có thể giao tiếp được với người khác. Để giải quyết vấn đề này, lát nữa trong video Dũng sẽ giới thiệu cho các bạn một công cụ giúp các bạn có thể tự cải thiện, tự luyện kỹ năng nói của mình trong bài thi IELTS. Sau nhiều năm đi du học và làm việc ở nước ngoài, Dũng cảm thấy trình độ tiếng Anh của mình đã được cải thiện rõ rệt. Tuy nhiên khi mới vào môi trường làm việc ở nước ngoài, cần giao tiếp bằng tiếng Anh thì mình rất là khó để thoát ý ra, ví dụ như khi giao tiếp với cả các thầy cô hoặc là giao tiếp với khách hàng. Cái này sẽ cần một thời gian để luyện tập, với những bạn đang ở Việt Nam, chắc chắn là mình sẽ gặp khó khăn hơn so với việc là mình có cơ hội được đi ra nước ngoài để làm việc và du học trong một thời gian dài. Những khó khăn chính đấy là ở Việt Nam thì không có môi trường để có thể giao tiếp bằng tiếng Anh giữa người với người. Thứ hai là áp lực điểm số thi những chứng chỉ rất cao, và thứ ba là trường lớp cấp hai, cấp ba, kể cả lên đại học, chỉ chủ yếu tập trung vào những bài kiểm tra ngữ pháp. Sau đây là bốn điều cần làm mà Dũng đã chiêm nghiệm lại, có thể áp dụng với tất cả những bạn, kể cả đang ở Việt Nam có thể giúp mình cải thiện và nâng cao kỹ năng tiếng Anh. Đầu tiên, học từ vựng đời sống hàng ngày theo chủ đề. Nếu bạn muốn nâng cao khả năng tiếng Anh của mình, một cách tốt nhất theo Dũng nghĩ, đó là bắt đầu từ việc học từ vựng đời sống hàng ngày theo các chủ đề cụ thể. Hãy cố gắng tập trung vào một chủ đề mỗi tuần, ví dụ như đi mua sắm, hỏi đường, làm thêm. Việc học này giúp bạn có chuẩn bị khi được đặt vào tình huống cụ thể trong cuộc sống. Chính việc học tập những tên gọi đồ dùng vật dụng xung quanh bằng tiếng Anh, cách mô tả những hoạt động bình thường hàng ngày bằng tiếng Anh là thứ giúp bạn giao tiếp trơn tru hơn. Điều thứ hai, đó là xóa bỏ mặc cảm khi nói tiếng Anh. Các bạn cố gắng đừng để mặc cảm về khả năng tiếng Anh của mình làm các bạn ngần ngại khi nói chuyện bằng tiếng Anh. Hãy nhớ rằng việc nói tiếng Anh là một quá trình cải thiện, và mọi người đều cần phải trải qua giai đoạn cố gắng học tập và phát triển. Bạn hãy coi đó là một cơ hội để cải thiện ngôn ngữ, hãy tự tin với những cố gắng, những câu chuyện cá nhân và kiến thức trải nghiệm của mình và chia sẻ nó một cách tự nhiên. Điều số ba, đấy là chuyển môi trường xung quanh sang tiếng Anh. Khi đạt đến một trình độ nhất định rồi, bạn hãy bắt đầu tìm kiếm những thông tin bằng tiếng Anh, ví dụ như là các bạn muốn tìm tài liệu về một bản ở trong lập trình, thì thay vì các bạn dùng tiếng Việt các bạn hãy search trên Google ngay bằng tiếng Anh luôn, và vào những cái diễn đàn bằng tiếng Anh. Khi mà xem những cái video hướng dẫn ở trên YouTube thì thay vì bạn tìm kiếm về một chủ đề bằng tiếng Việt, mình có thể tìm bằng tiếng Anh và nghe bằng tiếng Anh luôn. Thậm chí là cái điện thoại di động của mình, mình cũng chuyển sang tiếng Anh thay vì tiếng Việt để mình làm quen với cả những cái từ ở trong phần cài đặt. Từ những cái việc nhỏ nhỏ đấy sẽ làm mình làm quen với tiếng Anh hơn. Và với những bạn nào đang muốn nâng cao trình độ tiếng Anh của mình thông qua những kỳ thi như IELTS, TOEIC, tiếng Anh nói chung, thì mình xin giới thiệu nền tảng Prep. Khi bắt đầu vào, bạn sẽ làm một bài kiểm tra năng lực và Prep sẽ biết được trình độ hiện tại của bạn, và đưa cho bạn một lộ trình học phù hợp. Các bạn sẽ học qua những bài giảng xúc tích của các thầy cô. Sau mỗi bài giảng sẽ có bộ bài tập để các bạn có thể tự đánh giá, kiểm tra, nắm chắc kiến thức. Điểm sáng nhất của Prep là chấm chữa, chấm từng giây về speaking, và từng chữ về writing. Bộ đôi phòng ảo speaking và writing có AI đồng hành mỗi ngày. Điểm mình ấn tượng ở phòng speaking ảo của Prep là cả giác tương tác một một khi đang luyện nói, vì có giám khảo là người nước ngoài đọc câu hỏi và lắng nghe mình, chấm chữa khá chuẩn, tạo cảm giác y như trong phòng thi. Now we can move on to the second part of the exam. As you grow up I think we get more skeptical about people, we tend to keep our circle friends very small. Ờ, bất kỳ nơi đâu, bạn đều có thể xem đánh giá bài nói của mình trên ứng dụng điện thoại. Về phần xét từ vựng, nền tảng đã ghi nhận những từ vựng hay và những collocation hay mà mình nên phát huy và sử dụng. Tiếp theo là phần nâng cấp từ vựng, nền tảng đã thay thế những cái từ mà mình sử dụng bằng những cái từ mà có thể đạt band điểm cao hơn. Ví dụ câu này nó nói là As I mature, I tend to become cautious and selective about the people I allow into my inner circle. Mình thấy có rất là nhiều từ hay, ví dụ như là tend to, cautious, selective about, hay là inner circle. Tiếp đến là phần sửa lỗi, nền tảng này đã chấm và nhận xét về phần từ vựng, phát âm và ngữ pháp, và cuối cùng là phần gợi ý bài mẫu. Nếu bạn không biết trả lời một câu như nào thì Prep đã đưa ra một bài mẫu để các bạn có thể tham khảo. Sau khi trải nghiệm phòng speaking ảo thì mình đánh giá đây là một công cụ tốt để các bạn luyện thi IELTS. Thứ nhất là cái áp lực nó rất giống kỳ thi thật, hồi cấp ba mình phải thi đến bốn lần, thế nên mình rất là rõ cái máy cứ hiện đến chỗ nào là mình phải nói ngay lập tức sau lúc đấy. Thứ hai là phần AI đã ghi nhận những cái cụm từ tốt mà bạn phát huy, và đặc điểm hay là nó đã nâng cấp lên những cái từ khác để phù hợp với những band điểm cao hơn. Nhân đây, mình và Prep xin được dành tặng các bạn mã khuyến mãi Dũng lại để được giảm 30% khi đăng ký từ hai khóa IELTS tại Prep. Ngoài ra các bạn sẽ được tặng thêm 60 ngày sử dụng phòng luyện đề cho bốn kỹ năng toàn diện. Trong đó có phòng speaking ảo và phòng writing ảo. Ngoài ra nếu bạn quan tâm đến việc học và luyện thi TOEIC, thì mình và Prep có code DL25, giảm 25% và tặng kèm 45 ngày sử dụng phòng luyện đề cùng AI. Khóa học TOEIC sẽ giúp bạn tiếp cận mọi thứ trên một nền tảng duy nhất, thi gì học nấy. Ngoài ra trong đấy có ứng dụng phương pháp dạy và học CBI từ đại học Oxford, Cambridge, giúp các bạn tiết kiệm thời gian ôn luyện và đạt target sau một lộ trình. Các bạn cứ nhập code mình để trên màn hình để nhận ưu đãi khi đăng ký cả khóa IELTS và TOEIC nha. Và điều thứ tư, điều cuối cùng để nâng cao trình độ tiếng Anh của mình mà Dũng khuyên trong hôm nay, đấy là nâng cao vốn hiểu biết chung và chuyên môn. Đấy là qua những việc đọc sách, đọc báo, tham khảo, tham gia những cuộc thảo luận về nhiều chủ đề khác nhau. Nếu mà tốt hơn nữa là bằng tiếng Anh. Điều này không chỉ giúp các bạn cải thiện từ vựng và ngữ pháp, mà còn nâng cao vốn hiểu biết chung của mình về thế giới. Tiếng Anh mình nghĩ là cũng như nhiều các ngôn ngữ khác, chỉ là một công cụ để mình mô tả, suy nghĩ. Vì vậy, nếu tư duy không mạch lạc, và hiểu biết của mình về vấn đề mình đang nói đến không nhiều và không sâu, thì dù tiếng Anh của mình có lưu loát đến mấy, thì cuộc nói chuyện cũng không thể có giá trị được. Và hơn hết là khi mình không hiểu về vấn đề đấy, mình sẽ không có cái từ vựng chuyên ngành để mình nói về cái vấn đề đấy, và ngược lại nếu như bạn là một người có chuyên môn giỏi mà tiếng Anh chỉ ở mức cơ bản, thì mình nghĩ bạn hoàn toàn có thể tự tin truyền đạt ý tưởng của mình trước đám đông, và mọi người vẫn chú ý lắng nghe, và trân trọng những gì mình nói. Và cuối cùng, để kết thúc video này, Dũng chúc các bạn thành công trên con đường học tiếng Anh cũng như chuyên môn của mình. Cảm ơn các bạn đã lắng nghe nha.
```
