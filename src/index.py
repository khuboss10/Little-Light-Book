from workers import WorkerEntrypoint, Response

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>A Little Light</title>
<style>
*{box-sizing:border-box}
body{
 margin:0;min-height:100vh;font-family:Georgia,serif;
 background:linear-gradient(135deg,#f8f0e7,#e8e2f4,#dce8f1);
 color:#504665;text-align:center;padding:25px;
 display:flex;justify-content:center;align-items:center;
}
.card{max-width:500px;width:100%}
h1{font-size:2.4rem;font-weight:normal}
p{line-height:1.8}
button{
 border:0;border-radius:30px;padding:14px 25px;
 background:#8e80aa;color:white;font-size:16px;
 cursor:pointer;margin:10px;transition:.3s
}
button:hover{transform:scale(1.05)}
input{
 padding:12px;border:1px solid #c5b8d8;
 border-radius:20px;text-align:center;font-size:18px;
 width:200px;background:#fffdf9;color:#504665
}
#book{display:none}
.page{
 background:#fffaf3;padding:30px 24px;border-radius:20px;
 box-shadow:0 15px 40px #51456725;
 min-height:340px;animation:appear .8s;
}
@keyframes appear{
 from{opacity:0;transform:translateY(20px)}
 to{opacity:1;transform:translateY(0)}
}
#bigKiss{
 display:none;position:fixed;inset:0;background:#f7eaf1;
 z-index:10;align-items:center;justify-content:center;
 flex-direction:column;padding:20px;
}
#bigKiss .emoji{font-size:110px;animation:pop .6s infinite alternate}
@keyframes pop{to{transform:scale(1.2)}}
.heart{position:fixed;animation:float 4s linear forwards;pointer-events:none}
@keyframes float{
 from{transform:translateY(100vh);opacity:1}
 to{transform:translateY(-10vh);opacity:0}
}
.small{font-size:13px;color:#8b829b}
</style>
</head>
<body>

<div class="card" id="entrance">
 <div class="page">
  <div style="font-size:35px">✦</div>
  <h1>A Little Light</h1>
  <p>Something small, made with care,<br>just for you, Olwethu.</p>
  <p class="small">Enter your little secret to open this book.</p>
  <input id="pin" type="password" maxlength="10" placeholder="Enter secret PIN">
  <br>
  <button onclick="openBook()">Open my book ✨</button>
  <p id="error"></p>
 </div>
</div>

<div class="card" id="book">
 <div class="page">
  <div id="content"></div>
  <button id="next" onclick="nextPage()">Turn the page →</button>
 </div>
</div>

<div id="bigKiss">
 <div class="emoji">💋</div>
 <h1>A kiss for Olwethu!</h1>
 <p>A little virtual kiss, just to remind you<br>
that someone is wishing you well today.</p>
<button onclick="closeKiss()">Back to the book ✨</button>
</div>

<script>
let page=0;

const pages=[
`<h1>For Olwethu ✨</h1>
<p>Some things are better written down.
So I made you a little book, something
you can open whenever you need a
little warmth in your day.</p>
<p>Nothing complicated. Just a little light.</p>`,

`<h1>Whenever things feel heavy 🌷</h1>
<p>Olwethu, I hope you remember that you
don't have to have everything figured out.
Take things one moment at a time.
Rest when you need to, and give yourself
the same kindness you give others.</p>`,

`<h1>A reminder for you ✨</h1>
<p>Even on ordinary days, you matter.
Your presence, your laughter, your little
ways of being yourself — they matter.
Never forget that you deserve kindness,
patience and beautiful moments too.</p>`,

`<h1>A little surprise 💌</h1>
<p>Well... I couldn't make a book without
including something silly.</p>
<p>Whenever you're ready, press the button.</p>
<button onclick="kiss()">GET A KISS FROM AYA 💋</button>`,

`<h1>Before you go... 🌙</h1>
<p>Olwethu, I hope this little book reminds
you that there are people wishing you
good days, peaceful moments and reasons
to smile.</p>
<p>Whatever the days ahead bring, I hope
you meet them with hope and gentleness.</p>
<p>Take care of yourself, okay?</p>
<h2>With care,<br>Aya ✨</h2>`
];

function openBook(){
 if(document.getElementById("pin").value==="2011-15-02"){
  document.getElementById("entrance").style.display="none";
  document.getElementById("book").style.display="block";
  showPage();
 }else{
  document.getElementById("error").innerText="That isn't the right code 💫";
 }
}

function showPage(){
 document.getElementById("content").innerHTML=pages[page];
 document.getElementById("next").style.display=
 page===pages.length-1?"none":"inline-block";
}

function nextPage(){
 if(page<pages.length-1){
  page++;
  showPage();
 }
}

function kiss(){
 document.getElementById("bigKiss").style.display="flex";
 for(let i=0;i<25;i++){
  let h=document.createElement("div");
  h.className="heart";
  h.innerHTML=["💗","💕","💖","💓"][Math.floor(Math.random()*4)];
  h.style.left=Math.random()*100+"vw";
  h.style.fontSize=(20+Math.random()*25)+"px";
  document.body.appendChild(h);
  setTimeout(()=>h.remove(),4000);
 }
}

function closeKiss(){
 document.getElementById("bigKiss").style.display="none";
}
</script>
</body>
</html>"""
        return Response(html, headers={"Content-Type": "text/html; charset=utf-8"})
