import { StrictMode, Suspense } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import { RouterProvider } from 'react-router-dom'
import { router } from './router/router.tsx'
import Loader from './components/Loader/Loader.tsx'
import { Provider } from 'react-redux'
import { store } from './redux/store/store.ts'
import { AuthProvider } from './context/AuthContext.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Provider store={store}>
      <AuthProvider>
        <Suspense fallback={<Loader />}>
          <RouterProvider router={router} />
        </Suspense>
      </AuthProvider>
    </Provider>
  </StrictMode>,
)
