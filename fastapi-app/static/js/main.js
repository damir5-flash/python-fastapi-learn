const toLognInBtn = document.getElementById("signIn");
const toSignInBtn = document.getElementById("signUp");
const fistForm = document.getElementById("form1");
const secondForm = document.getElementById("form2");


const container = document.querySelector(".container");

toLognInBtn.addEventListener("click", () => {
	container.classList.remove("right-panel-active");
});

toSignInBtn.addEventListener("click", () => {
	container.classList.add("right-panel-active");

});

fistForm.addEventListener("submit", (e) => e.preventDefault());
secondForm.addEventListener("submit", (e) => e.preventDefault());

document.getElementById("form1").addEventListener("submit", async function(event) {
    event.preventDefault();
    console.log("Submitting form");

    const username = document.getElementById("user").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const age = document.getElementById("age").value;

    try {
        const response = await fetch('/api/v1/v1/users/singup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: username, // Используем правильное имя переменной
                email: email,
                password: password,
                age: parseInt(age, 10) // Указываем основание системы счисления
            })
        });

        if (!response.ok) {
			new Error('Network response was not ok');
        }

        const result = await response.json();
        console.log(result);
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
});
