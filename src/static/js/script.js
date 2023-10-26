//Popup toggles

function toggleUserMenu(){
    var popup = document.getElementById('user');
    popup.classList.toggle('active');
}

function toggleCoursesMenu(){
    var popup = document.getElementById('courses');
    popup.classList.toggle('active');
}

function toggleGroupsMenu(){
    var popup = document.getElementById('groups');
    popup.classList.toggle('active');
}

function toggleHistoryMenu(){
    var popup = document.getElementById('history');
    popup.classList.toggle('active');
}

function toggleHelpMenu(){
    var popup = document.getElementById('help');
    popup.classList.toggle('active');
}

function togglePopup(menu_name) {
    var userMenu = document.getElementById('user');
    var coursesMenu = document.getElementById('courses');
    var groupsMenu = document.getElementById('groups');
    var historyMenu = document.getElementById('history');
    var helpMenu = document.getElementById('help');

    userMenu.classList.remove('active');
    coursesMenu.classList.remove('active');
    groupsMenu.classList.remove('active');
    historyMenu.classList.remove('active');
    helpMenu.classList.remove('active');

    if (menu_name == 'user'){
        userMenu.classList.toggle('active');
    } else if (menu_name == 'courses'){
        coursesMenu.classList.add('active');
    } else if (menu_name == 'groups'){
        groupsMenu.classList.add('active');
    } else if (menu_name == 'history'){
        historyMenu.classList.add('active');
    } else if (menu_name == 'help'){
        helpMenu.classList.add('active');
    }
}