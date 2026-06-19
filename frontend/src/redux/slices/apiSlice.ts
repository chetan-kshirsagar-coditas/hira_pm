import { fetchBaseQuery, createApi } from "@reduxjs/toolkit/query/react";



export const apiSlice = createApi({
    baseQuery: fetchBaseQuery(
        {
            baseUrl: import.meta.env.VITE_BACKEND_BASE_URL,
            timeout: 20000,
            prepareHeaders: (headers) => {
                const token = localStorage.getItem('token');
                if(token) headers.set('Authorization', `Bearer ${token}`);
                return headers;
            }
        }
    ),
    tagTypes: ["getOrgs", "getArchivedOrgs"],
    endpoints: () => ({})
})