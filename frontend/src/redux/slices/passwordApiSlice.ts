import type { SetPasswordShape } from "@/pages/SetPasswordPage/SetPasswordPage.types";
import { apiSlice } from "./apiSlice";

export const passwordApiSlice = apiSlice
    .injectEndpoints({
        endpoints: (builder) => ({
            setPassword: builder.mutation({
                query: (passwordDatails: SetPasswordShape) => ({
                    url: "/auth/org_admin_set_password",
                    method: "POST",
                    body: passwordDatails
                }),
            })
        })
    })

export const {
    useSetPasswordMutation
} = passwordApiSlice;