const form = document.getElementById('add-ingredient')
const ingredients_list = document.getElementById('ingredients_list')

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

form.addEventListener('submit', (e)=>{
    e.preventDefault()
    
    const csrftoken = getCookie('csrftoken')
    let obj = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Action": "application/json",
            "X-CSRFToken": csrftoken
        },
        body:JSON.stringify({
            recipe_id: e.target.recipe_id.value,
            name: e.target.name.value,
            amount: e.target.amount.value
        })
    }
    url = `http://teachlife.pythonanywhere.com/recipes/${e.target.recipe_id.value}/add_ingredient`
    fetch(url, obj)
        .then(resp=> resp.json())
        .then(json=> handleSuccess(json))
        .catch(err => handleErr(err))
})

function handleSuccess(json){
    const li = document.createElement('li')
    const button = document.createElement('button')
    const span = document.createElement('span')
    span.innerHTML = '&#x1F5D1'
    li.innerHTML =  `${json.amount} ${json.name}`
    li.id = `ingredient${json.id}`
    button.addEventListener('click', ()=>handleClick(json.id))
    button.appendChild(span)
    li.appendChild(button)
    ingredients_list.appendChild(li)
    form.reset()
}

function handleErr(err){
    console.log(err)
}

function handleClick(id){
    const csrftoken = getCookie('csrftoken')
    const li = document.getElementById(`ingredient${id}`)
    li.remove()
    let obj = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Action": "application/json",
            "X-CSRFToken": csrftoken
        },
        body:JSON.stringify({
            ing_id: id,
        })
    }
    const url = `http://teachlife.pythonanywhere.com/recipes/delete_ingredient`
    fetch(url, obj)
        .then(resp => resp.json())
        .then(json => console.log(json))
        .catch(err => handleErr(err))
}