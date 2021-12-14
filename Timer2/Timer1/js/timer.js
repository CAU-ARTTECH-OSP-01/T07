var time = 0
var running = 0
var timerid = 0
function startPause() {
  if (running == 0) {
    //시작버튼
    running = 1
    increment()
    document.getElementById("stopTime").innerHTML = ""
    document.getElementById("start").innerHTML = "일시중지"
  } else {
    //일시정시버튼
    running = 0
    clearTimeout(timerid)

    document.getElementById("stopTime").innerHTML = "일시정지  "
    document.getElementById("start").innerHTML = "계속"
  }
}
//리셋
function reset() {
  running = 0
  time = 0
  clearTimeout(timerid)
  document.getElementById("stopTime").innerHTML = ""
  document.getElementById("start").innerHTML = "시작"
  document.getElementById("output").innerHTML = "<b>00:00</b>"
}
//타이머 시간측정
function increment() {
  if (running == 1) {
    timerid = setTimeout(function () {
      time++
      var mins = Math.floor((time % 3600) / 60)
      var secs = (time % 3600) % 60

      if (mins < 10) {
        mins = "0" + mins
      }
      if (secs < 10) {
        secs = "0" + secs
      }
      document.getElementById("output").innerHTML =
        "<b>" + mins + ":" + secs + "</b>"
      increment()
    }, 1000)
  }
}
