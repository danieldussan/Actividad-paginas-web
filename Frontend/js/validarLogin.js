
// if (userData.userId !== id){
//     localStorage.removeItem('userData');
//     window.location.href = 'login.html';
// }
window.addEventListener('pageshow', function (event) {
        const url = `${config.baseUrl}/auth/validate-login`
        request('GET',url)
        .then(response => {  
            let loggedIn = response['response'];
            console.log(loggedIn)
            if (loggedIn !== true) {
                localStorage.removeItem('userData');
                window.location.href = 'login.html';
            }
            console.log(loggedIn)
        })
        

   
});



