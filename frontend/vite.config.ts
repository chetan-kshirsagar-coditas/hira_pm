import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'
import dotenv from "dotenv";
dotenv.config();

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  define: {
    "process.env.VITE_BACKEND_BASE_URL": JSON.stringify(process.env.VITE_BACKEND_BASE_URL),
    "process.env.VITE_SUPABASE_KEY": JSON.stringify(process.env.VITE_SUPABASE_KEY),
  },
})






