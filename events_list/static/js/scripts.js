// The allows the Flash Message to remain visible for 6 seconds and then it will remove it

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


// This is form validation which prevents the user from inputting a blank space as a value

  document.querySelectorAll('.event-form').forEach(function(form) {
    form.addEventListener('submit', function(event) {
        let eventName = form.querySelector('#eventName').value.trim();
        let eventLocation = form.querySelector('#eventLocation').value.trim();
        let eventDescription = form.querySelector('#eventDescription').value.trim();

        if (eventName === '' || eventLocation === '' || eventDescription === '') {
            alert('Event name, location, and description cannot be empty or just spaces.');
            event.preventDefault(); // Prevent form submission
        }
    });
});


// This is form validation which prevents the user from inputting a date that is before the current date

const today = new Date().toISOString().split('T')[0];
    document.getElementById('eventDate').setAttribute('min', today);
