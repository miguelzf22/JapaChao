// script.js
function validarPost(nome="postar"){
    const form = document.forms[nome]
    const post = form["msg"]
    const display = document.querySelector['display']
    if(post.value.length <= 10){
        display.textContent = 'Fale mais! Seu post está muito curto.'
        display.style.color = 'red'
        return false
    }
    return true
}

function abrirResposta(id){
    const resposta = document.getElementById(id)
    if(resposta){
        resposta.showModal()
    }
}

function fecharResposta(id){
    const resposta = document.getElementById(id)
    if(resposta){
        resposta.close()
    }
}