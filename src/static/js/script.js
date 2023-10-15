function toggleClassContent(buttonId) {
    const homeContent = document.getElementById('home-content');
    const announcementContent = document.getElementById('announcement-content');
    //const syllabusContent = document.getElementById('syllabus-content');
    const modulesContent = document.getElementById('modules-content');
    const assignmentsContent = document.getElementById('assignments-content');

    const moduleSectionContent = document.getElementById('module-section-page-content');

    moduleSectionContent.classList.remove('active');
    homeContent.classList.remove('active');
    announcementContent.classList.remove('active');
    //syllabusContent.classList.remove('active');
    modulesContent.classList.remove('active');
    assignmentsContent.classList.remove('active');
    

    if (buttonId === 'btn-home') {
        homeContent.classList.toggle('active');
    } else if (buttonId === 'btn-announcement') {
        announcementContent.classList.toggle('active');
    } else if (buttonId === 'btn-modules') {
        modulesContent.classList.toggle('active');
    } else if (buttonId === 'btn-module-section') {
        moduleSectionContent.classList.toggle('active');
    } else if (buttonId === 'btn-syllabus') {
        syllabusContent.classList.toggle('active');
    } else if (buttonId === 'btn-assignments') {
        assignmentsContent.classList.toggle('active');
    }
}


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