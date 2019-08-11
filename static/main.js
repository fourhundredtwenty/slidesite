$(document).ready(function() {
    if(typeof(question) !== 'undefined') {
        q_response = get_question_response(question.q_id)
        if (q_response == null) {
            set_question_response(question.q_id, "seen")
        }
    }

    $("a.question-response").click(function(event){
        question_response_from_user = $(this).attr('href').substr(1);
        set_question_response(question.q_id, question_response_from_user)
    })

    update_question_list_icons()
});

function icon_from_user_response(user_response) {
    switch (user_response) {
        case 'wtf':
            open_iconic_class = "oi-warning text-warning"
            break
        case 'star':
            open_iconic_class = "oi-star text-primary"
            break
        case 'seen':
            open_iconic_class = "oi-envelope-open"
            break
        default:
            open_iconic_class = "oi-envelope-closed text-info"
            break
    }

    icon_element = $("<span></span>")
    icon_element.addClass("question-icon oi")
    icon_element.addClass(open_iconic_class)

    return icon_element
}

function update_question_list_icons() {
    $("#question-list li").each(function(index, element){
        question_id = $(element).data('question-id');
        user_response = get_question_response(question_id);

        old_icon = $(element).children(".question-icon")
        new_icon = icon_from_user_response(user_response)

        old_icon.replaceWith(new_icon)
    })
}

function generate_key(question_id) {
    return question_id
}

function set_question_response(question_id, response) {
    key = generate_key(question_id)
    localStorage.setItem(key, response)
}

function get_question_response(question_id) {
    key = generate_key(question_id)
    return localStorage.getItem(key);
}
