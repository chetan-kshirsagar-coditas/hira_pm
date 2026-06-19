import type { ButtonProps } from "./Button.types";
import styles from "./Button.module.scss";
import { MultiClass } from "@/utility/classResolve";

const Button = ({ children, className, variant, ...props }: ButtonProps) => {
    return (
        <button className={MultiClass([styles.button, className ? className: "", styles[variant ? variant : ""]])} {...props}>{children}</button>
    )
}

export default Button