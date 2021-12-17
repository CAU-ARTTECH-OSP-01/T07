;(function () {
  var canvas = document.getElementById("stopwatch"),
    ctx = canvas.getContext("2d"),
    digital = document.getElementById("time"),
    reset = document.getElementById("reset"),
    timerOn = false,
    second = (2 * Math.PI) / 65,
    start = 1.5 * Math.PI,
    t = 0,
    animation

  var draw = function () {
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    ctx.lineWidth = 30
    ctx.strokeStyle = "#F7958E"
    ctx.beginPath()
    ctx.arc(100, 100, 80, start, start + second * t)
    ctx.stroke()
    t = t > 65 ? 0 : t + 0.05
  }

  canvas.addEventListener("click", function () {
    if (!timerOn) {
      timerOn = true
      animation = setInterval(function () {
        draw()
        digital.innerHTML = Math.floor(66 - t)
      }, 65)
    } else {
      timerOn = false
      clearInterval(animation)
    }
  })

  reset.addEventListener("click", function () {
    setTimeout(function () {
      ctx.clearRect(0, 0, canvas.width, canvas.height)
      digital.innerHTML = Math.floor(66 - t)
      timerOn = false
      clearInterval(animation)
      t = 0
    }, 85500)
  })
})()
