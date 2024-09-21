/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './**/templates/**/*.html', 
    './static/js/**/*.js', 
    './static/css/**/*.css', 
    './**/static/js/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

