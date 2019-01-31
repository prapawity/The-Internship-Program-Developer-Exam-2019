# The-Internship-Program-Developer-Exam-2019
This is First Exam in The Internship Program Developer 2019
## Hangman 🏡
เกม Hangman ชิ้นนี้เป็นส่วนหนึ่งของข้อสอบในการคัดเลือกของโครงกาตร
    <b>The Internship Program Developer Exam 2019</b>
<br />
:heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign:

### Introduction ✏

 &nbsp;&nbsp;&nbsp;
    เกม Hangman เป็นเกมที่เกี่ยวกับการทายคำศัพท์จากคำใบ้ที่มี ให้ถูกต้องโดยหากมีการทายผิด จะเสียค่าพลังชีวิตไปครั้งละ 1 ชีวิต เมื่อใดที่พลังชีวิตเหลือ 0 เราก็จะแพ้หรือ Game Over<br>
    โดยภาษาที่ใช้ในการพัฒนาเป็นภาษา Python 

### Requirement
1. Python 3.7.0 หรือใหม่กว่า
2. Terminal หรือ Command line
3. หากไม่มี Python ให้ทำตามลิงค์นี้ https://realpython.com/installing-python


### Detail 📋
-- การให้คะแนน --<br/>
1. ทุกคำศัพท์คะแนนเต็มจะเท่ากันคือ 100 คะแนน
2. การให้คะแนนในแต่ละคำศัพท์จะไม่เหมือนกัน
3. การตอบผิดไม่ทำให้เสียคะแนน แต่จะเสียพลังชีวิต
4. พลังชีวิตมีทั้งหมด 5 ชีวิต
<br/><br>
## How To Play ❔ <br>
 1. Clone Project จาก https://github.com/prapawity/The-Internship-Program-Developer-Exam-2019<br>
![Clone file from github](https://github.com/prapawity/The-Internship-Program-Developer-Exam-2019/blob/master/ReadmePic/1.png?raw=true)<br>
![Download](https://github.com/prapawity/The-Internship-Program-Developer-Exam-2019/blob/master/ReadmePic/2.png?raw=true)<br>
![SaveFile](https://github.com/prapawity/The-Internship-Program-Developer-Exam-2019/blob/master/ReadmePic/3.png?raw=true)<br>
 2. Unzip file<br>
![PathFile](https://github.com/prapawity/The-Internship-Program-Developer-Exam-2019/blob/master/ReadmePic/4.png?raw=true)<br>
![Unzip](https://github.com/prapawity/The-Internship-Program-Developer-Exam-2019/blob/master/ReadmePic/5.png?raw=true)<br>
 3. เปิด Terminal ขึ้นมาและไปยัง Path ที่มีโฟลเดอร์ Hangman อยู่<br>
![OpenTerminal](https://github.com/prapawity/The-Internship-Program-Developer-Exam-2019/blob/master/ReadmePic/6.png?raw=true)<br>
 4. ใช้คำสั่ง <br> ◽ python3 main.py ใน OS X<br> ◽ python -3 main.py ใน Window<br>
![gotoPath](https://github.com/prapawity/The-Internship-Program-Developer-Exam-2019/blob/master/ReadmePic/7.png?raw=true)<br>
 5. หน้าเกมจะเปิดขึ้นมาเพื่อแสดง Category ที่มีโดยจะประกอบไปด้วย<br><b>
    1. ชื่อทีมฟุตบอลในพรีเมียนร์ลีคของประเทศอังกฤษ
    2. ตัวละครในจักรวาลของมาเวล
    3. ชื่อนักฟุตบอล
    4. ชื่อนักแสดงในฮอลลีวู๊ด
    5. ชื่อประเทศ

</b><br>
![category](https://github.com/prapawity/The-Internship-Program-Developer-Exam-2019/blob/master/ReadmePic/8.png?raw=true)<br>

6. เมื่อทำการเลือกหัวข้อที่ต้องการแล้ว จะมีค่าแสดงบอกว่าได้ทำการเลือกหัวข้อใดไปรวมไปถึงคำใบและคำศัพท์ที่เป็นคำถาม<br>
![selected](https://github.com/prapawity/The-Internship-Program-Developer-Exam-2019/blob/master/ReadmePic/9.png?raw=true)<br>

7. ให้ทำการใส่ตัวอักษรภาษาอังกฤษครั้งละ 1 ตัวอักษร หากใส่เกินหรือใส่เป็นอักขระหรือตัวอักษรที่ไม่ใช่ภาษาอังกฤษจะต้องทำการใส่ใหม่<br>

8. ในกรณีที่ใส่ถูก คะแนนจะเพิ่มและแสดงตัวอักษรที่ใส่ไป<br>
![correct](https://github.com/prapawity/The-Internship-Program-Developer-Exam-2019/blob/master/ReadmePic/10.png?raw=true)<br>

9. ในกรณีที่ใส่ผิด พลังชีวิตจะลดลงไป 1 ชีวิต และเมื่อใดตอบผิดถึง4ครั้ง คำใบ้จะแสดงขึ้นมา<br>
![incorrect](https://github.com/prapawity/The-Internship-Program-Developer-Exam-2019/blob/master/ReadmePic/11.png?raw=true)<br>

10. ถ้าหากตอบผิดจนชีวิตผมจะถือว่าแพ้ จะมีการแสดงคะแนนที่ได้<br>
![over](https://github.com/prapawity/The-Internship-Program-Developer-Exam-2019/blob/master/ReadmePic/12.png?raw=true)<br>

11. ถ้าหากตอบถูกจนครบ จะแสดงผลคะแนนที่ได้รับ และชีวิตที่เหลือ<br>
![win](https://github.com/prapawity/The-Internship-Program-Developer-Exam-2019/blob/master/ReadmePic/14.png?raw=true)<br>

12. ทุกครั้งที่จบเกมจะมีการถามว่าต้องการเริ่มเล่นใหม่หรือใหม่ หากกด Y จะทำการเริ่มเล่นอีกครั้ง หากกด N จะถือว่าเสร็จสิ้น<br>
![y](https://github.com/prapawity/The-Internship-Program-Developer-Exam-2019/blob/master/ReadmePic/13.png?raw=true)<br>
![n](https://github.com/prapawity/The-Internship-Program-Developer-Exam-2019/blob/master/ReadmePic/15.png?raw=true)<br>
![end](https://github.com/prapawity/The-Internship-Program-Developer-Exam-2019/blob/master/ReadmePic/116.png?raw=true)<br>