
function sendPost(cur_url, req_url, queryString){
    var xhr = new XMLHttpRequest();

    var url = req_url;

    console.log(url);

    xhr.open("POST", url, true);

    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 304) {
            window.location = cur_url;
        }
    };

    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
    console.log(queryString);
    xhr.send(queryString);
}

function remove_todo_visible(todo_area){
   var remove_todo = todo_area.getElementsByTagName('a')[0];

    remove_todo.style.visibility = 'visible';
}

function remove_todo_invisible(todo_area){
    var remove_todo = todo_area.getElementsByTagName('a')[0];

    remove_todo.style.visibility = 'hidden';
}

