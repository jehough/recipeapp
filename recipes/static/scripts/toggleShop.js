
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

function toggleShop(id){
    const csrftoken = getCookie('csrftoken')
    const li = document.getElementById(`ingredient${id}`)
    const button = document.getElementById(`button${id}`)
    li ? li.remove():null
    button ? button.remove():null
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
    const url = `http://127.0.0.1:8000/recipes/toggle_ingredient`
    fetch(url, obj)
        .then(resp => resp.json())
        .then(json => console.log(json))
        .catch(err => handleErr(err))
}