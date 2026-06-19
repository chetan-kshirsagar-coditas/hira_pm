import type { LoginData, OTPData } from "@/pages/LoginPage/LoginPage.types";
import { apiSlice } from "./apiSlice";
import type { AuthResponse } from "../types";

export const otpApiSlice = apiSlice
    .injectEndpoints({
        endpoints: (builder) => ({
            getOTP: builder.mutation<AuthResponse, LoginData>({
                query: (loginDetails) => ({
                    url: "/auth/request_otp",
                    method: "POST",
                    body: loginDetails
                }),
            }),
            verifyOTP: builder.mutation<AuthResponse, OTPData>({
                query: (otpDetails) => ({
                    url: "/auth/verify_otp",
                    method: "POST",
                    body: otpDetails
                }),
            }),
        })
    })

export const {
    useGetOTPMutation,
    useVerifyOTPMutation } = otpApiSlice;