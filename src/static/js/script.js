
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

function activateClassTab(tab_name) {
    var tabs = document.querySelectorAll('[class-tab]');
    
    tabs.forEach(function(tab) {
      var tabData = tab.getAttribute('class-tab');

      if (tabData === tab_name) {// check input menu name to toggle right one
        tab.classList.add('active-tab');
    } else {
        tab.classList.remove('active-tab');
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


//Calendar Button functionality
function toggleCalendarType(calendar_type) {

  var tabs = document.querySelectorAll('[calendar-tab]');
    
    tabs.forEach(function(tab) {
      var tabData = tab.getAttribute('calendar-tab');

      if (tabData === calendar_type) {// check input menu name to toggle right one
        tab.classList.add('calendar-tab-active');
    } else {
        tab.classList.remove('calendar-tab-active');
    }
    });
}

// Date search functionality

//Open date search form and hide button
function toggleDateSearchForm() {
  var dateSearchForm = document.getElementById('date-search-form');
  var btn = document.getElementById('btn-toggle-date-search');
  
  // add listener when button clicked, needs time out
  setTimeout(function() {
      document.addEventListener('click', clickOutsideHandler);
  }, "1");
  
  dateSearchForm.classList.toggle('active'); // show form
  btn.classList.toggle('active'); // hide button
}

//handle clicking outside the text box to hide form and reveal button
function clickOutsideHandler(event) {
  var dateSearchForm = document.getElementById('date-search-form');
  var btn = document.getElementById('btn-toggle-date-search');
  if (!dateSearchForm.contains(event.target) && event.target !== btn) {
      dateSearchForm.classList.remove('active'); // hide form
      btn.classList.remove('active'); // show button
      document.removeEventListener('click', clickOutsideHandler);
  }
}


function toggleCalendarEventScheduler(date) {
  var blur = document.getElementById('overlay');
  blur.classList.toggle('active');
  var popup = document.getElementById('calendar-event-popup');
  popup.classList.toggle('active');
  document.getElementById("event-date").value = date;
}

function getCellClicked(event) {
  const clickedGridItem = event.target.closest(".calendar-grid-item");

  if (clickedGridItem) {
    let date = clickedGridItem.getAttribute("day-id");
    console.debug(date)
    toggleCalendarEventScheduler(date);
  }
}