
<template>
    <div class="flex justify-end p-4">
      <router-link to="Leaves/NewLeave">
        <button class="bg-sky-600 text-white px-4 py-2 rounded-lg">New Leave</button>
      </router-link>
    </div>
    <div class="ml-10 p-10 h-[1100px] is-light-mode calendar-container">
      <Qalendar 
        :events="events"
        :config="config"
      />
    </div>
  </template>
  
  <script>
  import { Qalendar } from "qalendar";
  import { onMounted } from "vue"; // Import onMounted for lifecycle hook
  import { api } from '@/api'; // Import your API module (adjust the path as per your project structure)
  
  export default {
    components: {
      Qalendar,
    },
    data() {
      return {
        events: [],
        config: {
          week: {
            startsOn: 'monday', // Start the week on Monday
            nDays: 7,           // Show 7 days in a week view
            scrollToHour: 5,    // Scroll to 5 AM by default
          },
          style: {
            backgroundColor: "#F0F0F0", // Set background color for the calendar
            colorSchemes: {
              red: {
                backgroundColor: "#FF5733", // Example red color scheme
              },
              blue: {
                backgroundColor: "#337DFF", // Example blue color scheme
              },
              green: {
                backgroundColor: "#33FF57", // Example green color scheme
              },
              yellow: {
                backgroundColor: "#FFFF33", // Example yellow color scheme
              },
              orange: {
                backgroundColor: "#FFA533", // Example orange color scheme
              },
              purple: {
                backgroundColor: "#9333FF", // Example purple color scheme
              },
            },
          },
          dayStyle: {
            // Customize styles for individual days
            isWeekend: {
              backgroundColor: "#FF5733", // Red color for weekends
            },
            isToday: {
              backgroundColor: "#337DFF", // Blue color for today
            },
            // Customize weekdays color
            isWeekday: {
              backgroundColor: "#33FF57", // Green color for weekdays
            },
          },
        },
      };
    },
    // .calendar-month__event .calendar-month__event-title[data-v-4766dfc7]
    methods: {
      async fetchEvents() {
        try {
          const response = await api.get('/holidays/active_holidays'); // Replace with your API endpoint for events
          this.events = response.data.map((event, index) => ({
            id: event.id,
            title: event.description,
            with: event.with,
            time: {
              start: event.date,
              end: event.date,
            },
            color: this.getEventColor(index), // Assign color based on index or event properties
            isEditable: true,
          }));
          console.log('Fetched events:', this.events);
        } catch (error) {
          console.error('Error fetching events:', error);
        }
      },
      
      getEventColor(index) {
        // Example function to return different colors based on index or event properties
        const colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']; // Define your color palette
        return colors[index % colors.length]; // Cycle through colors based on index
      },
    },
    mounted() {
      this.fetchEvents(); // Fetch events when the component is mounted
    },
  };
  </script>
  
  <style>
  @import "qalendar/dist/style.css";
  
  .calendar-container {
    background-color:rgb(243, 244, 246) !important;
    margin-left: 50px;
    /* border-color: black; Set background color for the entire calendar */
  }
  /* .calendar-month .calendar-month__week-day-names, */
  /* .calendar-month__day-date, */
  .calendar-month__weekday:nth-child(6),
  .calendar-month__weekday:nth-child(7){
    background-color: #ffffffb6;
    color: #FF5733 ;
    
  }
  /* .calendar-month__day-date, */
  .calendar-month__day-name:nth-child(6),
  .calendar-month__day-name:nth-child(7) {
    color: #FF5733 !important; /* Red color for Saturday (6th day in a week starting from Monday) */
  }
  /* class="calendar-month__day-name calendar-month__week-day-name" */
  .calendar-month__weekday:nth-child(6) .calendar-month__day-date { /* Saturday */
      color: #FF5733; /* Red text color for Saturdays */
  }
  
  .calendar-month__weekday:nth-child(7) .calendar-month__day-date { /* Sunday */
      color: #FF5733; /* Red text color for Sundays */
  }
  
  
  /* .calendar-week__day:nth-child(6),
  
  .calendar-week__day:nth-child(5), */
  /* .week-timeline__day-name:nth-child(6) .week-timeline__day-name, */
  .week-timeline__day:nth-child(6),
  .week-timeline__day:nth-child(7){
    /* background-color: #ffffff; */
    color: #FF5733 ;
  }
  /* .week-timeline,
  .calendar-root-wrapper .calendar-root, 
  .week-timeline {
    border-color: black !important;
  }
  .day-timeline:not(:last-child),
  .calendar-week__day:not(:last-child) {
      border-right: 1px dashed rgb(2, 2, 2) !important;
  
  }
  .day-timeline:not(:last-child) {
      border-right: 1px dashed rgb(2, 2, 2) !important;
      border-top: 1px dashed rgb(2, 2, 2) !important;
  
  } */
  
  
  
  </style>
  
  
  
  
  
  
  <!-- npm install @schedule-x/vue @schedule-x/theme-default -->
  
  
  