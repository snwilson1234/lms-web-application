
// side menus functionality

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

// class tabs functionality (maybe not used?)
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

// Assignment upload tab functionality
function toggleUploadTab(evt, elem_name) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="upload-tab-content" and hide them
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


// Calendar Button functionality
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

// open date search form and hide button
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

// handle clicking outside the text box to hide form and reveal button
function clickOutsideHandler(event) {
  var dateSearchForm = document.getElementById('date-search-form');
  var btn = document.getElementById('btn-toggle-date-search');
  if (!dateSearchForm.contains(event.target) && event.target !== btn) {
      dateSearchForm.classList.remove('active'); // hide form
      btn.classList.remove('active'); // show button
      document.removeEventListener('click', clickOutsideHandler);
  }
}

// detect calendar cell click
function getCellClicked(event) {
  const actualClickedItem = event.target;
  const closestGridItem = event.target.closest(".calendar-grid-item");
  const closestEventItem = event.target.closest(".calendar-event-item");

  if (closestGridItem === actualClickedItem) {
    let date = closestGridItem.getAttribute("day-id");
    let day = closestGridItem.getAttribute("weekday");
    let shortDate = closestGridItem.getAttribute("short-date");
    let weekOfMonth = closestGridItem.getAttribute("week-of-month");
    toggleCalendarEventScheduler(date, day, shortDate, weekOfMonth);
  }
  else if (actualClickedItem === closestEventItem) {
    showEventPopup(closestEventItem);
  }
}

//toggle event scheduler for date clicked
function toggleCalendarEventScheduler(date, day, shortDate, weekOfMonth) {
  var blur = document.getElementById('overlay');
  blur.classList.toggle('active');
  var popup = document.getElementById('calendar-event-popup');
  popup.classList.toggle('active');

  var ordinalWeek = 0;
  if (weekOfMonth == 1) {
    ordinalWeek = "1st";
  }
  else if (weekOfMonth == 2) {
    ordinalWeek = "2nd";
  }
  else if (weekOfMonth == 3) {
    ordinalWeek = "3rd";
  }
  else {
    ordinalWeek = weekOfMonth + "th";
  }

  document.getElementById("id_date").value = date;
  document.getElementById("id_date").text = date;
  document.querySelector("[value='weekly-today']").text = "Weekly on " + day;
  document.querySelector("[value='monthly-today']").text = "Monthly on the " + ordinalWeek + " " + day;
  document.querySelector("[value='annually-today']").text = "Annually on " + shortDate;

}

//toggle input-dropdown highlight
function toggleInputDropdown(inputElement) {
  let inputDropdown = document.getElementById(inputElement.id + '-container');
  inputDropdown.classList.toggle('active');
  let timeDD = document.getElementById(inputElement.id + '-dd');
  timeDD.classList.toggle('active');
}

//event type tab functionality
function toggleEventTypeTab(tab_name) {
  
  var tabs = document.querySelectorAll('[event-type-tab]');
  
  
  tabs.forEach(function(tab) {
    var tabData = tab.getAttribute('event-type-tab');
    if (tabData === tab_name) {// check input menu name to toggle right one
      tab.classList.add('active');
      var tabBtn = document.getElementById('btn-' + tabData);
      tabBtn.classList.add('active');
  } else {
      tab.classList.remove('active');
      var tabBtn = document.getElementById('btn-' + tabData);
      tabBtn.classList.remove('active');
  }
  });
}

// fill from & to time drop downs with 12:00AM-11:55PM separated by 5min
function fillTimeDD() {
  let fromList = document.getElementById('id_from_time-dd');
  let toList   = document.getElementById('id_to_time-dd');

  for (var hours = 0; hours < 24; hours++) {
    for (var minutes = 0; minutes < 60; minutes += 5) {
      var fromListItem = document.createElement("li");
      var toListItem = document.createElement("li");
      if (hours == 0 || hours == 12){
        var timeString = "12"+ ":" + pad(minutes) + (hours < 12 ? " AM" : " PM");
      }
      else {
        var timeString = hours%12+ ":" + pad(minutes) + (hours < 12 ? " AM" : " PM");
      }
      fromListItem.textContent = timeString;
      var idString = timeString.replace(":","");
      fromListItem.setAttribute('id_from_time-list-item', idString.replace(" ","-") + "-from");
      toListItem.textContent = timeString;
      toListItem.setAttribute('id_to_time-list-item', idString.replace(" ","-") + "-to");
      //fromListItem.classList.add('')
      fromList.appendChild(fromListItem);
      toList.appendChild(toListItem);
    }
  }
}

// helper for above to pad with zeros when minutes/hours only one int long (ex: 5 -> 05)
function pad(number) {
  return (number < 10 ? "0" : "") + number;
}

function showEventPopup(eventCell) {
  
  const popup = document.getElementById(eventCell.getAttribute('event-title-id') + '-' + eventCell.getAttribute('event-date-id'));
  
  if (popup) {
      popup.classList.toggle('active');
      const closePopup = function(e) {
      if (!popup.contains(e.target) && e.target !== popup) {
        popup.classList.toggle('active');
        document.removeEventListener("mousedown", closePopup);
      }
    }
    document.addEventListener("mousedown", closePopup);
  }
  
  
}