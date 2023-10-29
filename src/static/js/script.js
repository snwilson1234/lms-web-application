
function togglePopup(menu_name) {
    var menus = document.querySelectorAll('[data-menu]');

    menus.forEach(function(menu) {// for all menus marked w/ "data-menu" attribute
        var menuData = menu.getAttribute('data-menu');
        if (menuData === menu_name) {// check input menu name to toggle right one
            menu.classList.toggle('active');
        } else {
            menu.classList.remove('active');
        }
    });
}


//Assignment upload tab functionality
function toggleUploadTab(evt, elem_name) {
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