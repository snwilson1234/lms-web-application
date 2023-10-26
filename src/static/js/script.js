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


//Assignment upload tab functionality
function openCity(evt, elem_name) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("upload-tab-content");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(elem_name).style.display = "block";
    evt.currentTarget.className += " active";
  }

function toggleUploadFileContent() {
    var content = document.getElementById('upload-box-content');
    content.classList.toggle('active');
}