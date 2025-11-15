const correo = document.getElementById('correo')
const password = document.getElementById('password')
const login = document.getElementById('login')
const BASE_URL = 'http://127.0.0.1:5000'

login.addEventListener('click',async (e)=>{
    e.preventDefault()
    const response = await fetch(`${BASE_URL}/usuario/login`,{method:'POST', headers:{'Content-Type':'application/json'},body:JSON.stringify({
        correo:correo.value,
        password: password.value
    })})

    const data = await response.json()

    const token = data.content
    
    localStorage.setItem('token', token)

    window.location.href='/semana07/frontend/perfil.html'
})