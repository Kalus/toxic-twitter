$(document).ready(function() {
    hideLoading();
    hideUserToxSenseBanner();
    hideLoadingUser();
    hideErrors();
});

function hideErrors() {
    $('#erroruser').hide();
    $('#errortopic').hide();
}

// Topic analysis
$('#topicsearch').click(analyze);
$('#topic').on('keypress', function(e) {
    if (e.keyCode == 13) {
        analyze();
    }
});
function analyze() {
    var topic = $('#topic').val();
    if (!topic.trim() || topic.length < 2) {
        return;
    }

    hideErrors();
    showLoading();
    $.get('/analyze', {topic:topic})
     .done(receiveData);
}
function hideLoading() {
    $('#topicsearch').removeAttr("disabled");
    $('#usersearch').removeAttr("disabled");
    $('#loading').hide();
}
function showLoading() {
    $('#topicsearch').attr("disabled", "disabled");
    $('#usersearch').attr("disabled", "disabled");
    $('#loading').show();
}
function receiveData(response) {
    hideLoading();
    if (response['error']) {
        $('#errortopic').show();
        return;
    }
    visualizeTopicTweets(response);
}

// User analysis
$('#usersearch').click(analyzeUser);
$('#user').on('keypress', function(e) {
    if (e.keyCode == 13) {
        analyzeUser();
    }
});
function analyzeUser() {
    var user = $('#user').val();
    if (!user.trim() || user.length < 2) {
        return;
    }

    hideErrors();
    showLoadingUser();
    $.get('/analyzeuser', {user:user})
     .done(receiveUserData);
}
function hideLoadingUser() {
    $('#topicsearch').removeAttr("disabled");
    $('#usersearch').removeAttr("disabled");
    $('#loadinguser').hide();
}
function showLoadingUser() {
    $('#topicsearch').attr("disabled", "disabled");
    $('#usersearch').attr("disabled", "disabled");
    $('#loadinguser').show();
}
function showUserToxSenseBanner(){
    $('#bannerResult').show();
}

function hideUserToxSenseBanner(){
    $('#bannerResult').hide();
}

function receiveUserData(response) {
    hideLoadingUser();
    if (response['error']) {
        $('#erroruser').show();
        return;
    }
    showUserToxSenseBanner();
    visualizeUserTweets(response);
}
