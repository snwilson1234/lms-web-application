import dayjs from "dayjs";
import "./styles.css";
const weekday = require("dayjs/plugin/weekday");
const weekOfYear = require("dayjs/plugin/weekOfYear");

dayjs.extend(weekday);
dayjs.extend(weekOfYear);

const WEEKDAYS = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
const TODAY = dayjs().format("ddd, MMM DD, YYYY");

const INITIAL_YEAR = dayjs().format("YYYY");
const INITIAL_MONTH = dayjs().format("M");

let selectedMonth = dayjs(new Date(INITIAL_YEAR, INITIAL_MONTH - 1, 1));
let currentMonthDays;
let previousMonthDays;
let nextMonthDays;


const daysOfWeekElement = document.getElementById("calendarheader");

WEEKDAYS.forEach((weekday) => {
  const weekDayElement = document.createElement("div");
  weekDayElement.classList.add("calendar-grid-header-item")
  daysOfWeekElement.appendChild(weekDayElement);
  weekDayElement.innerText = weekday;
});

// initialize calendar
createCalendar();

// initialize selectors
initMonthSelectors();


/* Calendar creation/helper functions */

function createCalendar(year = INITIAL_YEAR, month = INITIAL_MONTH) {
  const calendarDaysElement = document.getElementById("mycalendar");

  document.getElementById("selected-month").innerText = dayjs(
    new Date(year, month - 1)
  ).format("MMMM YYYY");

  removeAllDayElements(calendarDaysElement);

  currentMonthDays = createDaysForCurrentMonth(
    year,
    month,
    dayjs(`${year}-${month}-01`).daysInMonth()
  );

  previousMonthDays = createDaysForPreviousMonth(year, month);

  nextMonthDays = createDaysForNextMonth(year, month);

  const days = [...previousMonthDays, ...currentMonthDays, ...nextMonthDays];

  days.forEach((day) => {
    appendDay(day, calendarDaysElement);
  });
}

function appendDay(day, calendarDaysElement) {
  const dayElement = document.createElement("div");
  const dayElementClassList = dayElement.classList;
  dayElementClassList.add("calendar-grid-item");
  const dayOfMonthElement = document.createElement("h4");

  dayOfMonthElement.classList.add("bold-font");
  dayElement.setAttribute("day-id",day.date);
  dayElement.setAttribute("weekday",day.weekday);
  dayElement.setAttribute("short-date",day.shortDate);
  dayElement.setAttribute("week-of-month",day.weekOfMonth);
  dayOfMonthElement.innerText = day.dayOfMonth;
  dayElement.appendChild(dayOfMonthElement);
  calendarDaysElement.appendChild(dayElement);

  if (!day.isCurrentMonth) {
    dayElementClassList.add("calendar-day--not-current");
  }

  if (day.date === TODAY) {
    dayElementClassList.add("calendar-day--today");
  }
}

function removeAllDayElements(calendarDaysElement) {
  let first = calendarDaysElement.firstElementChild;

  while (first) {
    first.remove();
    first = calendarDaysElement.firstElementChild;
  }
}

function getNumberOfDaysInMonth(year, month) {
  return dayjs(`${year}-${month}-01`).daysInMonth();
}

function createDaysForCurrentMonth(year, month) {
  return [...Array(getNumberOfDaysInMonth(year, month))].map((day, index) => {
    return {
      date: dayjs(`${year}-${month}-${index + 1}`).format("ddd, MMM DD, YYYY"),
      dayOfMonth: index + 1,
      isCurrentMonth: true,
      weekday: dayjs(`${year}-${month}-${index + 1}`).format("dddd"),
      shortDate: dayjs(`${year}-${month}-${index + 1}`).format("MMMM DD"),
      weekOfMonth: getWeekOfMonth(dayjs(`${year}-${month}-${index + 1}`)),
    };
  });
}

function getWeekOfMonth(date) {
  // Get the first day of the month
  const firstDayOfMonth = dayjs(date).startOf('month');

  // Get the ISO week numbers for the first day of the month and the target date
  const weekNumberFirstDay = firstDayOfMonth.week();
  const weekNumberTargetDate = dayjs(date).week();

  // Calculate the week number within the month
  const weekOfMonth = weekNumberTargetDate - weekNumberFirstDay + 1;

  return weekOfMonth;
}

function createDaysForPreviousMonth(year, month) {
  const firstDayOfTheMonthWeekday = getWeekday(currentMonthDays[0].date);

  const previousMonth = dayjs(`${year}-${month}-01`).subtract(1, "month");

  const visibleNumberOfDaysFromPreviousMonth = firstDayOfTheMonthWeekday;

  const previousMonthLastMondayDayOfMonth = dayjs(currentMonthDays[0].date)
    .subtract(visibleNumberOfDaysFromPreviousMonth, "day")
    .date();

  return [...Array(visibleNumberOfDaysFromPreviousMonth)].map((day, index) => {
    return {
      date: dayjs(
        `${previousMonth.year()}-${previousMonth.month() + 1}-${
          previousMonthLastMondayDayOfMonth + index
        }`
      ).format("ddd, MMM DD, YYYY"),
      dayOfMonth: previousMonthLastMondayDayOfMonth + index,
      isCurrentMonth: false,
      weekday: dayjs(
        `${previousMonth.year()}-${previousMonth.month() + 1}-${
          previousMonthLastMondayDayOfMonth + index
        }`
      ).format("dddd"),
      shortDate: dayjs(
        `${previousMonth.year()}-${previousMonth.month() + 1}-${
          previousMonthLastMondayDayOfMonth + index
        }`
      ).format("MMMM DD"),
      weekOfMonth: getWeekOfMonth(dayjs(
        `${previousMonth.year()}-${previousMonth.month() + 1}-${
          previousMonthLastMondayDayOfMonth + index
        }`)),
    };
  });
}

function createDaysForNextMonth(year, month) {
  const lastDayOfTheMonthWeekday = getWeekday(
    `${year}-${month}-${currentMonthDays.length}`
  );

  const nextMonth = dayjs(`${year}-${month}-01`).add(1, "month");

  const visibleNumberOfDaysFromNextMonth = 6 - lastDayOfTheMonthWeekday;

  return [...Array(visibleNumberOfDaysFromNextMonth)].map((day, index) => {
    return {
      date: dayjs(
        `${nextMonth.year()}-${nextMonth.month() + 1}-${index + 1}`
      ).format("ddd, MMM DD, YYYY"),
      dayOfMonth: index + 1,
      isCurrentMonth: false,
      weekday: dayjs(
        `${nextMonth.year()}-${nextMonth.month() + 1}-${index + 1}`
      ).format("dddd"),
      shortDate: dayjs(
        `${nextMonth.year()}-${nextMonth.month() + 1}-${index + 1}`
      ).format("MMMM DD"),
      weekOfMonth: getWeekOfMonth(dayjs(
        `${nextMonth.year()}-${nextMonth.month() + 1}-${index + 1}`
      )),
    };
  });
}

function getWeekday(date) {
  return dayjs(date).weekday();
}

function initMonthSelectors() {
  document
    .getElementById("previous-month-seek")
    .addEventListener("click", function () {
      selectedMonth = dayjs(selectedMonth).subtract(1, "month");
      createCalendar(selectedMonth.format("YYYY"), selectedMonth.format("M"));
    });

  document
    .getElementById("next-month-seek")
    .addEventListener("click", function () {
      selectedMonth = dayjs(selectedMonth).add(1, "month");
      createCalendar(selectedMonth.format("YYYY"), selectedMonth.format("M"));
    });
}