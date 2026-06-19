import { useForm } from "react-hook-form";
import styles from "./SetPasswordPage.module.scss";
import setPassSvg from "@/assets/set-password-side.svg";
import FormInput from "@/components/Form/FormInput/FormInput";
import Button from "@/components/Button/Button";
import { snack } from "@/components/Snackbar/useSnackbarStore";
import { useSearchParams } from "react-router-dom";
import type { SetPassword, SetPasswordShape } from "./SetPasswordPage.types";
import { useSetPasswordMutation } from "@/redux/slices/passwordApiSlice";
import Form from "@/components/Form/Form";
import z from "zod";
import { zodResolver } from "@hookform/resolvers/zod";


const ZPasswordSchema = z.object({
  password: z.string().trim().nonempty("Please enter the password").min(8, "Password should be minimum of 8 characters.").max(30, "Password can't be longer than 30 characters."),
  confirmPassword: z.string().trim().nonempty("Please enter the password").min(8, "Password should be minimum of 8 characters.").max(30, "Password can't be longer than 30 characters."),
}) 


const SetPasswordPage = () => {
  const [searchParams] = useSearchParams();
  const [setPassword, { isLoading }] = useSetPasswordMutation();

  const defaultValues: SetPassword = {
    password: "",
    confirmPassword: ""
  }
  const methods = useForm<SetPassword>({ defaultValues, resolver: zodResolver(ZPasswordSchema) });

  const onSubmit = async (data: SetPassword) => {
    if (data.password !== data.confirmPassword) {
      snack.error("Password mismatch, please  recheck.")
      return;
    }
    const passwordData: SetPasswordShape = {
      token: searchParams.get("token")!,
      email: searchParams.get("email")!,
      password: data.password
    }
    try {
      const response = await setPassword(passwordData).unwrap();
      snack.success(response.message || "Password set succesfully.")
      window.location.href = "/";
    } catch (e: any) {
      snack.error(e.data?.detail || "Something went wrong !");
    }
  }

  return (
    <div className={styles.setPasswordPage}>
      <div className={styles.leftSection}>
        <img src={setPassSvg} alt="set password img" className={styles.sideImg} />
      </div>
      <div className={styles.rightSection}>
        <Form methods={methods} onSubmit={onSubmit} className={styles.setPassForm}>
          <FormInput
            name="password"
            label="Password"
            type="password"
            placeholder="Enter password here.."
          />
          <FormInput
            name="confirmPassword"
            label="Confirm Password"
            type="password"
            placeholder="Confirm your password here.."
          />

          <div className={styles.formButtonsContainer}>
            <Button variant="primary" type="submit">{isLoading ? "Confirming..." : "Confirm"}</Button>
            <Button type="reset">Reset</Button>
          </div>
        </Form>
      </div>
    </div>
  )
}

export default SetPasswordPage