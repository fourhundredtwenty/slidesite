$(document).ready(function() {
    $("a.question-response").click(function(event){
        question_response_from_user = $(this).attr('href').substr(1);
        var request_url = `/respond/${question.q_id}/${question_response_from_user}`
        fetch(request_url)
        .then(function(response) {
            return response.text().then(function(text) {
                $("#user-response-badge").text(text);
            });
        });
    })
});
