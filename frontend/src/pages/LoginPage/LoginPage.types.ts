export interface LoginData{
    email: string
}

export interface OTPShape {
    otp: string
}

export interface OTPData{
    email: string,
    entered_otp: number
}

export type OTPAction = { type: "TOGGLE_OTP_STATE" };
