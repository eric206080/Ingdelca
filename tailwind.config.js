/** Paleta basada en el logo de INGDELCA */
module.exports = {
  content: ['./*.html', './*/index.html', './js/*.js', './tools/*.py'],
  theme: {
    extend: {
      colors: {
        // Azul INGDELCA (gotas del logo)
        primary: {
          50: '#eef6fc', 100: '#d7e9f7', 200: '#b0d3ef', 300: '#7cb5e2', 400: '#4290cf',
          500: '#1c72b8', 600: '#0a5a9e', 700: '#044e8c', 800: '#083f72', 900: '#0b335c', 950: '#061f3d'
        },
        // Celeste INGDELCA (gota clara del logo)
        accent: {
          50: '#ecfaff', 100: '#d3f3fd', 200: '#a9e7fb', 300: '#6fd6f5', 400: '#3abfed',
          500: '#12a6dc', 600: '#0886bb', 700: '#096b97', 800: '#0e597c', 900: '#114a66'
        },
        // Azul marino del texto "INGDELCA"
        navy: { DEFAULT: '#0b386b', dark: '#012054' }
      },
      fontFamily: {
        heading: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
        body: ['"DM Sans"', 'system-ui', 'sans-serif'],
        brand: ['Georgia', '"Times New Roman"', 'serif']
      },
      keyframes: {
        float: { '0%, 100%': { transform: 'translateY(0)' }, '50%': { transform: 'translateY(-14px)' } },
        fadeUp: { from: { opacity: '0', transform: 'translateY(24px)' }, to: { opacity: '1', transform: 'translateY(0)' } }
      },
      animation: {
        float: 'float 7s ease-in-out infinite',
        'fade-up': 'fadeUp .9s ease-out both'
      }
    }
  },
  plugins: []
};
