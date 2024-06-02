export default defineNuxtConfig({
  devtools: { enabled: true },
  pages : true,
  css: ['~/assets/css/main.css'],
  modules: [
    'nuxt-icon',
    '@pinia/nuxt',
    '@pinia-plugin-persistedstate/nuxt',

  ],
  build: {
    transpile: ['pinia-plugin-persistedstate'],
  },
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  runtimeConfig: {
    public: {
      apiBase: '/api',
    },
  },
  vite: {
    server: {
      proxy: {
        '/api': {
          target: 'http://localhost:5000',  // URL backend Flask
          changeOrigin: true,
          secure: false,
        },
      },
    },
  },
})
