document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
      var alerts = document.querySelectorAll(".alert");

      alerts.forEach(function(alert) {
        alert.classList.add("hidden");
        alert.addEventListener("transitionend", function() {
          alert.remove();
        });
      });
    }, 6000);
  });