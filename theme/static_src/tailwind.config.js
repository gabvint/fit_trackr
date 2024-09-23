/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            fontFamily:{
                quattrocento: ["Quattrocento", 'system-ui'], 
                questrial: ["Questrial", 'system-ui'],
            },
            colors: {
                black: '#181C14', 
                grey: '#3C3D37', 
                sage: '#697565',
                darkerSage: '#565E50',
                cream: '#ECDFCC',
                terracotta: '#B44C43',
                mutedCoral: '#FFAB76',
                softRose: '#F5B7B1',
                goldenYellow: '#FFD700',
                pastelBlue: '#A2D2FF',
                coolSkyBlue: '#6AB7D8',
                lightGray: '#B5B5B5',
                lightTaupe: '#D1CFC7',
                offWhite: '#F1F1F1',
                warmCoffee: '#4B3F3B',
                slateBlueGreen: '#2A3D45',
            },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
