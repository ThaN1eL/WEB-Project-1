document.addEventListener('DOMContentLoaded', function() {
    // Redirect to index.html
    document.querySelectorAll('#landing,#landing2').forEach(function(element) {
        element.addEventListener('click', function(e) {
            e.preventDefault(); 
            window.location.href = 'index.html';
        });
    });

    
    document.querySelector('#re-signup').addEventListener('click', function(e) {
        e.preventDefault();
        window.location.href = 'sign_up.html';
    });

});


// Redirect to login page when users click on the "user" icon or "Enroll NOW" button
document.querySelectorAll('#users, #users2, #re-login').forEach(function(element) {
    element.addEventListener('click', function(e) {
        e.preventDefault(); 
        window.location.href = 'login.html'; // Redirect to login page
    });
});
