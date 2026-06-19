import type { OTPAction } from "./LoginPage.types";

export const OTPReducer = (state: boolean, action: OTPAction) => {
    switch(action.type){
        case "TOGGLE_OTP_STATE":
            return !state;
        default:
            return state;
    }
}