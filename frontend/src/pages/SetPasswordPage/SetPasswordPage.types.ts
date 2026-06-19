export interface SetPasswordShape {
    token: string,
    email: string,
    password: string
}

export interface SetPassword {
  password: string,
  confirmPassword: string
}