/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui'),],
  daisyui: {
    themes: ["light"], // or false if you don't want default themes
    base: true, // applies daisyUI base styles
    styled: true, // applies daisyUI component styles
    utils: true, // adds daisyUI utilities
    logs: true, // shows logs in console
  },
}

