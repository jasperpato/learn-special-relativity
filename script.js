function init() {
  scroll();
  dropMenu();
  titleParallax();
}

function scroll() {
  let progress = document.getElementById("progressbar");
  let totalHeight = document.body.scrollHeight - window.innerHeight;
  window.onscroll = function () {
    progress.style.height = (window.pageYOffset / totalHeight) * 100 + "%";
  };
}

function dropMenu() {
  $(document).ready(function () {
    $(".menu-toggle").click(function () {
      $("nav").toggleClass("active");
    });
  });
}

function titleParallax() {
  $("body").mousemove(function (e) {
    var valueX = (e.pageX * -1) / 75;
    var valueY = (e.pageY * -1) / 75;

    $("#title").css({
      transform: "translate(" + valueX + "px," + valueY + "px)",
    });
  });
  
 function makeQuiz(){
   myQuestions.forEach(
     (currentQuestion, QNum) => {
       const ans = [];
       
       for(letter in currentQuestion.ans){
         ans.push(
           <label>
            <input type="radio" name="question${questionNumber}" value="${letter}">
            ${letter} :
           ${currentQuestion.ans[letter]}
           </label> 
         );
       }       
       output.push(
         <div class="question"> ${currentQuestion.question} </div>
         <div class="answers"> ${answers.join('')} </div>
      );
    }
  );
  quizCont.innerHTML = output.join('');
}  

